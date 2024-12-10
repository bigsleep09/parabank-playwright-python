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
    page = setup
    home_page: HomePage = HomePage(page)
    contact_list_page: ContactListPage = home_page.login_with_credential(str(login_credentials.get('email')),
                                                                         str(login_credentials.get('password')))
    contact_list_page.is_logged_in()
    contacts_to_add: list[dict[str, object]] = get_json("resources/add_contact.jsonc")
    for contact in contacts_to_add:
        add_contact_page: AddContactPage = contact_list_page.click_add_new_contact()
        add_contact_page.is_page_loaded()
        add_contact_page.add_new_contact(
            first_name=str(contact.get("firstName")), last_name=str(contact.get("lastName")),
            email=str(contact.get("email")), phone=str(contact.get("phone")),
            birthdate=str(contact.get("birthdate")),
            country=str(contact.get("country")), city=str(contact.get("city")),
            address_street_1=str(contact.get("street1")),
            address_street_2=str(contact.get('street2')),
            state_province=str(contact.get('stateProvince')),
            postal_code=str(contact.get('postalCode')))
        page.wait_for_timeout(5000)
        expect(page).to_have_url("https://thinking-tester-contact-list.herokuapp.com/contactList")
        table_inner_text_list: list[str] = page.locator(ContactListPageLocators.contacts_table).all_inner_texts()
        table_inner_text_list_formated: list[str] = [text.replace("\t", " ") for text in table_inner_text_list]
        contact_added: bool = False
        for item in table_inner_text_list_formated:
            if item.__contains__(str(contact.get("email"))):
                contact_added = True
                break

        assert contact_added is True


from utils.file_handler import get_json
