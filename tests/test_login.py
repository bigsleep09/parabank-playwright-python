import allure
import pytest

from pages.contact_list_page import ContactListPage
from pages.home_page import HomePage
from utils.file_handler import get_json


@allure.story("Test")
@pytest.mark.parametrize("login_credentials", get_json("resources/login_data.jsonc"))
def test_login(setup, login_credentials: dict[str, object]):
    page = setup
    home_page: HomePage = HomePage(page)
    contact_list_page: ContactListPage = home_page.login_with_credential(str(login_credentials.get('email')),
                                                                         str(login_credentials.get('password')))
    contact_list_page.is_logged_in()
