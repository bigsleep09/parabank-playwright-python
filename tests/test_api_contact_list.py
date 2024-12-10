import allure
import pytest
from playwright.sync_api import expect, APIResponse


@allure.epic("Contact List API Testing")
class TestContactListAPI:

    @allure.story("User Registration")
    @pytest.mark.api
    def test_register_user(self, api_client):
        payload: dict[str, object] = {
            "firstName": "Test",
            "lastName": "User",
            "email": "test-rail4@fake.com",  # Change the email value after each run
            "password": "myPassword"
        }
        response: APIResponse = api_client.post("users", payload)

        try:
            response_data: dict[str, object] = response.json()
        except Exception:
            print("Exception raised while trying to json load the response_content.")

        # Use Playwright's expect to validate response status and data
        expect(response).to_be_ok()  # Asserts HTTP status is in 200-299 range
        assert '_id' in response_data.get('user'), "User ID not found in the response"
        assert 'token' in response_data, "Token not found in the response"
        api_client.set_token(response_data.get("token"))

    @allure.story("User Registration Failure (Email Already Exists)")
    @pytest.mark.api
    def test_register_user_with_existing_email(self, api_client):
        payload: dict[str, object] = {
            "firstName": "Test",
            "lastName": "User",
            "email": "test4@fake.com",  # Using an existing email for the negative test
            "password": "myPassword"
        }
        response: APIResponse = api_client.post("users", payload)

        # Validate that the response is not OK (conflict error, email already exists)
        expect(response).not_to_be_ok()
        response_data: dict[str, object] = response.json()
        assert response_data.get('message') == 'Email address is already in use', "Error message mismatch"

    @allure.story("User Login")
    @pytest.mark.api
    def test_login_user(self, api_client):
        payload: dict[str, object] = {"email": "test4@fake.com", "password": "myPassword"}
        response: APIResponse = api_client.post("users/login", payload)

        expect(response).to_be_ok()  # Check response status
        response_data: dict[str, object] = response.json()
        assert 'token' in response_data, "Token not found in the response"
        api_client.set_token(response_data.get("token"))

    @allure.story("User Login Failure (Incorrect Credentials)")
    @pytest.mark.api
    def test_login_user_with_incorrect_credentials(self, api_client):
        payload: dict[str, object] = {"email": "test4@fake.com", "password": "wrongPassword"}
        response: APIResponse = api_client.post("users/login", payload)

        expect(response).not_to_be_ok()  # Check for failure status (401 Unauthorized)

    @allure.story("Add New Contact")
    @pytest.mark.api
    def test_add_contact(self, api_client):
        payload: dict[str, object] = {
            "firstName": "Amy",
            "lastName": "Miller",
            "birthdate": "1992-02-02",
            "email": "amiller2@fake.com",
            "phone": "8005554242",
            "street1": "13 School St.",
            "street2": "Apt. 5",
            "city": "Washington",
            "stateProvince": "QC",
            "postalCode": "A1A1A1",
            "country": "USA"
        }
        response: APIResponse = api_client.post("contacts", payload)

        expect(response).to_be_ok()  # Validate status code
        response_data: dict[str, object] = response.json()
        assert '_id' in response_data, "Contact ID not found in the response"
        api_client.set_contact_id(response_data.get("_id"))  # Save for future tests

    @allure.story("Add Contact Failure (Invalid Email)")
    @pytest.mark.api
    def test_add_contact_with_invalid_email(self, api_client):
        payload: dict[str, object] = {
            "firstName": "Amy",
            "lastName": "Miller",
            "birthdate": "1992-02-02",
            "email": "invalid-email",  # Invalid email format
            "phone": "8005554242",
            "street1": "13 School St.",
            "street2": "Apt. 5",
            "city": "Washington",
            "stateProvince": "QC",
            "postalCode": "A1A1A1",
            "country": "USA"
        }
        response: APIResponse = api_client.post("contacts", payload)

        expect(response).not_to_be_ok()  # Validate failure status

    @allure.story("Get All Contacts")
    @pytest.mark.api
    def test_get_contact(self, api_client):
        response: APIResponse = api_client.get(f"contacts/{api_client.get_contact_id()}")

        expect(response).to_be_ok()  # Validate successful fetch
        contact: dict[str, object] = response.json()

        # Validate that the added contact exists in the response
        assert "amiller2@fake.com" in contact.get('email'), "Contact email not found"

    @allure.story("Update Contact")
    @pytest.mark.api
    def test_update_contact(self, api_client):
        payload: dict[str, object] = {
            "firstName": "Amy",
            "lastName": "Miller",
            "birthdate": "1992-02-02",
            "email": "amiller@fake.com",
            "phone": "8005554242",
            "street1": "13 School St.",
            "street2": "Apt. 5",
            "city": "Washington",
            "stateProvince": "QC",
            "postalCode": "A1A1A1",
            "country": "Canada"
        }
        response: APIResponse = api_client.put(f"contacts/{api_client.get_contact_id()}", payload)

        expect(response).to_be_ok()  # Validate status
        updated_contact: dict[str, object] = response.json()
        assert "amiller@fake.com" in updated_contact.get('email'), "Contact email not updated"

    @allure.story("Update Contact Failure (Invalid Contact ID)")
    @pytest.mark.api
    def test_update_contact_with_invalid_id(self, api_client):
        payload: dict[str, object] = {
            "firstName": "Amy",
            "lastName": "Miller",
            "birthdate": "1992-02-02",
            "email": "amiller@fake.com",
            "phone": "8005554242",
            "street1": "13 School St.",
            "street2": "Apt. 5",
            "city": "Washington",
            "stateProvince": "QC",
            "postalCode": "A1A1A1",
            "country": "Canada"
        }
        response: APIResponse = api_client.put("contacts/invalid_id", payload)

        expect(response).not_to_be_ok()  # Validate failure due to invalid ID

    @allure.story("Delete Contact")
    @pytest.mark.api
    def test_delete_contact(self, api_client):
        response: APIResponse = api_client.delete(f"contacts/{api_client.get_contact_id()}")

        expect(response).to_be_ok()  # Validate deletion
        # Verify deletion by fetching all contacts
        response = api_client.get("contacts")
        expect(response).to_be_ok()

    @allure.story("Delete Contact Failure (Invalid Contact ID)")
    @pytest.mark.api
    def test_delete_contact_with_invalid_id(self, api_client):
        response: APIResponse = api_client.delete("contacts/invalid_id")

        expect(response).not_to_be_ok()  # Validate failure due to invalid ID
