import allure
from playwright.sync_api import Page

from locators.contact_list_locators import HomePageLocators
from pages.contacts_list_page import ContactListPage
from pages.registration_page import RegistrationPage
from utils.base_page import BasePage


class HomePage(BasePage):
    """
    Represents the Home Page of the application.

    Provides methods to interact with the Home Page elements, such as logging in with credentials,
    and navigating to the Registration page.

    Attributes:
        page (Page): The Playwright page instance for interacting with the browser.
    """

    def __init__(self, page: Page):
        """
        Initializes the HomePage.

        Args:
            page (Page): The Playwright page instance.
        """
        super().__init__(page)

    @allure.step("Input email: {email}")
    def _input_email(self, email: str):
        """
        Inputs the provided email into the email input field on the Home Page.

        Args:
            email (str): The email to be entered.

        Raises:
            Exception: If the input operation fails.
        """
        try:
            self.fill_input(HomePageLocators.email_input, email)
        except Exception as e:
            self._attach_screenshot("Failed to input email")
            raise Exception(f"Error inputting email: {email}. {str(e)}")

    @allure.step("Input password")
    def _input_password(self, password: str):
        """
        Inputs the provided password into the password input field on the Home Page.

        Args:
            password (str): The password to be entered.

        Raises:
            Exception: If the input operation fails.
        """
        try:
            self.fill_input(HomePageLocators.password_input, password)
        except Exception as e:
            self._attach_screenshot("Failed to input password")
            raise Exception(f"Error inputting password. {str(e)}")

    @allure.step("Click on submit button")
    def _click_submit(self):
        """
        Clicks the submit button on the Home Page.

        Raises:
            Exception: If the click operation fails.
        """
        try:
            self.click(HomePageLocators.submit_button)
        except Exception as e:
            self._attach_screenshot("Failed to click submit button")
            raise Exception(f"Error clicking submit button. {str(e)}")

    @allure.step("Login with credentials: email={email}, password={password}")
    def login_with_credential(self, email: str, password: str) -> ContactListPage:
        """
        Logs in using the provided email and password, then navigates to the Contact List Page.

        Args:
            email (str): The email to be used for login.
            password (str): The password to be used for login.

        Returns:
            ContactListPage: The Contact List Page object.

        Raises:
            Exception: If the login process fails.
        """
        try:
            self._input_email(email)
            self._input_password(password)
            self._click_submit()
            return ContactListPage(self.page)
        except Exception as e:
            self._attach_screenshot("Failed to Login")
            raise Exception(f"Login failed for email: {email}. {str(e)}")

    def click_sign_in(self):
        """
        Clicks the Sign In button, navigating to the Registration Page.

        Returns:
            RegistrationPage: The Registration Page object.

        Raises:
            Exception: If the click operation fails.
        """
        try:
            self.click(HomePageLocators.sign_in_button)
            return RegistrationPage(self.page)
        except Exception as e:
            self._attach_screenshot("Failed to click sign in button")
            raise Exception(f"Error clicking sign in button. {str(e)}")
