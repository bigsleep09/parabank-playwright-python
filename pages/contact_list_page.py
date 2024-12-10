import allure
import pytest
from playwright.sync_api import Page, expect

from utils.base_page import BasePage


class ContactListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    @allure.step("Verify user is logged in")
    def is_logged_in(self):
        try:
            expect(self.page).to_have_url("https://thinking-tester-contact-list.herokuapp.com/contactList")

        except AssertionError as e:
            pytest.fail(f"User is not logged in. {str(e)}")
