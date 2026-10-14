
# API Testing Automation — Test Plan

## 1. Project Overview

**Project Name:** API Testing Automation  
**Application:** Task Management REST API  
**Framework:** FastAPI  
**Programming Language:** Python 3.11  
**Test Framework:** Pytest  
**HTTP Testing:** FastAPI TestClient / HTTPX  
**Reporting:** pytest-html  
**Code Coverage:** pytest-cov  
**API Collection Testing:** Postman CLI  
**CI/CD:** GitHub Actions

### Objective

Validate the functionality, input validation, error handling, and data integrity of the Task Management API using automated API tests.

The project demonstrates practical quality assurance skills through positive testing, negative testing, boundary-value analysis, regression testing, reporting, and continuous integration.

## 2. Scope of Testing

### In Scope

- Root and health endpoints
- Task creation, retrieval, updating, and deletion
- HTTP status code validation
- Required-field validation
- Empty and whitespace-only title validation
- Minimum and maximum title length
- Description length boundaries
- Invalid data types
- Missing and malformed request data
- Existing and nonexistent task IDs
- Response structure and data types
- Data integrity after rejected update requests
- Postman collection execution
- Automated test reporting and code coverage

### Out of Scope

- Authentication and authorization
- Production database integration
- Load and stress testing
- Security penetration testing
- Third-party integrations
- Production deployment validation

## 3. Test Environment

| Component | Configuration |
|---|---|
| Operating System | Windows / GitHub Actions Linux runner |
| Programming Language | Python 3.11 |
| API Framework | FastAPI |
| Test Framework | Pytest |
| HTTP Client | FastAPI TestClient / HTTPX |
| Reporting | pytest-html |
| Coverage | pytest-cov |
| API Collection | Postman CLI |
| CI/CD | GitHub Actions |

## 4. API Endpoints Under Test

| Method | Endpoint | Expected Behavior |
|---|---|---|
| GET | `/` | Returns API welcome information |
| GET | `/health` | Returns healthy status |
| POST | `/tasks` | Creates a task |
| GET | `/tasks` | Returns all tasks |
| GET | `/tasks/{task_id}` | Returns a task by ID |
| PUT | `/tasks/{task_id}` | Updates an existing task |
| DELETE | `/tasks/{task_id}` | Deletes an existing task |

## 5. Test Scenarios

### A. Health and Root Endpoints

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
- Verify successful deletion returns the expected message.
- Verify a deleted task can no longer be retrieved.
- Verify deleting a nonexistent task returns HTTP 404.

### F. Postman and CI/CD

- Verify the Postman collection executes successfully.
- Verify request assertions pass.
- Verify GitHub Actions executes the automated checks.
- Verify test reports are uploaded as workflow artifacts when generated.

## 6. Expected HTTP Status Codes

| Status Code | Meaning | Example |
|---|---|---|
| 200 | OK | Retrieve or update a task |
| 201 | Created | Create a task successfully |
| 404 | Not Found | Request a nonexistent task |
| 422 | Unprocessable Entity | Submit invalid input |

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
| task_id | Nonnumeric value | HTTP 422 |

## 8. Test Execution Procedure

1. Install project dependencies.
2. Execute the Pytest suite.
3. Review failures and investigate defects.
4. Generate an HTML test report.
5. Review code coverage.
6. Execute the Postman collection against a running API.
7. Commit and push approved changes.
8. Verify the GitHub Actions workflow.

### Run Pytest with HTML Report and Coverage

```powershell
.\.venv\Scripts\python.exe -m pytest -v --cov=app --cov-report=term-missing --cov-report=html:reports/coverage --html=reports/report.html --self-contained-html
```

### Run Postman Collection

Start the API in one PowerShell terminal:

```powershell
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

In a second terminal, from the project root:

```powershell
postman collection run .\postman\Task_Management_API.postman_collection.json --reporters cli
```

## 9. Entry Criteria

- Python and project dependencies are installed.
- The application can be imported.
- Test files and the Postman collection are available.
- The required test environment is accessible.

## 10. Exit Criteria

- Automated test execution is complete.
- Failures have been investigated.
- Regression tests cover confirmed defects.
- Coverage and test reports have been reviewed.
- Postman checks have been executed.
- GitHub Actions completes successfully.

## 11. Risks and Limitations

- Tasks are stored in memory; restarting the application resets the data.
- The tests use a controlled test environment.
- Authentication, authorization, production database behavior, performance, and penetration testing are outside the current scope.
- Passing tests does not guarantee the absence of all defects.

## 12. Test Results

Record results from the latest actual execution. Do not treat historical results as a new run.

- **Pytest result:** See the latest terminal output.
- **Postman result:** See the latest Postman CLI output.
- **Code coverage:** See the latest coverage report.
- **CI/CD result:** See the latest GitHub Actions run.

Refer to `TEST_EXECUTION_REPORT.md` for the recorded execution summary.

## 13. Conclusion

This test plan defines the scope, endpoints, test data, validation scenarios, execution procedures, and completion criteria for the Task Management API.

It demonstrates a structured approach to API quality assurance using Python, Pytest, FastAPI, Postman, test reporting, code coverage, and continuous integration.
