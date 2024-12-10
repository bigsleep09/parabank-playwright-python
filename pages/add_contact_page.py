from playwright.sync_api import Page, expect

from locators.contact_list_locators import AddContactPageLocators
from utils.base_page import BasePage


class AddContactPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def is_page_loaded(self):
        expected_url: str = "https://thinking-tester-contact-list.herokuapp.com/addContact"
        try:
            expect(self.page).to_have_url(expected_url)
        except AssertionError as e:
            self._attach_screenshot("Expected URL doesn't match with Actual")
            raise Exception(f"Error comparing URL. {str(e)}")

    def _input_first_name(self, first_name: str):
        try:

            self.fill_input(AddContactPageLocators.first_name_input, first_name)
        except Exception as e:

            self._attach_screenshot("Failed to insert first name")
            raise Exception(f"Error inserting first name {str(e)}")

    def _input_last_name(self, last_name: str):
        try:

            self.fill_input(AddContactPageLocators.last_name_input, last_name)
        except Exception as e:

            self._attach_screenshot("Failed to insert last name")
            raise Exception(f"Error inserting last name {str(e)}")

    def _input_birthdate(self, birthdate: str):
        try:

            self.fill_input(AddContactPageLocators.birthdate_input, birthdate)
        except Exception as e:

            self._attach_screenshot("Failed to insert birthdate")
            raise Exception(f"Error inserting birthdate {str(e)}")

    def _input_email(self, email: str):
        try:

            self.fill_input(AddContactPageLocators.email_input, email)
        except Exception as e:

            self._attach_screenshot("Failed to insert email")
            raise Exception(f"Error inserting email {str(e)}")

    def _input_phone(self, phone: str):
        try:

            self.fill_input(AddContactPageLocators.phone_input, phone)
        except Exception as e:

            self._attach_screenshot("Failed to insert phone")
            raise Exception(f"Error inserting phone {str(e)}")

    def _input_address_street_1(self, address_street_1: str):
        try:

            self.fill_input(AddContactPageLocators.address_street_1_input, address_street_1)
        except Exception as e:

            self._attach_screenshot("Failed to insert address_street_1")
            raise Exception(f"Error inserting address_street_1 {str(e)}")

    def _input_address_street_2(self, address_street_2: str):
        try:

            self.fill_input(AddContactPageLocators.address_street_2_input, address_street_2)
        except Exception as e:

            self._attach_screenshot("Failed to insert address_street_2")
            raise Exception(f"Error inserting address_street_2 {str(e)}")

    def _input_city(self, city: str):
        try:

            self.fill_input(AddContactPageLocators.city_input, city)
        except Exception as e:

            self._attach_screenshot("Failed to insert city")
            raise Exception(f"Error inserting city {str(e)}")

    def _input_state_province(self, state_province: str):
        try:

            self.fill_input(AddContactPageLocators.state_province_input, state_province)
        except Exception as e:

            self._attach_screenshot("Failed to insert state_province")
            raise Exception(f"Error inserting state_province {str(e)}")

    def _input_postal_code(self, postal_code: str):
        try:

            self.fill_input(AddContactPageLocators.postal_code_input, postal_code)
        except Exception as e:

            self._attach_screenshot("Failed to insert postal_code")
            raise Exception(f"Error inserting postal_code {str(e)}")

    def _input_country(self, country: str):
        try:

            self.fill_input(AddContactPageLocators.country_input, country)
        except Exception as e:

            self._attach_screenshot("Failed to insert country")
            raise Exception(f"Error inserting country {str(e)}")

    def _click_submit_button(self):
        try:
            self.click(AddContactPageLocators.submit_button)
        except Exception as e:
            self._attach_screenshot("Failed to click submit button")
            raise Exception(f"Error clicking submit button {str(e)}")

    def add_new_contact(self, first_name: str, last_name: str, email: str, phone: str | None, birthdate: str,
                        country: str | None,
                        city: str | None, address_street_1: str | None, address_street_2: str | None,
                        state_province: str | None, postal_code: str | None):
        try:
            self._input_first_name(first_name)
            self._input_last_name(last_name)
            self._input_birthdate(birthdate)
            self._input_email(email)
            self._input_phone(phone)
            self._input_address_street_1(address_street_1)
            self._input_address_street_2(address_street_2)
            self._input_city(city)
            self._input_state_province(state_province)
            self._input_postal_code(postal_code)
            self._input_country(country)
            self._click_submit_button()
        except Exception as e:
            self._attach_screenshot("Failed Adding New Contact")
            raise Exception(f"Error Adding New Contact {str(e)}")
