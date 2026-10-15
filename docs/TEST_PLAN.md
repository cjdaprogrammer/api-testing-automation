# API Testing Automation — Test Plan

## 1. Project Overview

| Item | Details |
|---|---|
| Project | API Testing Automation |
| Application | Task Management REST API |
| Framework | FastAPI |
| Programming language | Python 3.11 |
| Test framework | pytest |
| HTTP testing | FastAPI TestClient / HTTPX |
| Reporting | pytest-html |
| Code coverage | pytest-cov |
| API collection testing | Postman CLI |
| CI/CD | GitHub Actions |
| Database | SQLite with SQLAlchemy |

### Objective

Validate the Task Management API's functionality, input validation, error handling, response structure, and data integrity through repeatable automated tests.

The project demonstrates positive testing, negative testing, boundary-value analysis, regression testing, database testing, reporting, and continuous integration.

## 2. Scope of Testing

### In Scope

- Root and health endpoints
- Task creation, retrieval, updating, and deletion
- HTTP status code validation
- Required-field validation
- Empty and whitespace-only title validation
- Minimum and maximum title length
- Description length boundaries
- Invalid data types and malformed request data
- Existing and nonexistent task IDs
- Response structure and data types
- Data integrity after rejected update requests
- Database persistence and session cleanup
- Postman collection execution
- Automated test reporting and code coverage
- GitHub Actions workflow execution

### Out of Scope

- Authentication and authorization
- Production database deployment and migration validation
- Load and stress testing
- Comprehensive security and penetration testing
- Third-party integrations
- Production deployment validation

## 3. Test Environment

| Component | Configuration |
|---|---|
| Operating system | Windows locally; Ubuntu GitHub Actions runner |
| Programming language | Python 3.11 |
| API framework | FastAPI |
| Test framework | pytest |
| HTTP client | FastAPI TestClient / HTTPX |
| Database | SQLite with SQLAlchemy |
| Reporting | pytest-html |
| Coverage | pytest-cov |
| API collection | Postman CLI |
| CI/CD | GitHub Actions |

## 4. API Endpoints Under Test

| Method | Endpoint | Expected Behavior |
|---|---|---|
| GET | `/` | Returns API information |
| GET | `/health` | Returns a healthy status |
| POST | `/tasks` | Creates a task |
| GET | `/tasks` | Returns the task collection |
| GET | `/tasks/{task_id}` | Returns a task by ID |
| PUT | `/tasks/{task_id}` | Updates an existing task |
| DELETE | `/tasks/{task_id}` | Deletes an existing task |

## 5. Test Scenarios

### A. Root and Health Endpoints

- Verify the root endpoint returns HTTP 200.
- Verify the health endpoint returns HTTP 200.
- Verify the health response contains the expected status.

### B. Task Creation and Validation

- Verify valid task creation returns HTTP 201.
- Verify required fields are validated.
- Verify empty and whitespace-only titles are rejected.
- Verify a one-character title is accepted.
- Verify a 100-character title is accepted.
- Verify a title exceeding 100 characters is rejected.
- Verify a 500-character description is accepted.
- Verify a description exceeding 500 characters is rejected.
- Verify invalid field types are rejected.
- Verify an empty JSON object is rejected.
- Verify returned task fields and data types are correct.
- Verify a rejected create request does not persist a task.

### C. Task Retrieval

- Verify all tasks can be retrieved.
- Verify a task can be retrieved by ID.
- Verify an empty task collection returns an empty list.
- Verify a nonexistent task returns HTTP 404.
- Verify a nonnumeric task ID returns HTTP 422.

### D. Task Updates

- Verify an existing task can be updated.
- Verify updating a nonexistent task returns HTTP 404.
- Verify invalid update payloads return HTTP 422.
- Verify whitespace-only titles are rejected during updates.
- Verify overlong descriptions are rejected.
- Verify rejected updates do not modify existing task data.

### E. Task Deletion

- Verify an existing task can be deleted.
- Verify successful deletion returns the expected response.
- Verify a deleted task can no longer be retrieved.
- Verify deleting a nonexistent task returns HTTP 404.

### F. Database Behavior

- Verify task data persists across separate database sessions.
- Verify updates remain persisted.
- Verify deleted records remain absent.
- Verify database sessions are cleaned up during normal and exceptional execution paths.

### G. Postman and CI/CD

- Verify the Postman collection executes successfully.
- Verify the collection's request assertions pass.
- Verify GitHub Actions executes the configured automated checks.
- Verify reports are uploaded as workflow artifacts when generated.

## 6. Expected HTTP Status Codes

| Status Code | Meaning | Example |
|---|---|---|
| 200 | OK | Successful retrieval or update |
| 201 | Created | Successful task creation |
| 404 | Not Found | Request for a nonexistent task |
| 422 | Unprocessable Entity | Invalid request data |

These are the expected status codes for the scenarios listed above. Actual behavior should be confirmed against the running API.

## 7. Test Data

### Valid Request

```json
{
  "title": "Complete API testing",
  "description": "Validate task management endpoints",
  "completed": false
}
```

### Invalid and Boundary Test Data

| Field | Input | Expected Result |
|---|---|---|
| title | Missing | HTTP 422 |
| title | Empty string | HTTP 422 |
| title | Whitespace only | HTTP 422 |
| title | One character | HTTP 201 |
| title | 100 characters | HTTP 201 |
| title | 101 characters | HTTP 422 |
| description | 500 characters | HTTP 201 |
| description | 501 characters | HTTP 422 |
| description | Numeric value | HTTP 422 |
| Request body | Empty object | HTTP 422 |
| task ID | Nonnumeric value | HTTP 422 |

## 8. Test Execution Procedure

1. Install the project dependencies.
2. Run the automated pytest suite.
3. Investigate any failed tests.
4. Generate an HTML test report.
5. Review the coverage report.
6. Run the Postman collection against the API.
7. Record the actual results and warnings.
8. Commit and push approved changes.
9. Verify the GitHub Actions workflow.

### Run pytest with coverage and HTML reporting

From the project root in PowerShell:

```powershell
New-Item -ItemType Directory -Force reports | Out-Null

python -m pytest tests -v `
  --cov=app `
  --cov-report=term-missing `
  --cov-report=html:reports/coverage `
  --html=reports/report.html `
  --self-contained-html
```

### Run the Postman collection

Start the API in one terminal:

```powershell
python -m uvicorn app.main:app --reload
```

In a second terminal, from the project root:

```powershell
postman collection run .\postman\Task_Management_API.postman_collection.json
```

Review the command output to confirm the actual request and assertion results.

## 9. Entry Criteria

- Python and project dependencies are installed.
- The application can be imported and started.
- Test files and the Postman collection are available.
- The required test environment is accessible.

## 10. Exit Criteria

- Automated test execution is complete.
- Failures have been investigated and documented.
- Confirmed defects have appropriate regression tests.
- Coverage and test reports have been reviewed.
- Postman checks have been executed and reviewed.
- GitHub Actions completes successfully for the intended change.

## 11. Risks and Limitations

- SQLite is used for persistence; production database deployment and migration behavior are outside the current scope.
- Authentication and authorization are not implemented.
- Load, stress, and comprehensive security testing are outside the documented scope.
- Passing tests and high statement coverage do not guarantee the absence of defects.
- Test results may vary with dependency versions and environment configuration.

## 12. Test Results

Execution metrics belong in `docs/TEST_EXECUTION_REPORT.md`.

For the latest results, review:

- Pytest terminal output
- Postman CLI output
- Coverage report
- GitHub Actions workflow run

Historical results should not be presented as results from a new execution.

## 13. Conclusion

This test plan defines the scope, endpoints, test data, validation scenarios, execution procedures, entry criteria, exit criteria, and limitations for the Task Management API.

It demonstrates a structured approach to API quality assurance using Python, pytest, FastAPI, SQLite, Postman, test reporting, code coverage, and continuous integration.
