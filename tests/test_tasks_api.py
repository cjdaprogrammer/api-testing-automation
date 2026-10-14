import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    """Create a fresh API client and isolated task storage for each test."""
    from app import main

    main.tasks.clear()
    main.next_task_id = 1

    with TestClient(app) as test_client:
        yield test_client

    main.tasks.clear()
    main.next_task_id = 1


@pytest.fixture
def sample_task():
    """Reusable valid task payload."""
    return {
        "title": "Complete QA portfolio",
        "description": "Write automated API tests",
        "completed": False,
    }


def test_root_endpoint_returns_success(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Task Management API is running"
    assert response.json()["docs"] == "/docs"


def test_health_check_returns_healthy_status(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


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


def test_create_task_without_title_returns_422(client):
    response = client.post(
        "/tasks",
        json={"description": "A task without a title"},
    )

    assert response.status_code == 422


def test_create_task_with_empty_title_returns_422(client):
    response = client.post(
        "/tasks",
        json={"title": ""},
    )

    assert response.status_code == 422


def test_create_task_with_title_over_100_characters_returns_422(client):
    response = client.post(
        "/tasks",
        json={"title": "A" * 101},
    )

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
    assert response.json()["completed"] is True


def test_update_nonexistent_task_returns_404(client, sample_task):
    response = client.put("/tasks/999", json=sample_task)

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"


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


def test_empty_task_list_returns_empty_array(client):
    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.parametrize(
    "title",
    [
        "",
        " ",
        "A" * 101,
    ],
    ids=[
        "empty-title",
        "whitespace-title",
        "title-over-100-characters",
    ],
)
def test_create_task_with_invalid_titles_returns_422(client, title):
    response = client.post(
        "/tasks",
        json={"title": title},
    )

    assert response.status_code == 422


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

    # Verify that the original task remains unchanged.
    unchanged = client.get(f"/tasks/{created['id']}")

    assert unchanged.status_code == 200
    assert unchanged.json()["title"] == sample_task["title"]
    assert unchanged.json()["completed"] is False

