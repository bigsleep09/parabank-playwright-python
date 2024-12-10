import allure
from playwright.sync_api import Page, expect

from locators.contact_list_locators import RegistrationPageLocators
from pages.contacts_list_page import ContactListPage
from utils.base_page import BasePage


class RegistrationPage(BasePage):
    """
    Represents the Registration Page of the application.

    Provides methods for interacting with the elements on the Registration Page,
    such as inputting user information and registering a new user.

    Attributes:
        page (Page): The Playwright page instance for interacting with the browser.
    """

    def __init__(self, page: Page):
        """
        Initializes the RegistrationPage.

        Args:
            page (Page): The Playwright page instance.
        """
        super().__init__(page)

    def is_page_loaded(self):
        """
        Verifies that the Registration Page is loaded by checking the current URL.

        Raises:
            AssertionError: If the current URL does not match the expected URL.
        """
        expect(self.page).to_have_url("https://thinking-tester-contact-list.herokuapp.com/addUser")

    @allure.step("Input first name: {first_name}")
    def _input_first_name(self, first_name: str):
        """
        Inputs the provided first name into the first name input field.

        Args:
            first_name (str): The first name to be entered.

        Raises:
            Exception: If the input operation fails.
        """
        try:
            self.page.locator(RegistrationPageLocators.first_name_input).press_sequentially(first_name, timeout=200)
        except Exception as e:
            self._attach_screenshot("Failed to insert first name")
            raise Exception(f"Error inputting first name: {str(e)}")

    @allure.step("Input last name: {last_name}")
    def _input_last_name(self, last_name: str):
        """
        Inputs the provided last name into the last name input field.

        Args:
            last_name (str): The last name to be entered.

        Raises:
            Exception: If the input operation fails.
        """
        try:
            self.page.locator(RegistrationPageLocators.last_name_input).press_sequentially(last_name, timeout=200)
        except Exception as e:
            self._attach_screenshot("Failed to insert last name")
            raise Exception(f"Error inputting last name: {str(e)}")

    @allure.step("Input email: {email}")
    def _input_email(self, email: str):
        """
        Inputs the provided email into the email input field.

        Args:
            email (str): The email to be entered.

        Raises:
            Exception: If the input operation fails.
        """
        try:
            self.page.locator(RegistrationPageLocators.email_input).press_sequentially(email, timeout=200)
        except Exception as e:
            self._attach_screenshot("Failed to insert email")
            raise Exception(f"Error inputting email: {str(e)}")

    @allure.step("Input password")
    def _input_password(self, password: str):
        """
        Inputs the provided password into the password input field.

        Args:
            password (str): The password to be entered.

        Raises:
            Exception: If the input operation fails.
        """
        try:
            self.page.locator(RegistrationPageLocators.password_input).press_sequentially(password, timeout=200)
        except Exception as e:
            self._attach_screenshot("Failed to insert password")
            raise Exception(f"Error inputting password: {str(e)}")

    @allure.step("Register user with provided details")
    def register_user(self, first_name: str, last_name: str, email: str, password: str):
        """
        Registers a new user with the provided details and navigates to the Contact List Page.

        Args:
            first_name (str): The first name of the user.
            last_name (str): The last name of the user.
            email (str): The email of the user.
            password (str): The password for the user account.

        Returns:
            ContactListPage: The Contact List Page object.

        Raises:
            Exception: If the registration process fails.
        """
        try:
            self._input_first_name(first_name)
            self._input_last_name(last_name)
            self._input_email(email)
            self._input_password(password)
            self.click(RegistrationPageLocators.submit_button)
            return ContactListPage(self.page)
        except Exception as e:
            self._attach_screenshot("Failed to register user")
            raise Exception(f"Error registering user: {str(e)}")
