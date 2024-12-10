import pytest
from playwright.sync_api import Page

from pages.contacts_list_page import ContactListPage
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from utils.file_handler import get_json


@pytest.mark.user_interface
def test_registration(setup):
    """
    Test case for the user registration process.

    This test case simulates the process of registering a new user. It verifies that after registration,
    the user is logged in and can then log out successfully.

    Steps:
        1. Navigate to the home page.
        2. For each user in the provided registration data:
            - Click on the "Sign In" button to access the registration page.
            - Fill in the registration details and submit the form.
            - Verify that the user is redirected to the contact list page (i.e., logged in).
            - Logout from the application to verify the logout functionality.

    Args:
        setup (Page): The Playwright page instance provided by the test setup.

    Asserts:
        - After registration, the user is logged in and can logout successfully.
    """
    page: Page = setup
    home_page = HomePage(page)
    registration_credentials: list[dict[str, object]] = get_json("resources/registration_data.jsonc")
    for user in registration_credentials:
        # Navigate to the registration page
        registration_page: RegistrationPage = home_page.click_sign_in()
        registration_page.is_page_loaded()
        print(user)

        # Register the user and verify successful login
        contact_list_page: ContactListPage = registration_page.register_user(
            str(user.get("firstName")),
            str(user.get("lastName")),
            str(user.get("email")),
            str(user.get("password"))
        )
        contact_list_page.is_logged_in()

        # Log out the user to verify the logout functionality
        contact_list_page.logout()
