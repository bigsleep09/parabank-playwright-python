import allure
from playwright.sync_api import expect, Page

from locators.contact_list_locators import EditContactPageLocators
from utils.base_page import BasePage


class EditContactPage(BasePage):
    """
    Represents the Edit Contact Page in the application.

    Provides methods to interact with the Edit Contact Page elements, such as filling out the form,
    submitting the form, and handling various input fields for updating contact details.

    Attributes:
        page (Page): The Playwright page instance for interacting with the browser.
    """

    def __init__(self, page: Page):
        """
        Initializes the EditContactPage.

        Args:
            page (Page): The Playwright page instance.
        """
        super().__init__(page)

    @allure.step("Verify Edit Contact page is loaded")
    def is_page_loaded(self):
        """
        Verifies that the Edit Contact Page has successfully loaded by checking the URL.

        Raises:
            AssertionError: If the current URL does not match the expected URL.
        """
        try:
            expect(self.page).to_have_url("https://thinking-tester-contact-list.herokuapp.com/editContact")
        except AssertionError as e:
            self._attach_screenshot("Page Load Failure")
            raise AssertionError(f"Edit Contact Page did not load correctly: {str(e)}")

    @allure.step("Enter first name: {first_name}")
    def _input_first_name(self, first_name: str):
        """
        Enters the first name into the first name input field.

        Args:
            first_name (str): The first name to be entered.

        Raises:
            Exception: If the input operation fails.
        """
        try:
            self.fill_input(EditContactPageLocators.first_name_input, first_name)
        except Exception as e:
            self._attach_screenshot("Failed to insert first name")
            raise Exception(f"Error inserting first name {str(e)}")

    @allure.step("Enter last name: {last_name}")
    def _input_last_name(self, last_name: str):
        """
        Enters the last name into the last name input field.

        Args:
            last_name (str): The last name to be entered.

        Raises:
            Exception: If the input operation fails.
        """
        try:
            self.fill_input(EditContactPageLocators.last_name_input, last_name)
        except Exception as e:
            self._attach_screenshot("Failed to insert last name")
            raise Exception(f"Error inserting last name {str(e)}")

    @allure.step("Enter birthdate: {birthdate}")
    def _input_birthdate(self, birthdate: str):
        """
        Enters the birthdate into the birthdate input field.

        Args:
            birthdate (str): The birthdate to be entered.

        Raises:
            Exception: If the input operation fails.
        """
        try:
            self.fill_input(EditContactPageLocators.birthdate_input, birthdate)
        except Exception as e:
            self._attach_screenshot("Failed to insert birthdate")
            raise Exception(f"Error inserting birthdate {str(e)}")

    @allure.step("Enter email: {email}")
    def _input_email(self, email: str):
        """
        Enters the email into the email input field.

        Args:
            email (str): The email address to be entered.

        Raises:
            Exception: If the input operation fails.
        """
        try:
            self.fill_input(EditContactPageLocators.email_input, email)
        except Exception as e:
            self._attach_screenshot("Failed to insert email")
            raise Exception(f"Error inserting email {str(e)}")

    @allure.step("Enter phone number: {phone}")
    def _input_phone(self, phone: str):
        """
        Enters the phone number into the phone input field.

        Args:
            phone (str): The phone number to be entered.

        Raises:
            Exception: If the input operation fails.
        """
        try:
            self.fill_input(EditContactPageLocators.phone_input, phone)
        except Exception as e:
            self._attach_screenshot("Failed to insert phone")
            raise Exception(f"Error inserting phone {str(e)}")

    @allure.step("Enter address line 1: {address_street_1}")
    def _input_address_street_1(self, address_street_1: str):
        """
        Enters the first address line into the corresponding input field.

        Args:
            address_street_1 (str): The first address line to be entered.

        Raises:
            Exception: If the input operation fails.
        """
        try:
            self.fill_input(EditContactPageLocators.address_street_1_input, address_street_1)
        except Exception as e:
            self._attach_screenshot("Failed to insert address_street_1")
            raise Exception(f"Error inserting address_street_1 {str(e)}")

    @allure.step("Enter address line 2: {address_street_2}")
    def _input_address_street_2(self, address_street_2: str):
        """
        Enters the second address line into the corresponding input field.

        Args:
            address_street_2 (str): The second address line to be entered.

        Raises:
            Exception: If the input operation fails.
        """
        try:
            self.fill_input(EditContactPageLocators.address_street_2_input, address_street_2)
        except Exception as e:
            self._attach_screenshot("Failed to insert address_street_2")
            raise Exception(f"Error inserting address_street_2 {str(e)}")

    @allure.step("Enter city: {city}")
    def _input_city(self, city: str):
        """
        Enters the city into the city input field.

        Args:
            city (str): The city to be entered.

        Raises:
            Exception: If the input operation fails.
        """
        try:
            self.fill_input(EditContactPageLocators.city_input, city)
        except Exception as e:
            self._attach_screenshot("Failed to insert city")
            raise Exception(f"Error inserting city {str(e)}")

    @allure.step("Enter state/province: {state_province}")
    def _input_state_province(self, state_province: str):
        """
        Enters the state or province into the state/province input field.

        Args:
            state_province (str): The state or province to be entered.

        Raises:
            Exception: If the input operation fails.
        """
        try:
            self.fill_input(EditContactPageLocators.state_province_input, state_province)
        except Exception as e:
            self._attach_screenshot("Failed to insert state_province")
            raise Exception(f"Error inserting state_province {str(e)}")

    @allure.step("Enter postal code: {postal_code}")
    def _input_postal_code(self, postal_code: str):
        """
        Enters the postal code into the postal code input field.

        Args:
            postal_code (str): The postal code to be entered.

        Raises:
            Exception: If the input operation fails.
        """
        try:
            self.fill_input(EditContactPageLocators.postal_code_input, postal_code)
        except Exception as e:
            self._attach_screenshot("Failed to insert postal_code")
            raise Exception(f"Error inserting postal_code {str(e)}")

    @allure.step("Enter country: {country}")
    def _input_country(self, country: str):
        """
        Enters the country into the country input field.

        Args:
            country (str): The country to be entered.

        Raises:
            Exception: If the input operation fails.
        """
        try:
            self.fill_input(EditContactPageLocators.country_input, country)
        except Exception as e:
            self._attach_screenshot("Failed to insert country")
            raise Exception(f"Error inserting country {str(e)}")

    @allure.step("Click Submit button")
    def _click_submit_button(self):
        """
        Clicks the Submit button to submit the form.

        Raises:
            Exception: If the click action fails.
        """
        try:
            self.click(EditContactPageLocators.submit_button)
        except Exception as e:
            self._attach_screenshot("Failed to click submit button")
            raise Exception(f"Error clicking submit button {str(e)}")

    @allure.step("Edit an existing contact with provided details")
    def edit_contact(self, first_name: str, last_name: str, email: str, phone: str | None, birthdate: str,
                     country: str | None, city: str | None, address_street_1: str | None,
                     address_street_2: str | None, state_province: str | None, postal_code: str | None):
        """
        Edits an existing contact with the provided details by filling the form and submitting it.

        Args:
            first_name (str): The first name of the contact.
            last_name (str): The last name of the contact.
            email (str): The email address of the contact.
            phone (str | None): The phone number of the contact (optional).
            birthdate (str): The birthdate of the contact.
            country (str | None): The country of the contact (optional).
            city (str | None): The city of the contact (optional).
            address_street_1 (str | None): The first line of the address (optional).
            address_street_2 (str | None): The second line of the address (optional).
            state_province (str | None): The state or province of the contact (optional).
            postal_code (str | None): The postal code of the contact (optional).

        Raises:
            Exception: If any input field fails to be populated or the submit button click fails.
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
            self._attach_screenshot("Failed to Update Contact")
            raise Exception(f"Error updating contact {str(e)}")
