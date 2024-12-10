import allure
from playwright.sync_api import Page, Locator


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def fill_input(self, selector: str, value: str | int | float):
        input_field: Locator = self.page.locator(selector)
        input_field.press_sequentially(value, timeout=300)

    def click(self, selector: str):
        self.page.click(selector)

    def _attach_screenshot(self, name: str):
        """Helper method to attach screenshots to Allure reports."""
        screenshot_path = self.page.screenshot()
        allure.attach(screenshot_path, name=name, attachment_type=allure.attachment_type.PNG)
