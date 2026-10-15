# Bug Report — Task Management API

## 1. Bug Summary

| Field | Details |
|---|---|
| Bug ID | API-BUG-001 |
| Title | API accepts task titles containing only whitespace |
| Severity | Medium |
| Priority | High |
| Status | Fixed; regression tests added |
| Component | Task creation and task input validation |
| Test type | REST API functional and regression testing |

## 2. Environment

- Application: Task Management API
- Framework: FastAPI
- Language: Python 3.11
- Validation: Pydantic
- Database: SQLAlchemy with SQLite
- Test framework: pytest

## 3. Preconditions

- The Task Management API is running.
- The task creation endpoint, `POST /tasks`, is accessible.

## 4. Steps to Reproduce

1. Send a POST request to `/tasks`.
2. Provide a task title containing only whitespace characters.
3. Inspect the HTTP response.
4. If the request is accepted, check whether the task was persisted.

### Example Request

```json
{
  "title": "   ",
  "description": "Whitespace validation test",
  "completed": false
}
```

## 5. Expected Result

- The API rejects the request with HTTP `422 Unprocessable Entity`.
- The response indicates that the title fails input validation.
- No task is created in the database.

## 6. Original Actual Result

During development testing, a whitespace-only task title was identified as an input-validation defect.

The original validation checked the title's length but did not ensure that the title contained at least one non-whitespace character.

**Evidence note:** The original response body and status code were not recorded in this report. Capture them from a reproducible test if you need to document the precise original response.

## 7. Root Cause

The original title validation did not distinguish between a string containing meaningful characters and one containing only whitespace.

For example, `"   "` contains characters but does not represent a meaningful task title.

## 8. Fix Implemented

A Pydantic field validator was added to reject titles when:

```python
value.strip()
```

returns an empty string.

This prevents whitespace-only titles from passing the title validation rule.

## 9. Regression Testing

The automated test suite includes coverage for:

- Empty task titles
- Whitespace-only task titles
- Titles exceeding the permitted maximum length
- Invalid task update payloads
- Preservation of existing task data after a rejected update
- Confirmation that a rejected create request does not create a task

These tests help verify that invalid titles are rejected and that rejected operations do not unintentionally alter task data.

## 10. Verification Results

The latest confirmed local pytest run reported **49 passed and 0 failed**.

This is a result for the complete test suite. It should not be interpreted as a separate pass count for this bug unless the individual regression tests are run and recorded independently.

## 11. QA Conclusion

The whitespace-validation defect was addressed by adding a Pydantic validation rule and regression tests. The change helps prevent tasks with meaningless titles from being accepted.

The report records the defect, expected behavior, root cause, fix, and verification approach. The original response details were not retained, so they should be captured in a reproducible test rather than reconstructed from memory.
