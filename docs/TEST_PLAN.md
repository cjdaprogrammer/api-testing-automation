\# API Testing Automation — Test Plan



\## 1. Project Overview



\*\*Project Name:\*\* Task Management API Testing Automation



\*\*Application:\*\* Task Management REST API



\*\*Framework:\*\* Pytest



\*\*API Client:\*\* HTTPX / FastAPI TestClient



\*\*Programming Language:\*\* Python



\*\*Reporting:\*\* pytest-html



\*\*CI/CD:\*\* GitHub Actions



\### Objective



The objective of this project is to validate the functionality, reliability, and input validation of a REST API through automated testing.



The test suite verifies that API endpoints return the expected HTTP status codes, response data, and error messages for valid and invalid requests.



\## 2. Scope of Testing



\### In Scope



\- API health checks

\- Task creation

\- Retrieving all tasks

\- Retrieving a task by ID

\- Updating an existing task

\- Deleting an existing task

\- Request payload validation

\- Required field validation

\- Title length validation

\- Whitespace-only title validation

\- Invalid data type handling

\- Handling requests for nonexistent task IDs

\- Response structure and data type validation

\- Data integrity after rejected update requests



\### Out of Scope



\- Production database integration

\- Authentication and authorization

\- Load and stress testing

\- Security penetration testing

\- Third-party API integration

\- Production deployment validation



\## 3. Test Environment



| Component | Configuration |

|---|---|

| Operating System | Windows |

| Language | Python 3.11 |

| API Framework | FastAPI |

| Test Framework | Pytest |

| HTTP Testing | FastAPI TestClient / HTTPX |

| HTML Reports | pytest-html |

| Code Coverage | pytest-cov |

| CI/CD | GitHub Actions |



\## 4. API Endpoints Under Test



| Method | Endpoint | Expected Behavior |

|---|---|---|

| GET | `/` | Returns the API welcome message |

| GET | `/health` | Returns a healthy status |

| POST | `/tasks` | Creates a task |

| GET | `/tasks` | Returns the task collection |

| GET | `/tasks/{task\_id}` | Returns a task by ID |

| PUT | `/tasks/{task\_id}` | Updates an existing task |

| DELETE | `/tasks/{task\_id}` | Deletes an existing task |



\## 5. Test Scenarios



\### A. Health and Availability



\- Verify the root endpoint returns HTTP 200.

\- Verify the health endpoint returns HTTP 200.

\- Verify the health response contains the expected status.



\### B. Task Creation



\- Verify a valid task can be created.

\- Verify successful creation returns HTTP 201.

\- Verify the created task has the expected fields and data types.

\- Verify a missing title is rejected.

\- Verify an empty title is rejected.

\- Verify a whitespace-only title is rejected.

\- Verify a title longer than 100 characters is rejected.

\- Verify an invalid value for the `completed` field is rejected.



\### C. Task Retrieval



\- Verify all tasks can be retrieved.

\- Verify a task can be retrieved using its ID.

\- Verify requesting a nonexistent task returns HTTP 404.

\- Verify an empty task collection returns an empty list.



\### D. Task Updates



\- Verify an existing task can be updated.

\- Verify updating a nonexistent task returns HTTP 404.

\- Verify invalid update payloads return HTTP 422.

\- Verify whitespace-only titles are rejected during updates.

\- Verify a rejected update does not change the existing task.



\### E. Task Deletion



\- Verify an existing task can be deleted.

\- Verify successful deletion returns the expected success message.

\- Verify deleting a nonexistent task returns HTTP 404.

\- Verify task IDs are assigned incrementally during creation.



\## 6. Expected HTTP Status Codes



| Status Code | Meaning | Example |

|---|---|---|

| 200 | OK | Retrieve or update a task |

| 201 | Created | Create a task successfully |

| 404 | Not Found | Request a nonexistent task |

| 422 | Unprocessable Entity | Submit invalid request data |



\## 7. Test Data



\### Valid Test Data



```json

{

&#x20; "title": "Complete API testing",

&#x20; "description": "Validate task management endpoints",

&#x20; "completed": false

}

```



\### Invalid Test Data



| Field | Invalid Value | Expected Result |

|---|---|---|

| title | Missing | HTTP 422 |

| title | Empty string | HTTP 422 |

| title | Whitespace only | HTTP 422 |

| title | More than 100 characters | HTTP 422 |

| completed | Invalid string value | HTTP 422 |



\## 8. Test Execution Procedure



1\. Install the project dependencies.

2\. Run the automated test suite.

3\. Review test results and investigate failures.

4\. Generate an HTML test report.

5\. Review code coverage.

6\. Push approved changes to GitHub.

7\. Verify that the GitHub Actions workflow completes successfully.



\### Commands



Run all tests:



```powershell

.\\.venv\\Scripts\\python.exe -m pytest -v

```



Generate an HTML report:



```powershell

.\\.venv\\Scripts\\python.exe -m pytest -v --html=reports/report.html --self-contained-html

```



Generate a coverage report:



```powershell

.\\.venv\\Scripts\\python.exe -m pytest --cov=app --cov-report=term-missing

```



\## 9. Entry Criteria



\- Python is installed.

\- Project dependencies are installed.

\- The API application can be imported.

\- The automated test suite is available.



\## 10. Exit Criteria



\- All expected test scenarios have been executed.

\- Failed tests have been investigated.

\- Confirmed defects have been documented.

\- Test results and coverage have been reviewed.

\- The GitHub Actions workflow completes successfully.



\## 11. Risks and Limitations



\- The API stores tasks in memory, so data does not persist across application restarts.

\- These tests validate API behavior in a controlled test environment.

\- Passing automated tests does not guarantee that the application is free of all defects.

\- Performance, security, and production database behavior are not covered by this test plan.



\## 12. Test Results



Test results must be recorded after running the current version of the suite. Do not assume a test count or pass rate without verifying the latest execution output.



\*\*Latest execution date:\*\* To be recorded.



\*\*Tests passed:\*\* To be recorded.



\*\*Tests failed:\*\* To be recorded.



\*\*Code coverage:\*\* To be recorded.



\*\*CI/CD status:\*\* To be verified in GitHub Actions.



\## 13. Conclusion



This test plan documents the intended API testing scope, endpoints, positive and negative scenarios, expected responses, and execution process.



It supports a structured, repeatable approach to API quality assurance and demonstrates practical skills in Python, Pytest, REST API validation, test reporting, code coverage, and continuous integration.



