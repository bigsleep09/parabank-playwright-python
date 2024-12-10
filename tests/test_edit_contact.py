import allure
import pytest
from playwright.sync_api import Page, expect

from locators.contact_list_locators import ContactDetailsPageLocators
from pages.contact_details_page import ContactDetailsPage
from pages.contacts_list_page import ContactListPage
from pages.edit_contact_page import EditContactPage
from pages.home_page import HomePage
from utils.file_handler import get_json


@allure.title("Test Update Contact")
@allure.description("Verify that a contact can be successfully updated with the given data.")
@pytest.mark.parametrize("login_credentials", get_json("resources/login_data.jsonc"))
@pytest.mark.user_interface
def test_update_contact(setup, login_credentials: dict[str, object]):
    """
    Test case to update an existing contact.

    This test case verifies that the user can update a contact's details. It involves logging in,
    selecting a contact, editing its details, and confirming that the updated information appears in
    the contact details form.

    Steps:
        1. Login with provided credentials.
        2. Navigate to the contact list page and verify login.
        3. Select a contact by index.
        4. Click the edit button and modify contact details.
        5. Save the changes and verify the updated details.

    Args:
        setup (Page): The Playwright page instance from the test setup.
        login_credentials (dict): Credentials used to log into the application.

    Asserts:
        - The updated contact details are correctly reflected in the contact details form.
    """
    update_contact_data: list[dict[str, object]] = get_json("resources/update_contact_data.jsonc")
    page: Page = setup
    home_page: HomePage = HomePage(page)
    for contact_to_update in update_contact_data:
        contact_list_page: ContactListPage = home_page.login_with_credential(str(login_credentials.get('email')),
                                                                             str(login_credentials.get('password')))
        contact_list_page.is_logged_in()
        page.wait_for_timeout(2000)
        contact_details_page: ContactDetailsPage = contact_list_page.select_contact_by_index(
            0)  # Change the index if you are looking for another contact
        page.wait_for_timeout(2000)
        contact_details_page.is_page_loaded()
        edit_contact_page: EditContactPage = contact_details_page.click_edit_contact_button()
        edit_contact_page.is_page_loaded()
        edit_contact_page.edit_contact(
            first_name=str(contact_to_update.get("firstName")), last_name=str(contact_to_update.get("lastName")),
            email=str(contact_to_update.get("email")), phone=str(contact_to_update.get("phone")),
            birthdate=str(contact_to_update.get("birthdate")),
            country=str(contact_to_update.get("country")), city=str(contact_to_update.get("city")),
            address_street_1=str(contact_to_update.get("street1")),
            address_street_2=str(contact_to_update.get('street2')),
            state_province=str(contact_to_update.get('stateProvince')),
            postal_code=str(contact_to_update.get('postalCode')))
        contact_details_page.is_page_loaded()
        page.wait_for_timeout(3000)
        contact_details_form_text: list[str] = page.locator(
            ContactDetailsPageLocators.contact_details_form).all_inner_texts()
        assert str(contact_to_update.get("firstName")) and str(contact_to_update.get("lastName")) and str(
            contact_to_update.get("email")) and str(contact_to_update.get("phone")) and str(
            contact_to_update.get("birthdate")) and str(contact_to_update.get("country")) and str(
            contact_to_update.get("city")) and str(contact_to_update.get("street1")) and str(
            contact_to_update.get('street2')) and str(contact_to_update.get('stateProvince')) and str(
            contact_to_update.get('postalCode')) in contact_details_form_text


@allure.title("Test Delete Contact")
@allure.description("Verify that a contact can be successfully deleted.")
@pytest.mark.parametrize("login_credentials", get_json("resources/login_data.jsonc"))
@pytest.mark.user_interface
def test_delete_contact(setup, login_credentials: dict[str, object]):
    """
    Test case to delete a contact.

    This test case verifies that the user can delete an existing contact. It involves logging in,
    selecting a contact, and performing the delete action. The test then ensures that the contact is
    removed by checking the current URL.

    Steps:
        1. Login with provided credentials.
        2. Navigate to the contact list page and verify login.
        3. Select a contact by index.
        4. Delete the contact and confirm the deletion.

    Args:
        setup (Page): The Playwright page instance from the test setup.
        login_credentials (dict): Credentials used to log into the application.

    Asserts:
        - The contact is deleted and the URL redirects to the contact list page.
    """
    page: Page = setup
    home_page: HomePage = HomePage(page)

    contact_list_page: ContactListPage = home_page.login_with_credential(str(login_credentials.get('email')),
                                                                         str(login_credentials.get('password')))
    contact_list_page.is_logged_in()
    page.wait_for_timeout(2000)
    contact_details_page: ContactDetailsPage = contact_list_page.select_contact_by_index(
        0)  # Change the index if you are looking for another contact
    page.wait_for_timeout(2000)
    contact_details_page.is_page_loaded()
    contact_details_page.delete_contact()
    page.wait_for_timeout(5000)
    expect(page).to_have_url(
        "https://thinking-tester-contact-list.herokuapp.com/contactList")  # Check for successful redirect
