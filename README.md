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

## Project Structure

```
├── contact-list-playwright-python
│   ├── locators
│   │   └── contact_list_locators.py
│   ├── pages
│   │   ├── contact_details_page.py
│   │   ├── contacts_list_page.py
│   │   ├── home_page.py
│   │   └── registration_page.py
│   ├── resources
│   │   ├── login_data.jsonc
│   │   └── registration_data.jsonc
│   ├── tests
│   │   ├── test_add_contact.py
│   │   ├── test_api_contact_list.py
│   │   ├── test_login.py
│   │   ├── test_registration.py
│   │   └── test_edit_contact.py
│   ├── utils
│   │   ├── api.py
│   │   ├── base_page.py
│   │   ├── file_handler.py
│   ├── .gitignore
│   ├── README.md
│   ├── conftest.py
│   ├── pytest.ini
│   └── requirements.txt
````

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/bigsleep09/parabank-playwright-python.git
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   playwright install
   ```
3. Run the tests

| Test Type           | Command                        | Description                                             | File/s                                                                               |
|---------------------|--------------------------------|---------------------------------------------------------|--------------------------------------------------------------------------------------|
| API                 | ```pytest -m api```            | Run all API tests related to Contact List App.          | ```test_api_contact_list.py```                                                       |
| User Interface Cell | ```pytest -m user_interface``` | Run all User interface test related to Contact list App | ```test_add_contact.py, test_edit_contact.py, test_login.py, test_registration.py``` |

4. Open Report

```bash
allure serve allure-results
```

## Test Coverage

### API Tests (test.api_contact_list.py)

- test_register_user
- test_register_user_with_existing_email
- test_login_user
- test_login_user_with_incorrect_credentials
- test_add_contact
- test_add_contact_with_invalid_email
- test_get_contact
- test_update_contact
- test_update_contact_with_invalid_id
- test_delete_contact
- test_delete_contact_with_invalid_id

### User Interface Tests

#### test_add_contact.py

-

#### test_login.py

-

#### test_registration.py

-

#### test_update_contact.py


