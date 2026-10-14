
# Bug Report — Task Management API

## Bug ID

API-BUG-001

## Title

API accepted a task title containing only whitespace

## Severity

Medium — accepting a title without meaningful content can result in invalid task data.

## Priority

High — required-field validation should be reliable before release.

## Status

Fixed — validation was implemented and regression tests were added.

## Environment

- Application: Task Management API
- Framework: FastAPI
- Language: Python 3.11
- Validation: Pydantic
- Test framework: Pytest
- Test type: REST API functional and regression testing

## Preconditions

The task creation endpoint is available and can receive JSON requests.

## Steps to Reproduce

1. Send a POST request to `/tasks`.
2. Submit a title containing only spaces.
3. Inspect the HTTP response.

### Example Request

```json
{
  "title": "   ",
  "description": "Whitespace validation test",
  "completed": false
}
```

## Expected Result

The API rejects the request with HTTP 422 because the title contains no meaningful text.

## Original Actual Result

During development testing, whitespace-only titles were identified as an input-validation defect.

## Root Cause

The original validation checked the title's length but did not ensure that the title contained a non-whitespace character.

## Fix Implemented

A Pydantic field validator was added to reject a title when `value.strip()` is empty.

The validator prevents titles containing only spaces or other surrounding whitespace from being accepted.

## Regression Testing

The automated suite includes checks for:

- Empty titles
- Whitespace-only titles
- Titles exceeding the maximum permitted length
- Invalid task update payloads
- Preservation of existing task data after a rejected update

## Verification

The reported automated test suite has passed after the validation changes. Re-run the suite when modifying this behavior to verify that the defect remains fixed.

## QA Conclusion

The validation defect was addressed in the application, and regression tests help prevent it from returning. This report documents the original issue and its implemented fix.
