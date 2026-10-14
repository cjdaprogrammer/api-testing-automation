\# API Testing Automation Framework



A Python-based API testing project built to demonstrate software testing fundamentals, automated test execution, API validation, and continuous integration using GitHub Actions.



\## Project Overview



This project contains a Task Management API built with FastAPI and an automated test suite using pytest and HTTPX. It validates API behavior, response status codes, response data, input validation, and error handling.



The project is designed as a Junior QA Engineer portfolio project.



\## Tech Stack



\- \*\*Python 3.11\*\* — programming language

\- \*\*FastAPI\*\* — API framework

\- \*\*pytest\*\* — automated testing framework

\- \*\*HTTPX\*\* — HTTP client and API test support

\- \*\*pytest-html\*\* — HTML test reports

\- \*\*Git and GitHub\*\* — version control and source code hosting

\- \*\*GitHub Actions\*\* — continuous integration (CI)



\## Project Structure



```text

api-testing-automation/

├── .github/

│   └── workflows/

│       └── tests.yml

├── app/

│   ├── \_\_init\_\_.py

│   └── main.py

├── tests/

│   ├── \_\_init\_\_.py

│   └── test\_tasks\_api.py

├── reports/

├── .gitignore

├── pytest.ini

├── requirements.txt

└── README.md

```



\## Test Coverage



The automated test suite covers:



\- API root endpoint and health check

\- Creating tasks

\- Retrieving tasks and listing all tasks

\- Handling nonexistent task IDs

\- Required title validation

\- Empty and overlong title validation

\- Invalid data types

\- Updating existing tasks

\- Handling updates to nonexistent tasks

\- Deleting tasks

\- Handling deletion of nonexistent tasks

\- Task ID increment behavior

\- Empty task list behavior



\## Getting Started



\### 1. Clone the repository



```bash

git clone https://github.com/cjdaprogrammer/api-testing-automation.git

cd api-testing-automation

```



\### 2. Create a virtual environment



```bash

python -m venv .venv

```



Activate it on Windows PowerShell:



```powershell

.\\.venv\\Scripts\\Activate.ps1

```



If PowerShell blocks activation, run:



```powershell

Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned

.\\.venv\\Scripts\\Activate.ps1

```



\### 3. Install dependencies



```bash

python -m pip install -r requirements.txt

```



\### 4. Run the automated tests



```bash

python -m pytest -v

```



\### 5. Generate an HTML test report



```bash

python -m pytest -v --html=reports/report.html --self-contained-html

```



Open the generated report on Windows:



```powershell

Start-Process reports/report.html

```



\## Run the API Locally



Start the FastAPI development server:



```bash

uvicorn app.main:app --reload

```



Open the interactive API documentation:



\- API documentation: http://127.0.0.1:8000/docs

\- API root: http://127.0.0.1:8000/



Stop the server with `Ctrl + C`.



\## Continuous Integration



GitHub Actions automatically runs the test suite when changes are pushed to the configured branches or when a pull request is opened. The workflow also generates an HTML report and uploads it as an artifact.



The workflow currently passes in GitHub Actions.



\## Quality Assurance Skills Demonstrated



\- API functional testing

\- Positive and negative test scenarios

\- Input validation testing

\- HTTP status code verification

\- Error handling validation

\- Automated regression testing

\- Test reporting

\- Continuous integration

\- Git and GitHub workflow



\## Future Improvements



\- Add authentication and authorization test scenarios

\- Add parameterized tests and reusable test fixtures

\- Add API schema and response structure validation

\- Add test coverage reporting

\- Add environment-based configuration

\- Expand test coverage for edge cases



\## Author



\*\*Junior QA Engineer Portfolio Project\*\*



GitHub: https://github.com/cjdaprogrammer

