import allure
import pytest
from playwright.sync_api import Page, expect

from locators.contact_list_locators import ContactListPageLocators
from pages.add_contact_page import AddContactPage
from pages.contact_details_page import ContactDetailsPage
from utils.base_page import BasePage


class ContactListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    @allure.step("Verify user is logged in")
    def is_logged_in(self):
        """
        Checks if the user is on the Contact List page by verifying the URL.
        """
        try:
            expect(self.page).to_have_url("https://thinking-tester-contact-list.herokuapp.com/contactList")
        except AssertionError as e:
            pytest.fail(f"User is not logged in. {str(e)}")

    @allure.step("Click 'Add New Contact' button")
    def click_add_new_contact(self) -> AddContactPage:
        """
        Clicks the 'Add New Contact' button and navigates to the Add Contact page.
        """
        try:
            self.click(ContactListPageLocators.add_new_contact_button)
            return AddContactPage(self.page)
        except Exception as e:
            self._attach_screenshot("Failed to click add new contact button")
            raise Exception(f"Error clicking 'Add New Contact' button. {str(e)}")

    @allure.step("Select contact by index: {index}")
    def select_contact_by_index(self, index):
        """
        Selects a contact from the contact list by its index and navigates to the Contact Details page.

        :param index: Index of the contact to select (0-based)
        """
        try:
            self.click_by_index(ContactListPageLocators.contacts_table, index)
            return ContactDetailsPage(self.page)
        except Exception as e:
            self._attach_screenshot(f"Failed to select contact at index {index}")
            raise Exception(f"Error clicking contact with index {index}\n{str(e)}")

    def logout(self):
        """
        Click "Logout" button and return to home page
        """
        try:
            self.click(ContactListPageLocators.logout_button)

        except Exception as e:
            self._attach_screenshot(f"Failed to logout")
            raise Exception(f"Error loggin out\n{str(e)}")
