import allure
from playwright.sync_api import Page, expect

from locators.contact_list_locators import AddContactPageLocators
from utils.base_page import BasePage


class AddContactPage(BasePage):
    """
    Represents the Add Contact Page in the application.

    Provides methods for interacting with the page, such as verifying if the page is loaded,
    filling out contact details, and submitting the form. Includes Allure steps for detailed
    test reporting.

    Attributes:
        page (Page): The Playwright page instance for interacting with the browser.
    """

    def __init__(self, page: Page):
        """
        Initializes the AddContactPage class.

        Args:
            page (Page): The Playwright page instance.
        """
        super().__init__(page)

    @allure.step("Verify Add Contact page is loaded")
    def is_page_loaded(self):
        """
        Verifies that the Add Contact page is loaded by checking the current URL.

        Raises:
            Exception: If the current URL does not match the expected URL.
        """
        expected_url: str = "https://thinking-tester-contact-list.herokuapp.com/addContact"
        try:
            expect(self.page).to_have_url(expected_url)
        except AssertionError as e:
            self._attach_screenshot("Expected URL doesn't match with Actual")
            raise Exception(f"Error comparing URL. {str(e)}")

    @allure.step("Enter first name: {first_name}")
    def _input_first_name(self, first_name: str):
        """
        Inputs the first name into the corresponding field.

        Args:
            first_name (str): The first name to input.

        Raises:
            Exception: If the input action fails.
        """
        try:
            self.fill_input(AddContactPageLocators.first_name_input, first_name)
        except Exception as e:
            self._attach_screenshot("Failed to insert first name")
            raise Exception(f"Error inserting first name {str(e)}")

    @allure.step("Enter last name: {last_name}")
    def _input_last_name(self, last_name: str):
        """
        Inputs the last name into the corresponding field.

        Args:
            last_name (str): The last name to input.

        Raises:
            Exception: If the input action fails.
        """
        try:
            self.fill_input(AddContactPageLocators.last_name_input, last_name)
        except Exception as e:
            self._attach_screenshot("Failed to insert last name")
            raise Exception(f"Error inserting last name {str(e)}")

    @allure.step("Enter birthdate: {birthdate}")
    def _input_birthdate(self, birthdate: str):
        """
        Inputs the birthdate into the corresponding field.

        Args:
            birthdate (str): The birthdate to input.

        Raises:
            Exception: If the input action fails.
        """
        try:
            self.fill_input(AddContactPageLocators.birthdate_input, birthdate)
        except Exception as e:
            self._attach_screenshot("Failed to insert birthdate")
            raise Exception(f"Error inserting birthdate {str(e)}")

    @allure.step("Enter email: {email}")
    def _input_email(self, email: str):
        """
        Inputs the email into the corresponding field.

        Args:
            email (str): The email to input.

        Raises:
            Exception: If the input action fails.
        """
        try:
            self.fill_input(AddContactPageLocators.email_input, email)
        except Exception as e:
            self._attach_screenshot("Failed to insert email")
            raise Exception(f"Error inserting email {str(e)}")

    @allure.step("Enter phone number: {phone}")
    def _input_phone(self, phone: str):
        """
        Inputs the phone number into the corresponding field.

        Args:
            phone (str): The phone number to input.

        Raises:
            Exception: If the input action fails.
        """
        try:
            self.fill_input(AddContactPageLocators.phone_input, phone)
        except Exception as e:
            self._attach_screenshot("Failed to insert phone")
            raise Exception(f"Error inserting phone {str(e)}")

    @allure.step("Enter address line 1: {address_street_1}")
    def _input_address_street_1(self, address_street_1: str):
        """
        Inputs the address line 1 into the corresponding field.

        Args:
            address_street_1 (str): The address line 1 to input.

        Raises:
            Exception: If the input action fails.
        """
        try:
            self.fill_input(AddContactPageLocators.address_street_1_input, address_street_1)
        except Exception as e:
            self._attach_screenshot("Failed to insert address_street_1")
            raise Exception(f"Error inserting address_street_1 {str(e)}")

    @allure.step("Enter address line 2: {address_street_2}")
    def _input_address_street_2(self, address_street_2: str):
        """
        Inputs the address line 2 into the corresponding field.

        Args:
            address_street_2 (str): The address line 2 to input.

        Raises:
            Exception: If the input action fails.
        """
        try:
            self.fill_input(AddContactPageLocators.address_street_2_input, address_street_2)
        except Exception as e:
            self._attach_screenshot("Failed to insert address_street_2")
            raise Exception(f"Error inserting address_street_2 {str(e)}")

    @allure.step("Enter city: {city}")
    def _input_city(self, city: str):
        """
        Inputs the city into the corresponding field.

        Args:
            city (str): The city to input.

        Raises:
            Exception: If the input action fails.
        """
        try:
            self.fill_input(AddContactPageLocators.city_input, city)
        except Exception as e:
            self._attach_screenshot("Failed to insert city")
            raise Exception(f"Error inserting city {str(e)}")

    @allure.step("Enter state/province: {state_province}")
    def _input_state_province(self, state_province: str):
        """
        Inputs the state or province into the corresponding field.

        Args:
            state_province (str): The state or province to input.

        Raises:
            Exception: If the input action fails.
        """
        try:
            self.fill_input(AddContactPageLocators.state_province_input, state_province)
        except Exception as e:
            self._attach_screenshot("Failed to insert state_province")
            raise Exception(f"Error inserting state_province {str(e)}")

    @allure.step("Enter postal code: {postal_code}")
    def _input_postal_code(self, postal_code: str):
        """
        Inputs the postal code into the corresponding field.

        Args:
            postal_code (str): The postal code to input.

        Raises:
            Exception: If the input action fails.
        """
        try:
            self.fill_input(AddContactPageLocators.postal_code_input, postal_code)
        except Exception as e:
            self._attach_screenshot("Failed to insert postal_code")
            raise Exception(f"Error inserting postal_code {str(e)}")

    @allure.step("Enter country: {country}")
    def _input_country(self, country: str):
        """
        Inputs the country into the corresponding field.

        Args:
            country (str): The country to input.

        Raises:
            Exception: If the input action fails.
        """
        try:
            self.fill_input(AddContactPageLocators.country_input, country)
        except Exception as e:
            self._attach_screenshot("Failed to insert country")
            raise Exception(f"Error inserting country {str(e)}")

    @allure.step("Click Submit button")
    def _click_submit_button(self):
        """
        Clicks the Submit button to add the contact.

        Raises:
            Exception: If the click action fails.
        """
        try:
            self.click(AddContactPageLocators.submit_button)
        except Exception as e:
            self._attach_screenshot("Failed to click submit button")
            raise Exception(f"Error clicking submit button {str(e)}")

    @allure.step("Add a new contact with provided details")
    def add_new_contact(self, first_name: str, last_name: str, email: str, phone: str | None, birthdate: str,
                        country: str | None, city: str | None, address_street_1: str | None,
                        address_street_2: str | None, state_province: str | None, postal_code: str | None):
        """
        Fills in the form to add a new contact and submits it.

        Args:
            first_name (str): The first name of the contact.
            last_name (str): The last name of the contact.
            email (str): The email address of the contact.
            phone (str | None): The phone number of the contact.
            birthdate (str): The birthdate of the contact.
            country (str | None): The country of the contact.
            city (str | None): The city of the contact.
            address_street_1 (str | None): Address line 1 of the contact.
            address_street_2 (str | None): Address line 2 of the contact.
            state_province (str | None): The state or province of the contact.
            postal_code (str | None): The postal code of the contact.

        Raises:
            Exception: If any input or submit action fails.
        """
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
