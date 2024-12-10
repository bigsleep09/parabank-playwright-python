from playwright.sync_api import Page

from locators.contact_list_locators import RegistrationPageLocators
from utils.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def _input_first_name(self, first_name: str):
        try:
            self.page.locator(RegistrationPageLocators.first_name_input).press_sequentially(first_name, timeout=200)
        except Exception as e:
            raise Exception(f"Error inputting first_name. {str(e)}")

    def _input_last_name(self, last_name: str):
        try:
            self.page.locator(RegistrationPageLocators.last_name_input).press_sequentially(last_name, timeout=200)
        except Exception as e:
            raise Exception(f"Error inputting last_name. {str(e)}")

    def _input_email(self, email: str):
        try:
            self.page.locator(RegistrationPageLocators.email_input).press_sequentially(email, timeout=200)
        except Exception as e:
            raise Exception(f"Error inputting email. {str(e)}")

    def _input_password(self, password: str):
        try:
            self.page.locator(RegistrationPageLocators.password_input).press_sequentially(password, timeout=200)
        except Exception as e:
            raise Exception(f"Error inputting password. {str(e)}")

    def register_user(self, first_name: str, last_name: str, email: str, password: str):
        try:
            self._input_first_name(first_name)
            self._input_last_name(last_name)
            self._input_email(email)
            self._input_password(password)
        except Exception as e:
            raise Exception
