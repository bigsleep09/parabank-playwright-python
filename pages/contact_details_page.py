import allure
from playwright.sync_api import Page, expect

from locators.contact_list_locators import ContactDetailsPageLocators
from pages.edit_contact_page import EditContactPage
from utils.base_page import BasePage


class ContactDetailsPage(BasePage):
    """
    Represents the Contact Details Page in the application.

    Provides methods to interact with elements on the Contact Details Page, such as verifying
    the page is loaded, editing contact details, deleting a contact, and handling confirmation dialogs.

    Attributes:
        page (Page): The Playwright page instance for interacting with the browser.
    """

    def __init__(self, page: Page):
        """
        Initializes the ContactDetailsPage.

        Args:
            page (Page): The Playwright page instance.
        """
        super().__init__(page)

    @allure.step("Verify Contact Details Page is loaded")
    def is_page_loaded(self):
        """
        Validates that the Contact Details Page has successfully loaded by verifying the URL.

        Raises:
            AssertionError: If the current URL does not match the expected URL.
        """
        try:
            expect(self.page).to_have_url("https://thinking-tester-contact-list.herokuapp.com/contactDetails")
        except AssertionError as e:
            self._attach_screenshot("Page Load Failure")
            raise AssertionError(f"Contact Details Page did not load correctly: {str(e)}")

    @allure.step("Click 'Edit Contact' button")
    def click_edit_contact_button(self) -> EditContactPage:
        """
        Clicks the 'Edit Contact' button to navigate to the Edit Contact Page.

        Returns:
            EditContactPage: An instance of the EditContactPage class.

        Raises:
            Exception: If the click action fails.
        """
        try:
            self.click(ContactDetailsPageLocators.edit_contact_button)
            return EditContactPage(self.page)
        except Exception as e:
            self._attach_screenshot("Failed to click 'Edit Contact' button")
            raise Exception(f"Error clicking 'Edit Contact' button: {str(e)}")

    @allure.step("Click 'Delete Contact' button")
    def click_delete_contact_button(self):
        """
        Clicks the 'Delete Contact' button to initiate the delete action.

        Raises:
            Exception: If the click action fails.
        """
        try:
            self.click(ContactDetailsPageLocators.delete_contact_button)
        except Exception as e:
            self._attach_screenshot("Failed to click 'Delete Contact' button")
            raise Exception(f"Error clicking 'Delete Contact' button: {str(e)}")

    @allure.step("Confirm 'Delete Contact' in the dialog")
    def click_ok_in_dialog(self):
        """
        Handles the browser dialog that appears when confirming the delete action.

        Raises:
            Exception: If accepting the dialog or clicking the confirm button fails.
        """
        try:
            # Listen for the dialog and accept it when it appears.
            self.page.once("dialog", lambda dialog: dialog.accept())
            # Click the 'Delete Contact' button to trigger the dialog.
            self.page.get_by_role("button", name="Delete Contact").click()
        except Exception as e:
            self._attach_screenshot("Failed to confirm dialog")
            raise Exception(f"Error clicking confirm in dialog alert: {str(e)}")

    @allure.step("Delete contact")
    def delete_contact(self):
        """
        Deletes the contact by clicking the 'Delete Contact' button and confirming the action
        in the dialog.

        Steps:
            1. Click the 'Delete Contact' button.
            2. Confirm the action in the dialog.
            3. Wait for the action to complete.

        Raises:
            Exception: If any step in the delete process fails.
        """
        try:
            self.click_delete_contact_button()
            self.click_ok_in_dialog()
            self.page.wait_for_timeout(5000)  # Wait for the deletion process to complete
        except Exception as e:
            self._attach_screenshot("Failed to delete contact")
            raise Exception(f"Error deleting contact: {str(e)}")
