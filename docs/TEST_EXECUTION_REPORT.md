# Test Execution Report — Task Management API

## 1. Execution Summary

| Item | Result |
|---|---|
| Project | API Testing Automation |
| Application | Task Management API |
| Framework | Pytest |
| Language | Python 3.11 |
| Latest confirmed local test run | 49 passed |
| Failed tests | 0 |
| Warnings | 1 deprecation warning |
| Previously reported statement coverage | 100% |
| Database | SQLAlchemy with SQLite |
| Postman collection | 15 requests reported passing in an earlier run |
| GitHub Actions | Previously reported green; current workflow requires re-verification |
| HTML test report | `reports/report.html` |
| Coverage report | `htmlcov/index.html` or `reports/coverage/index.html`, depending on the command used |

**Execution note:** The latest local run completed with 49 passing tests in 5.63 seconds and one warning. Coverage and Postman results are from earlier reported runs and should be regenerated or rerun before being presented as current results.

## 2. Test Objective

Validate API endpoint behavior, request validation, response data, error handling, and task data integrity through automated tests.

## 3. Test Results

### Pytest

The latest confirmed local test execution reported 49 passed and no failed tests.

The test suite covers normal API operations, invalid requests, boundary values, database-session handling, and persistence behavior across database sessions.

### Code Coverage

A previous coverage run reported 100% statement coverage for the application code.

Statement coverage measures which executable statements ran during testing. It does not prove that every possible behavior is correct or that the application is defect-free.

### Postman

An earlier Postman collection run reported 15 requests and 25 assertions with no failures. Rerun the collection against the current API before treating these figures as current.

### Continuous Integration

The GitHub Actions workflow is configured to run pytest with coverage and execute the Postman collection. Verify the latest workflow run in GitHub before reporting its current status.

## 4. Areas Tested

- Root and health endpoints
- Task creation, retrieval, update, and deletion
- Required-field and invalid-input validation
- Empty and whitespace-only titles
- Title and description length boundaries
- Invalid field data types and malformed JSON
- Missing and null fields
- Nonpositive, nonnumeric, and nonexistent task IDs
- Response schema and data integrity
- Rejected updates preserving existing task data
- Database session creation and cleanup
- Task persistence across separate database sessions
- Postman request assertions
- Automated CI configuration

## 5. Test Evidence

- Pytest HTML report: `reports/report.html`
- Coverage HTML report: `htmlcov/index.html` or `reports/coverage/index.html`
- Postman collection: `postman/Task_Management_API.postman_collection.json`
- CI workflow: `.github/workflows/tests.yml`

Generated reports are excluded from normal Git tracking. GitHub Actions is configured to upload selected reports as workflow artifacts.

## 6. Reproduction Commands

Run the test suite with coverage and generate the HTML report:

```powershell
New-Item -ItemType Directory -Force reports | Out-Null
python -m pytest -v --cov=app --cov-report=term-missing --cov-report=html:reports/coverage --html=reports/report.html --self-contained-html
```

Run the Postman collection against the running API:

```powershell
postman collection run .\postman\Task_Management_API.postman_collection.json --reporters cli
```

## 7. Limitations

- SQLite is used for persistence; production database deployment and migration behavior are outside the current scope.
- Authentication and authorization are not implemented.
- Load, stress, and penetration testing have not been established by the results documented here.
- Automated tests and code coverage do not guarantee the absence of defects.
- The deprecation warning from the latest local run should be investigated for compatibility with the installed test dependencies.

## 8. Conclusion

The current local test run confirms that all 49 collected tests passed. Earlier results also documented full statement coverage and successful Postman checks.

Re-run the test suite, refresh coverage evidence, execute the Postman collection, and verify the latest GitHub Actions run before publishing updated execution metrics.
