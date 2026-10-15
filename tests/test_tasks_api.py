import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database import Base, get_db
from app.main import app, TaskRecord



@pytest.fixture
def test_engine():
    """Create an isolated in-memory database for each test."""
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )

    Base.metadata.create_all(bind=engine)

    try:
        yield engine
    finally:
        Base.metadata.drop_all(bind=engine)
        engine.dispose()


@pytest.fixture
def testing_session_local(test_engine):
    """Create sessions connected to the isolated test database."""
    return sessionmaker(
        bind=test_engine,
        autoflush=False,
        autocommit=False,
    )


@pytest.fixture
def client(test_engine, testing_session_local):
    """Provide an API client using the isolated test database."""

    def override_get_db():
        db = testing_session_local()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    try:
        with TestClient(app) as test_client:
            yield test_client
    finally:
        app.dependency_overrides.pop(get_db, None)


@pytest.fixture
def sample_task():
    """Reusable valid task payload."""
    return {
        "title": "Complete QA portfolio",
        "description": "Write automated API tests",
        "completed": False,
    }


# --------------------------------------------------
# Root and health endpoints
# --------------------------------------------------

def test_root_endpoint_returns_success(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Task Management API is running"
    assert response.json()["docs"] == "/docs"


def test_health_check_returns_healthy_status(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


# --------------------------------------------------
# Create and retrieve tasks
# --------------------------------------------------

def test_create_task_returns_201(client, sample_task):
    response = client.post("/tasks", json=sample_task)

    assert response.status_code == 201

    data = response.json()
    assert data["id"] == 1
    assert data["title"] == sample_task["title"]
    assert data["description"] == sample_task["description"]
    assert data["completed"] is False


def test_get_tasks_returns_created_tasks(client, sample_task):
    client.post("/tasks", json=sample_task)

    response = client.get("/tasks")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["title"] == sample_task["title"]


def test_get_task_by_id(client, sample_task):
    created = client.post("/tasks", json=sample_task).json()

    response = client.get(f"/tasks/{created['id']}")

    assert response.status_code == 200
    assert response.json() == created


def test_get_nonexistent_task_returns_404(client):
    response = client.get("/tasks/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"


def test_empty_task_list_returns_empty_array(client):
    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.json() == []


# --------------------------------------------------
# Create validation
# --------------------------------------------------

def test_create_task_without_title_returns_422(client):
    response = client.post(
        "/tasks",
        json={"description": "A task without a title"},
    )

    assert response.status_code == 422


def test_create_task_with_empty_title_returns_422(client):
    response = client.post("/tasks", json={"title": ""})

    assert response.status_code == 422


def test_create_task_with_title_over_100_characters_returns_422(client):
    response = client.post("/tasks", json={"title": "A" * 101})

    assert response.status_code == 422


def test_create_task_with_invalid_completed_type_returns_422(client):
    response = client.post(
        "/tasks",
        json={
            "title": "Test invalid type",
            "completed": "not-a-boolean",
        },
    )

    assert response.status_code == 422


@pytest.mark.parametrize(
    "title",
    ["", " ", "A" * 101],
    ids=["empty-title", "whitespace-title", "title-over-100-characters"],
)
def test_create_task_with_invalid_titles_returns_422(client, title):
    response = client.post("/tasks", json={"title": title})

    assert response.status_code == 422


# --------------------------------------------------
# Update tasks and validate data integrity
# --------------------------------------------------

def test_update_task(client, sample_task):
    created = client.post("/tasks", json=sample_task).json()

    updated_payload = {
        "title": "Updated QA portfolio",
        "description": "Test the update endpoint",
        "completed": True,
    }

    response = client.put(
        f"/tasks/{created['id']}",
        json=updated_payload,
    )

    assert response.status_code == 200
    assert response.json()["id"] == created["id"]
    assert response.json()["title"] == updated_payload["title"]
    assert response.json()["description"] == updated_payload["description"]
    assert response.json()["completed"] is True


def test_update_nonexistent_task_returns_404(client, sample_task):
    response = client.put("/tasks/999", json=sample_task)

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"


def test_update_task_with_whitespace_title_returns_422(client, sample_task):
    created = client.post("/tasks", json=sample_task).json()

    response = client.put(
        f"/tasks/{created['id']}",
        json={
            "title": "   ",
            "description": "This update should be rejected",
            "completed": True,
        },
    )

    assert response.status_code == 422

    unchanged = client.get(f"/tasks/{created['id']}")

    assert unchanged.status_code == 200
    assert unchanged.json()["title"] == sample_task["title"]
    assert unchanged.json()["completed"] is False


@pytest.mark.parametrize(
    "payload",
    [
        {"title": ""},
        {"title": "   "},
        {"title": "A" * 101},
        {"title": "Valid title", "completed": "not-a-boolean"},
    ],
    ids=[
        "empty-title",
        "whitespace-title",
        "title-too-long",
        "invalid-completed-type",
    ],
)
def test_update_task_with_invalid_payload_returns_422(
    client, sample_task, payload
):
    created = client.post("/tasks", json=sample_task).json()

    response = client.put(
        f"/tasks/{created['id']}",
        json=payload,
    )

    assert response.status_code == 422

    current = client.get(f"/tasks/{created['id']}")

    assert current.status_code == 200
    assert current.json()["title"] == sample_task["title"]
    assert current.json()["description"] == sample_task["description"]
    assert current.json()["completed"] is False


# --------------------------------------------------
# Delete tasks
# --------------------------------------------------

def test_delete_task(client, sample_task):
    created = client.post("/tasks", json=sample_task).json()

    response = client.delete(f"/tasks/{created['id']}")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Task deleted successfully"
    }

    get_response = client.get(f"/tasks/{created['id']}")
    assert get_response.status_code == 404


def test_delete_nonexistent_task_returns_404(client):
    response = client.delete("/tasks/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"


def test_new_task_ids_increment(client):
    first = client.post(
        "/tasks",
        json={"title": "First task"},
    ).json()

    second = client.post(
        "/tasks",
        json={"title": "Second task"},
    ).json()

    assert first["id"] == 1
    assert second["id"] == 2


# --------------------------------------------------
# Response schema
# --------------------------------------------------

def test_created_task_response_has_expected_schema(client, sample_task):
    response = client.post("/tasks", json=sample_task)

    assert response.status_code == 201

    data = response.json()

    assert set(data.keys()) == {
        "id",
        "title",
        "description",
        "completed",
    }
    assert isinstance(data["id"], int)
    assert isinstance(data["title"], str)
    assert isinstance(data["description"], str)
    assert isinstance(data["completed"], bool)


# --------------------------------------------------
# Boundary and input-validation tests
# --------------------------------------------------

def test_create_task_with_one_character_title_returns_201(client):
    response = client.post("/tasks", json={"title": "A"})

    assert response.status_code == 201
    assert response.json()["title"] == "A"


def test_create_task_with_exactly_100_character_title_returns_201(client):
    title = "A" * 100

    response = client.post("/tasks", json={"title": title})

    assert response.status_code == 201
    assert response.json()["title"] == title
    assert len(response.json()["title"]) == 100


def test_create_task_with_description_at_500_characters_returns_201(client):
    description = "D" * 500

    response = client.post(
        "/tasks",
        json={
            "title": "Boundary test",
            "description": description,
        },
    )

    assert response.status_code == 201
    assert response.json()["description"] == description
    assert len(response.json()["description"]) == 500


def test_create_task_with_description_over_500_characters_returns_422(client):
    response = client.post(
        "/tasks",
        json={
            "title": "Boundary test",
            "description": "D" * 501,
        },
    )

    assert response.status_code == 422


def test_create_task_with_numeric_description_returns_422(client):
    response = client.post(
        "/tasks",
        json={
            "title": "Invalid description",
            "description": 12345,
        },
    )

    assert response.status_code == 422


def test_create_task_with_empty_json_object_returns_422(client):
    response = client.post("/tasks", json={})

    assert response.status_code == 422


def test_get_task_with_non_numeric_id_returns_422(client):
    response = client.get("/tasks/not-a-number")

    assert response.status_code == 422


def test_update_task_with_description_over_500_characters_returns_422(
    client, sample_task
):
    created = client.post("/tasks", json=sample_task).json()

    response = client.put(
        f"/tasks/{created['id']}",
        json={
            "title": "Updated task",
            "description": "D" * 501,
            "completed": True,
        },
    )

    assert response.status_code == 422

    current = client.get(f"/tasks/{created['id']}")

    assert current.status_code == 200
    assert current.json()["title"] == sample_task["title"]
    assert current.json()["description"] == sample_task["description"]
    assert current.json()["completed"] is False


# --------------------------------------------------
# Database persistence tests
# --------------------------------------------------

def test_created_task_persists_across_database_sessions(
    client, sample_task, testing_session_local
):
    response = client.post("/tasks", json=sample_task)

    assert response.status_code == 201
    task_id = response.json()["id"]

    # Open a separate database session.
    with testing_session_local() as db:
        saved_task = db.get(TaskRecord, task_id)

        assert saved_task is not None
        assert saved_task.title == sample_task["title"]
        assert saved_task.description == sample_task["description"]
        assert saved_task.completed is False


def test_updated_task_persists_across_database_sessions(
    client, sample_task, testing_session_local
):
    created = client.post("/tasks", json=sample_task).json()
    task_id = created["id"]

    updated_payload = {
        "title": "Persisted updated task",
        "description": "Verify database update",
        "completed": True,
    }

    response = client.put(
        f"/tasks/{task_id}",
        json=updated_payload,
    )

    assert response.status_code == 200

    # Verify the update using a separate session.
    with testing_session_local() as db:
        saved_task = db.get(TaskRecord, task_id)

        assert saved_task is not None
        assert saved_task.title == updated_payload["title"]
        assert saved_task.description == updated_payload["description"]
        assert saved_task.completed is True


def test_deleted_task_remains_deleted_in_database(
    client, sample_task, testing_session_local
):
    created = client.post("/tasks", json=sample_task).json()
    task_id = created["id"]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 200

    # Verify deletion using a separate session.
    with testing_session_local() as db:
        deleted_task = db.get(TaskRecord, task_id)
        assert deleted_task is None


# --------------------------------------------------
# Additional negative API tests
# --------------------------------------------------

def test_create_task_with_null_json_returns_422(client):
    response = client.post("/tasks", json=None)

    assert response.status_code == 422


def test_create_task_with_null_title_returns_422(client):
    response = client.post(
        "/tasks",
        json={"title": None},
    )

    assert response.status_code == 422


def test_create_task_with_list_instead_of_object_returns_422(client):
    response = client.post(
        "/tasks",
        json=["Task title", "Task description"],
    )

    assert response.status_code == 422


def test_create_task_with_boolean_title_returns_422(client):
    response = client.post(
        "/tasks",
        json={"title": True},
    )

    assert response.status_code == 422


def test_create_task_with_invalid_request_body_returns_422(client):
    response = client.post(
        "/tasks",
        content='{"title": "Incomplete JSON"',
        headers={"Content-Type": "application/json"},
    )

    assert response.status_code == 422


def test_invalid_create_request_does_not_create_task(client):
    response = client.post(
        "/tasks",
        json={"title": "   "},
    )

    assert response.status_code == 422

    tasks_response = client.get("/tasks")

    assert tasks_response.status_code == 200
    assert tasks_response.json() == []


@pytest.mark.parametrize("task_id", [0, -1, -100])
def test_get_task_with_nonpositive_id_returns_404(client, task_id):
    response = client.get(f"/tasks/{task_id}")

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"


def test_update_task_without_title_returns_422(client, sample_task):
    created = client.post("/tasks", json=sample_task).json()

    response = client.put(
        f"/tasks/{created['id']}",
        json={
            "description": "Missing title",
            "completed": True,
        },
    )

    assert response.status_code == 422

    current = client.get(f"/tasks/{created['id']}")

    assert current.status_code == 200
    assert current.json()["title"] == sample_task["title"]
    assert current.json()["completed"] is False


def test_update_task_with_null_description_returns_422(client, sample_task):
    created = client.post("/tasks", json=sample_task).json()

    response = client.put(
        f"/tasks/{created['id']}",
        json={
            "title": "Updated title",
            "description": None,
            "completed": True,
        },
    )

    assert response.status_code == 422

    current = client.get(f"/tasks/{created['id']}")

    assert current.status_code == 200
    assert current.json()["title"] == sample_task["title"]
    assert current.json()["description"] == sample_task["description"]
    assert current.json()["completed"] is False
