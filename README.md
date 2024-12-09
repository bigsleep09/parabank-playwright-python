# Automation Framework for Contact List App using Playwright and Python

## Tools and Technologies
- **Python**
- **Playwright**
- **Pytest**
- **Allure** for test reporting

## Test Scenarios
1. **User Registration**: Register a new user.
2. **User Login**: Log in using valid credentials.
3. **Account Actions**: Perform Create Read Update Delete (CRUD) actions using the User Interface and API

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repo_url>

2. Install dependencies 
   ```bash
   pip install -r requirements.txt
   playwright install
3. Run the tests
```bash
   pytest --alluredir=allure-results
