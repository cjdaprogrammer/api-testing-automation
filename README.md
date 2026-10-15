# API Testing Automation

[![API Testing Automation](https://github.com/cjdaprogrammer/api-testing-automation/actions/workflows/tests.yml/badge.svg)](https://github.com/cjdaprogrammer/api-testing-automation/actions/workflows/tests.yml)

A Python-based API testing portfolio project demonstrating REST API validation, automated regression testing, negative testing, boundary-value analysis, SQLite persistence, and continuous integration.

This project tests a Task Management REST API built with **FastAPI, SQLAlchemy, and SQLite**. It combines automated pytest tests, a Postman collection, coverage reports, and QA documentation to demonstrate a practical software testing workflow.

## Project Highlights

- Automated API regression tests using pytest
- CRUD endpoint testing: create, retrieve, update, and delete tasks
- Positive, negative, and boundary-value testing
- Request validation and error-handling checks
- Database persistence and session-cleanup tests
- HTML test reports and code coverage reporting
- Postman collection execution through GitHub Actions
- QA documentation, including a test plan, bug report, and execution report

## Test Results

**Latest recorded local test run**

| Metric | Result |
|---|---|
| Automated tests | 49 passed |
| Statement coverage | 100% |
| Executable statements covered | 87 of 87 |
| Execution time | Approximately 5.63 seconds |

These results describe a local test run, not a guarantee that every possible defect or behavior has been tested. Coverage measures which executable statements were exercised; it does not measure the quality or completeness of all tests.

For the current CI result, see the [GitHub Actions workflow](https://github.com/cjdaprogrammer/api-testing-automation/actions).

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.11 | Application and test code |
| FastAPI | REST API framework |
| SQLAlchemy | Database operations |
| SQLite | Persistent data storage |
| pytest | Automated test execution |
| HTTPX / FastAPI TestClient | API test requests |
| pytest-cov | Coverage measurement |
| pytest-html | HTML test reports |
| Postman CLI | API collection execution in CI |
| Git and GitHub Actions | Version control and continuous integration |

## Testing Scope

### API functionality
- Root and health endpoints
- Create, list, retrieve, update, and delete tasks
- Successful and unsuccessful HTTP responses
- Task identifiers and response structures

### Negative testing and validation
- Missing required fields
- Empty and whitespace-only task titles
- Invalid data types and task payloads
- Malformed JSON
- Requests involving nonexistent task IDs
- Rejected requests and data-integrity checks

### Boundary-value analysis
- One-character task titles
- Titles at and beyond the 100-character limit
- Descriptions at and beyond the 500-character limit

### Database testing
- Task persistence across separate database sessions
- Update persistence
- Deleted records remaining absent
- Database session cleanup during normal and exceptional execution paths

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

FastAPI provides interactive API documentation at `/docs` while the application is running.

## Getting Started

### Prerequisites
- Python 3.11
- Git

### 1. Clone the repository

```bash
git clone https://github.com/cjdaprogrammer/api-testing-automation.git
cd api-testing-automation
```

### 2. Create and activate a virtual environment

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script activation, follow your organization's security policy or use a supported activation method for your environment.

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Run the automated tests

```powershell
python -m pytest tests -v
```

### 5. Run tests with coverage

```powershell
python -m pytest tests --cov=app --cov-report=term-missing
```

### 6. Generate HTML reports

Create the reports directory first:

```powershell
New-Item -ItemType Directory -Force reports
```

Then run:

```powershell
python -m pytest tests --cov=app --cov-report=html:htmlcov --html=reports/report.html --self-contained-html
```

Open the reports after the run:

- Pytest report: `reports/report.html`
- Coverage report: `htmlcov/index.html`

## Postman Testing

The repository includes a Postman collection at:

`postman/Task_Management_API.postman_collection.json`

The GitHub Actions workflow starts the API server and runs the collection using Postman CLI. The API server must be running and reachable for local collection execution.

## Continuous Integration

The GitHub Actions workflow is defined in `.github/workflows/tests.yml`. It is configured to run on pushes and pull requests targeting `main` or `master`, and can also be started manually.

The workflow:
1. Checks out the repository.
2. Sets up Python and installs dependencies.
3. Runs pytest with coverage and HTML reporting.
4. Uploads pytest reports as workflow artifacts.
5. Starts the API server.
6. Runs the Postman collection.
7. Uploads the API server log as an artifact.

Check the [workflow runs](https://github.com/cjdaprogrammer/api-testing-automation/actions) for the latest execution status and details.

## QA Documentation

- [Test Plan](docs/TEST_PLAN.md) — testing scope, approach, and scenarios.
- [Bug Report](docs/BUG_REPORT.md) — documented defect details and reproducible findings.
- [Test Execution Report](docs/TEST_EXECUTION_REPORT.md) — recorded test results and coverage evidence.

## Skills Demonstrated

- REST API testing
- Positive and negative testing
- Boundary-value analysis
- Equivalence partitioning
- Request and response validation
- Automated regression testing
- Database persistence and data integrity
- Python and pytest
- SQLAlchemy and SQLite
- Postman API testing
- Test reporting and code coverage
- QA documentation and continuous integration

## Project Limitations

This project is a learning and portfolio application, not a production-ready service. Its current scope does not establish production-grade authentication, authorization, load testing, or comprehensive security testing.

## Author

**Clark James De Luna**

Aspiring Junior QA Engineer

- GitHub: [cjdaprogrammer](https://github.com/cjdaprogrammer)
- Portfolio: [cj-portfolio-lemon.vercel.app](https://cj-portfolio-lemon.vercel.app)
