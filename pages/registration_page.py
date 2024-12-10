from playwright.sync_api import Page

from utils.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def _input_first_name(self,first_name:str):
        try:
            self.page.locator(HomePageLocators.password_input).press_sequentially(password, timeout=200)
        except Exception as e:
            raise Exception(f"Error inputting password. {str(e)}")

    def _input_last_name(self,last_name:str):
        try:
            self.page.locator(HomePageLocators.password_input).press_sequentially(password, timeout=200)
        except Exception as e:
            raise Exception(f"Error inputting password. {str(e)}")

    def _input_email(self,email:str):
        try:
            self.page.locator(HomePageLocators.password_input).press_sequentially(password, timeout=200)
        except Exception as e:
            raise Exception(f"Error inputting password. {str(e)}")

    def _input_password(self,password:str):
        try:
            self.page.locator(HomePageLocators.password_input).press_sequentially(password, timeout=200)
        except Exception as e:
            raise Exception(f"Error inputting password. {str(e)}")
