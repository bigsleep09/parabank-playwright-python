import allure
import pytest

from pages.contacts_list_page import ContactListPage
from pages.home_page import HomePage
from utils.file_handler import get_json


@allure.title("Login with valid credentials")
@allure.description("Test to perform login scenario with valid credentials.")
@pytest.mark.parametrize("login_credentials", get_json("resources/login_data.jsonc"))
@pytest.mark.user_interface
def test_login_with_valid_credentials(setup, login_credentials: dict[str, object]):
    """
    Test case to validate the login functionality with valid credentials.

    This test case simulates the process of logging into the application with valid user credentials.
    It verifies that after login, the user is successfully redirected to the contact list page.

    Steps:
        1. Login with the provided valid credentials (email and password).
        2. Verify successful login by checking if the user is redirected to the contact list page.
        3. Confirm the login by asserting that the contact list page is displayed.

    Args:
        setup (Page): The Playwright page instance from the test setup.
        login_credentials (dict): Credentials (email and password) used to log into the application.

    Asserts:
        - The user is successfully logged in and redirected to the contact list page.
    """
    page = setup
    home_page: HomePage = HomePage(page)
    contact_list_page: ContactListPage = home_page.login_with_credential(str(login_credentials.get('email')),
                                                                         str(login_credentials.get('password')))
    contact_list_page.is_logged_in()
