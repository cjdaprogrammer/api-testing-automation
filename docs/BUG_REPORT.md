\# Bug Report — Task Management API



\## Bug ID

API-BUG-001



\## Title

API accepts a task title containing only whitespace



\## Severity

Medium — invalid task data could be accepted if input validation fails.



\## Priority

High — input validation should be corrected before release.



\## Status

Fixed — regression tests added.



\## Environment

\- Application: Task Management API

\- Framework: FastAPI

\- Language: Python 3.11

\- Test framework: Pytest

\- Test type: REST API functional testing



\## Preconditions

The API test client is available, and the task creation endpoint can be accessed.



\## Steps to Reproduce

1\. Send a POST request to `/tasks`.

2\. Submit a title containing only spaces.

3\. Observe the HTTP response.



Example request:



```json

{

&#x20; "title": "   ",

&#x20; "description": "Whitespace validation test",

&#x20; "completed": false

}

```



\## Expected Result

The API should reject the request with HTTP 422 because the title contains no meaningful text.



\## Actual Result

During testing, whitespace-only titles were identified as an input-validation defect. The application was updated to reject titles that contain only whitespace.



\## Root Cause

The original validation checked the title's length but did not ensure that the title contained a non-whitespace character.



\## Fix Implemented

A Pydantic field validator was added to reject titles when `value.strip()` is empty.



\## Regression Testing

The automated test suite includes checks for:

\- Empty titles

\- Whitespace-only titles

\- Titles exceeding the maximum length

\- Invalid task update payloads

\- Preservation of existing task data after a rejected update



\## Verification

The fix should be verified by running the current Pytest suite and confirming that all tests pass.



\## QA Conclusion

The validation defect was addressed, and regression tests help prevent the same issue from returning in future changes.



