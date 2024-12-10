import allure
from playwright.sync_api import Page, Locator


class BasePage:
    """
    A base class providing reusable methods for Playwright page interactions.
    It serves as a parent class for other page objects to reduce duplication and
    streamline common UI actions like navigation, input, clicks, and screenshot capturing.

    Attributes:
        page (Page): The Playwright page object used for browser interaction.
    """

    def __init__(self, page: Page):
        """
        Initializes the BasePage class with a Playwright page instance.

        Args:
            page (Page): The Playwright page object to interact with the web page.
        """
        self.page = page

    def navigate(self, url: str):
        """
        Navigates to the specified URL.

        Args:
            url (str): The URL to navigate to.
        """
        self.page.goto(url)

    def fill_input(self, selector: str, value: str | int | float):
        """
        Fills an input field with the provided value.

        Args:
            selector (str): The CSS or XPath selector of the input field.
            value (str | int | float): The value to input into the field.

        Raises:
            Exception: If the input field cannot be located or filled.
        """
        try:
            input_field: Locator = self.page.locator(selector)
            input_field.fill(str(value), timeout=300)
        except Exception as e:
            self._attach_screenshot(f"Failed to fill input: {selector}")
            raise Exception(f"Error filling input field with selector '{selector}': {str(e)}")

    def click(self, selector: str):
        """
        Clicks on an element specified by the selector.

        Args:
            selector (str): The CSS or XPath selector of the element to click.

        Raises:
            Exception: If the element cannot be located or clicked.
        """
        try:
            self.page.click(selector)
        except Exception as e:
            self._attach_screenshot(f"Failed to click element: {selector}")
            raise Exception(f"Error clicking element with selector '{selector}': {str(e)}")

    def click_by_index(self, selector: str, index: int):
        """
        Clicks on an element at a specific index within a list of elements matching the selector.

        Args:
            selector (str): The CSS or XPath selector for the list of elements.
            index (int): The 0-based index of the element to click.

        Raises:
            Exception: If the element at the specified index cannot be located or clicked.
        """
        try:
            self.page.locator(selector).nth(index).click()
        except Exception as e:
            self._attach_screenshot(f"Failed to click element at index {index}: {selector}")
            raise Exception(f"Error clicking element with selector '{selector}' at index {index}: {str(e)}")

    def _attach_screenshot(self, name: str):
        """
        Helper method to attach screenshots to Allure reports for debugging purposes.

        Args:
            name (str): The name or description of the screenshot to be displayed in the report.

        Notes:
            Screenshots are taken at the point of failure and attached to the Allure report as PNG files.
        """
        try:
            screenshot_path = self.page.screenshot()
            allure.attach(screenshot_path, name=name, attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            raise Exception(f"Error capturing screenshot: {str(e)}")
