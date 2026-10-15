# API Testing Automation

A portfolio project demonstrating REST API testing, automated regression testing, input validation, database persistence, and test reporting using Python and pytest.

## Project Overview

This project tests a Task Management API built with FastAPI and SQLAlchemy. It includes automated tests for CRUD operations, request validation, error handling, response schemas, and database integrity.

The goal is to demonstrate practical software quality assurance (QA) skills through repeatable, documented automated tests.

## Test Results

Latest local test execution:

- **49 tests passed**
- **100% statement coverage**
- **87 of 87 executable statements covered**
- Execution time: approximately 5.63 seconds
- One Starlette deprecation warning

> Coverage measures which executable statements were run. It does not guarantee that the application is defect-free or that every possible behavior has been tested.

## Technologies

- Python 3.11
- FastAPI
- SQLAlchemy
- SQLite
- pytest
- HTTPX / FastAPI TestClient
- pytest-cov
- pytest-html
- Postman
- Git and GitHub

## Features Tested

### API functionality
- Root and health endpoints
- Create, retrieve, update, and delete tasks
- Successful and unsuccessful responses
- Task IDs and response schemas

### Negative testing
- Missing required fields
- Empty and whitespace-only titles
- Invalid data types
- Malformed JSON
- Nonexistent task IDs
- Invalid task payloads
- Rejected requests and data integrity

### Boundary-value testing
- One-character task titles
- Titles at the 100-character limit
- Titles exceeding the permitted length
- Descriptions at the 500-character limit
- Descriptions exceeding the permitted length

### Database testing
- Task creation and persistence across database sessions
- Task update persistence
- Deleted records remaining absent
- Database session cleanup on normal and exceptional paths

## Project Structure

```text
api-testing-automation/
├── app/
│   ├── __init__.py
│   ├── database.py
│   └── main.py
├── tests/
│   ├── test_database.py
│   └── test_tasks_api.py
├── docs/
│   ├── TEST_PLAN.md
│   ├── BUG_REPORT.md
│   └── TEST_EXECUTION_REPORT.md
├── postman/
│   └── Task_Management_API.postman_collection.json
├── reports/
│   └── report.html
├── .github/
│   └── workflows/
│       └── tests.yml
├── requirements.txt
└── README.md
```

*The structure above reflects the expected project layout; adjust it if your actual files differ.*

## Installation

Clone the repository and navigate to the project directory.

```bash
git clone https://github.com/cjdaprogrammer/api-testing-automation.git
cd api-testing-automation
```

Create and activate a virtual environment.

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the project dependencies.

```powershell
python -m pip install -r requirements.txt
```

## Run the Automated Tests

Run the complete test suite:

```powershell
python -m pytest tests -v
```

Generate a coverage summary:

```powershell
python -m pytest tests --cov=app --cov-report=term-missing
```

Generate HTML reports:

```powershell
python -m pytest tests --cov=app --cov-report=html --html=reports/report.html --self-contained-html
```

The test report is written to `reports/report.html`, and the coverage report is written to `htmlcov/index.html`.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | API information |
| GET | `/health` | Health check |
| POST | `/tasks` | Create a task |
| GET | `/tasks` | List tasks |
| GET | `/tasks/{task_id}` | Retrieve a task |
| PUT | `/tasks/{task_id}` | Update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

Interactive API documentation is available at `/docs` when the FastAPI application is running.

## QA Documentation

- `docs/TEST_PLAN.md` — test scope, approach, and test scenarios.
- `docs/BUG_REPORT.md` — documented defects and reproducible findings.
- `docs/TEST_EXECUTION_REPORT.md` — execution results and coverage evidence.

## Continuous Integration

The repository includes a GitHub Actions workflow intended to run automated tests. Verify the workflow's current configuration and its latest GitHub Actions run before claiming that CI is passing.

## Skills Demonstrated

- REST API testing
- Positive and negative testing
- Boundary-value analysis
- Equivalence partitioning
- Data validation and integrity testing
- Automated regression testing
- Python and pytest
- SQLAlchemy and SQLite
- Test reporting and code coverage
- QA documentation

## Author

**Clark James De Luna**

- GitHub: https://github.com/cjdaprogrammer
- Portfolio: https://cj-portfolio-lemon.vercel.app

This project is part of my portfolio as an aspiring Junior QA Engineer, demonstrating practical API testing, automation, and software quality assurance skills.
