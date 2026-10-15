# Test Execution Report — Task Management API

## 1. Execution Summary

| Item | Result |
|---|---|
| Project | API Testing Automation |
| Application | Task Management API |
| Test framework | pytest |
| Language | Python 3.11 |
| Latest confirmed local result | 49 passed |
| Failed tests | 0 |
| Execution time | Approximately 5.63 seconds |
| Latest local warning | 1 deprecation warning |
| Previously reported statement coverage | 100% (87 of 87 statements) |
| Database | SQLAlchemy with SQLite |
| Postman collection | 15 requests and 25 assertions reported passing in an earlier run |
| CI status | Latest workflow reported green; see GitHub Actions for current status |

**Result status:** The latest confirmed local pytest run passed all 49 tests. The coverage and Postman figures above are historical results and should be refreshed before being described as results from the same execution.

## 2. Test Objective

Evaluate the Task Management API's functionality, input validation, response behavior, error handling, and data integrity through repeatable automated tests.

The test suite focuses on expected behavior, invalid inputs, boundary conditions, and database persistence.

## 3. Test Execution Results

### 3.1 Automated pytest tests

The latest confirmed local execution reported:

- Tests passed: 49
- Tests failed: 0
- Execution time: approximately 5.63 seconds
- Warnings: 1 deprecation warning

The suite covers CRUD operations, invalid requests, boundary values, response validation, database persistence, and database-session cleanup.

### 3.2 Code coverage

A previously recorded coverage run reported 100% statement coverage, covering 87 of 87 executable statements in the application code.

Statement coverage indicates which executable statements were exercised during a run. It does not prove that all possible behaviors, edge cases, or defects have been identified.

**Status:** Historical result; regenerate the coverage report to confirm the current figure.

### 3.3 Postman collection

An earlier collection execution reported 15 requests and 25 assertions passing with no failures.

**Status:** Historical result; rerun the collection against the current API before treating these figures as current.

### 3.4 Continuous integration

The GitHub Actions workflow is configured to install dependencies, run pytest with coverage, generate reports, start the API server, and execute the Postman collection.

The latest workflow was reported as green. Confirm the current run and its individual steps in the [GitHub Actions workflow history](https://github.com/cjdaprogrammer/api-testing-automation/actions).

## 4. Test Coverage Areas

The automated tests and supporting collection cover the following areas:

- Root and health endpoints
- Task creation, retrieval, update, and deletion
- Required-field validation and invalid inputs
- Empty and whitespace-only task titles
- Title and description length boundaries
- Invalid field data types and malformed JSON
- Missing and null fields
- Nonpositive, nonnumeric, and nonexistent task IDs
- Response structure and data integrity
- Rejected updates preserving existing task data
- Database session creation and cleanup
- Task persistence across separate database sessions
- Postman request assertions
- Automated CI workflow execution

## 5. Test Evidence

| Evidence | Location |
|---|---|
| Pytest HTML report | `reports/report.html` |
| Coverage HTML report | `reports/coverage/index.html` or `htmlcov/index.html`, depending on the command |
| Postman collection | `postman/Task_Management_API.postman_collection.json` |
| GitHub Actions workflow | `.github/workflows/tests.yml` |
| Test plan | `docs/TEST_PLAN.md` |
| Bug report | `docs/BUG_REPORT.md` |

Generated reports are excluded from normal Git tracking. The CI workflow is configured to upload selected reports as workflow artifacts.

## 6. Reproduction Commands

Run the automated tests and generate coverage and HTML reports from PowerShell:

```powershell
New-Item -ItemType Directory -Force reports | Out-Null

python -m pytest tests -v `
  --cov=app `
  --cov-report=term-missing `
  --cov-report=html:reports/coverage `
  --html=reports/report.html `
  --self-contained-html
```

The expected output files are:

- `reports/report.html`
- `reports/coverage/index.html`

To execute the Postman collection, first ensure the API server is running and Postman CLI is installed:

```powershell
postman collection run .\postman\Task_Management_API.postman_collection.json
```

Review the command output to confirm the request and assertion results for that run.

## 7. Limitations

- SQLite is used for persistence. Production database deployment and migration behavior are outside the current scope.
- Authentication and authorization are not implemented.
- The documented results do not establish load, stress, or comprehensive security testing.
- Passing tests and high statement coverage do not guarantee that the application is defect-free.
- The deprecation warning from the latest confirmed local run should be investigated for compatibility with the installed dependencies.

## 8. Conclusion

The latest confirmed local pytest execution passed all 49 collected tests with no failures. Earlier recorded results also showed 100% statement coverage and a successful Postman collection run.

These results demonstrate practical work in API regression testing, input validation, boundary-value analysis, database testing, and automated reporting.

For an up-to-date assessment, rerun pytest with coverage, execute the Postman collection, and inspect the latest GitHub Actions run. Record the date, results, and any warnings from each execution so the evidence remains traceable.

