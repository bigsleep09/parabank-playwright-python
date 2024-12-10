import pytest
from playwright.sync_api import expect

from locators.contact_list_locators import ContactListPageLocators
from pages.add_contact_page import AddContactPage
from pages.contacts_list_page import ContactListPage
from pages.home_page import HomePage
from utils.file_handler import get_json


@pytest.mark.parametrize("login_credentials", get_json("resources/login_data.jsonc"))
@pytest.mark.user_interface
def test_add_contact(setup, login_credentials: dict[str, object]):
    """
    Test for adding a new contact to the contact list.

    This test logs in using the provided credentials, navigates to the 'Add Contact' page,
    adds new contacts as per the data in the resources/add_contact.jsonc file,
    and verifies that the newly added contact appears in the contact list.

    Parameters:
        setup (Page): The setup function that provides a Playwright Page instance for testing.
        login_credentials (dict): The login credentials used to authenticate the user.
            - 'email': User's email for login.
            - 'password': User's password for login.

    Steps:
        1. Log in using the credentials provided.
        2. Navigate to the 'Add Contact' page.
        3. Add contacts by filling in their details from the add_contact.jsonc file.
        4. Validate that the newly added contact is listed in the contact list.
        5. Assert that the contact appears in the table based on their email.

    Asserts:
        - The contact is successfully added to the contact list.
        - The contact is visible in the table using their email address.

    Raises:
        AssertionError: If the contact is not added or not visible in the list.
    """
    page = setup
    home_page: HomePage = HomePage(page)

    # Logging in with credentials
    contact_list_page: ContactListPage = home_page.login_with_credential(str(login_credentials.get('email')),
                                                                         str(login_credentials.get('password')))
    contact_list_page.is_logged_in()

    # Fetching the contacts data to be added
    contacts_to_add: list[dict[str, object]] = get_json("resources/add_contact.jsonc")

    # Adding contacts
    for contact in contacts_to_add:
        add_contact_page: AddContactPage = contact_list_page.click_add_new_contact()
        add_contact_page.is_page_loaded()

        # Filling out and submitting the contact form
        add_contact_page.add_new_contact(
            first_name=str(contact.get("firstName")),
            last_name=str(contact.get("lastName")),
            email=str(contact.get("email")),
            phone=str(contact.get("phone")),
            birthdate=str(contact.get("birthdate")),
            country=str(contact.get("country")),
            city=str(contact.get("city")),
            address_street_1=str(contact.get("street1")),
            address_street_2=str(contact.get('street2')),
            state_province=str(contact.get('stateProvince')),
            postal_code=str(contact.get('postalCode'))
        )

        # Wait for the page to reload after contact is added
        page.wait_for_timeout(5000)

        # Verifying if the URL matches the expected contact list page URL
        expect(page).to_have_url("https://thinking-tester-contact-list.herokuapp.com/contactList")

        # Extracting the list of contacts from the contact table
        table_inner_text_list: list[str] = page.locator(ContactListPageLocators.contacts_table).all_inner_texts()
        table_inner_text_list_formated: list[str] = [text.replace("\t", " ") for text in table_inner_text_list]

        # Checking if the new contact's email is present in the table
        contact_added: bool = False
        for item in table_inner_text_list_formated:
            if item.__contains__(str(contact.get("email"))):
                contact_added = True
                break

        # Asserting the contact was added successfully
        assert contact_added is True
