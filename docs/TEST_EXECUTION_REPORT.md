
# Test Execution Report — Task Management API

## 1. Execution Summary

| Item | Result |
|---|---|
| Project | API Testing Automation |
| Application | Task Management API |
| Test Framework | Pytest |
| Programming Language | Python 3.11 |
| Pytest Result | 33 passed in the latest reported run |
| Failed Tests | 0 in that reported run |
| Statement Coverage | 100% in the previously reported coverage run |
| Postman Collection | 15 requests reported passing |
| CI/CD | GitHub Actions reported green |
| HTML Test Report | `reports/report.html` |
| Coverage Report | `reports/coverage/index.html` |
| Report Updated | October 14, 2026 |

**Evidence note:** The results above summarize previously reported project runs. Execute the current suite again to confirm the results against the latest repository state.

## 2. Test Objective

Validate API endpoint behavior, request validation, response data, error handling, and task data integrity through automated testing.

## 3. Execution Results

### Pytest

The latest reported suite contained 33 passing tests and no failures.

Coverage was previously reported at 100% statement coverage for `app/main.py`. Coverage results apply to the executed test suite and do not prove that every possible behavior or defect has been tested.

### Postman

The Postman collection was reported to contain 15 requests, with all checks passing in the latest reported run.

### Continuous Integration

GitHub Actions was reported green after the Postman collection execution was added to the workflow.

## 4. Areas Tested

- Root and health endpoints
- Task creation, retrieval, update, and deletion
- Required and invalid input handling
- Empty and whitespace-only titles
- Title length boundaries
- Description length boundaries
- Invalid field data types
- Empty request bodies
- Nonnumeric task IDs
- Nonexistent resources
- Response schema and data integrity
- Rejected update behavior
- Postman request assertions
- CI execution

## 5. Test Evidence

The project generates reports using pytest-html and pytest-cov.

- Pytest HTML report: `reports/report.html`
- Coverage HTML report: `reports/coverage/index.html`
- Postman collection: `postman/Task_Management_API.postman_collection.json`
- CI workflow: `.github/workflows/tests.yml`

The reports directory is generated during test execution and is not intended to be committed if it is excluded by `.gitignore`. GitHub Actions can retain generated reports as workflow artifacts.

## 6. Reproduction Commands

Run the full test suite and generate reports:

```powershell
.\.venv\Scripts\python.exe -m pytest -v --cov=app --cov-report=term-missing --cov-report=html:reports/coverage --html=reports/report.html --self-contained-html
```

Run the Postman collection against the running API:

```powershell
postman collection run .\postman\Task_Management_API.postman_collection.json --reporters cli
```

## 7. Limitations

- The application stores tasks in memory; data resets when the process restarts.
- Authentication and authorization are not implemented.
- Production database behavior, load testing, and penetration testing are outside the current scope.
- Successful automated checks do not guarantee the absence of all defects.

## 8. Conclusion

The previously reported results indicate successful execution of the Pytest suite, Postman checks, and GitHub Actions workflow.

Re-run the commands in this report before using these figures as evidence of the current version's results. Keep the report synchronized with actual test output after future changes.
