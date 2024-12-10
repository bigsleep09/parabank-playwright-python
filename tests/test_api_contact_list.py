import allure
import pytest
from playwright.sync_api import expect, APIResponse

from utils.file_handler import get_json


@allure.epic("Contact List API Testing")
class TestContactListAPI:
    """
    Test suite for API interactions with the Contact List service.

    This suite includes tests for user registration, user login, adding, updating, retrieving, and deleting contacts.

    Each test case is documented to ensure that the API interactions are valid and the responses are correct.
    """

    @allure.story("User Registration")
    @pytest.mark.api
    @pytest.mark.parametrize("registration_credentials", get_json("resources/registration_data.jsonc"))
    def test_register_user(self, api_client, registration_credentials: dict[str, object]):
        """
        Test case for registering a new user.

        This test registers a user by sending a POST request with the provided registration credentials.

        Parameters:
            api_client (APIClient): The client used to send API requests.
            registration_credentials (dict): The credentials used to register a new user, containing:
                - 'firstName': User's first name.
                - 'lastName': User's last name.
                - 'email': User's email address.
                - 'password': User's password.

        Asserts:
            - Response status is OK (200-299).
            - The response contains a user ID and a token.
        """
        response: APIResponse = api_client.post("users", registration_credentials)

        try:
            response_data: dict[str, object] = response.json()
        except Exception:
            print("Exception raised while trying to json load the response_content.")

        # Assert response status is OK (200-299)
        expect(response).to_be_ok()
        # Check that user ID and token are present in the response
        assert '_id' in response_data.get('user'), "User ID not found in the response"
        assert 'token' in response_data, "Token not found in the response"
        # Set token for further requests
        api_client.set_token(response_data.get("token"))

    @allure.story("User Registration Failure (Email Already Exists)")
    @pytest.mark.api
    def test_register_user_with_existing_email(self, api_client):
        """
        Test case for user registration failure due to email already in use.

        This test attempts to register a user with an email that already exists in the system.

        Parameters:
            api_client (APIClient): The client used to send API requests.

        Asserts:
            - The response status is not OK (conflict error, email already exists).
            - The response contains a message indicating the email is already in use.
        """
        payload: dict[str, object] = {
            "firstName": "Test",
            "lastName": "User",
            "email": "test4@fake.com",  # Using an existing email for the negative test
            "password": "myPassword"
        }
        response: APIResponse = api_client.post("users", payload)

        # Assert response status is not OK (email conflict)
        expect(response).not_to_be_ok()
        response_data: dict[str, object] = response.json()
        # Assert the error message
        assert response_data.get('message') == 'Email address is already in use', "Error message mismatch"

    @allure.story("User Login")
    @pytest.mark.api
    @pytest.mark.parametrize("login_credentials", get_json("resources/login_data.jsonc"))
    def test_login_user(self, api_client, login_credentials: dict[str, object]):
        """
        Test case for logging in a user.

        This test logs in using the provided credentials and validates the presence of a token in the response.

        Parameters:
            api_client (APIClient): The client used to send API requests.
            login_credentials (dict): The credentials used for login, containing:
                - 'email': User's email address.
                - 'password': User's password.

        Asserts:
            - Response status is OK (200-299).
            - The response contains a token.
        """
        response: APIResponse = api_client.post("users/login", login_credentials)

        expect(response).to_be_ok()  # Validate status
        response_data: dict[str, object] = response.json()
        # Assert token presence
        assert 'token' in response_data, "Token not found in the response"
        api_client.set_token(response_data.get("token"))

    @allure.story("User Login Failure (Incorrect Credentials)")
    @pytest.mark.api
    def test_login_user_with_incorrect_credentials(self, api_client):
        """
        Test case for user login failure due to incorrect credentials.

        This test attempts to log in with incorrect credentials (wrong password).

        Parameters:
            api_client (APIClient): The client used to send API requests.

        Asserts:
            - The response status is not OK (401 Unauthorized).
        """
        payload: dict[str, object] = {"email": "test4@fake.com", "password": "wrongPassword"}
        response: APIResponse = api_client.post("users/login", payload)

        expect(response).not_to_be_ok()  # Check for failure status (401 Unauthorized)

    @allure.story("Add New Contact")
    @pytest.mark.api
    def test_add_contact(self, api_client):
        """
        Test case for adding a new contact.

        This test adds a new contact using a POST request and validates the successful addition.

        Parameters:
            api_client (APIClient): The client used to send API requests.

        Asserts:
            - Response status is OK (200-299).
            - The response contains a contact ID.
        """
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
        """
        Test case for adding a contact with an invalid email.

        This test attempts to add a new contact with an invalid email format.

        Parameters:
            api_client (APIClient): The client used to send API requests.

        Asserts:
            - Response status is not OK (failure due to invalid email).
        """
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
        """
        Test case for retrieving a contact by ID.

        This test fetches a contact using the contact ID and validates the response.

        Parameters:
            api_client (APIClient): The client used to send API requests.

        Asserts:
            - Response status is OK (200-299).
            - The contact email is present in the response.
        """
        response: APIResponse = api_client.get(f"contacts/{api_client.get_contact_id()}")

        expect(response).to_be_ok()  # Validate successful fetch
        contact: dict[str, object] = response.json()
        assert "amiller2@fake.com" in contact.get('email'), "Contact email not found"

    @allure.story("Update Contact")
    @pytest.mark.api
    def test_update_contact(self, api_client):
        """
        Test case for updating a contact.

        This test updates a contact's details and validates the updated contact's data.

        Parameters:
            api_client (APIClient): The client used to send API requests.

        Asserts:
            - Response status is OK (200-299).
            - The contact's email is updated.
        """
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
        """
        Test case for updating a contact with an invalid contact ID.

        This test attempts to update a contact using an invalid contact ID.

        Parameters:
            api_client (APIClient): The client used to send API requests.

        Asserts:
            - Response status is not OK (failure due to invalid contact ID).
        """
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
        """
        Test case for deleting a contact.

        This test deletes a contact by ID and verifies successful deletion.

        Parameters:
            api_client (APIClient): The client used to send API requests.

        Asserts:
            - Response status is OK (200-299).
        """
        response: APIResponse = api_client.delete(f"contacts/{api_client.get_contact_id()}")

        expect(response).to_be_ok()  # Validate deletion
        # Verify deletion by fetching all contacts
        response = api_client.get("contacts")
        expect(response).to_be_ok()

    @allure.story("Delete Contact Failure (Invalid Contact ID)")
    @pytest.mark.api
    def test_delete_contact_with_invalid_id(self, api_client):
        """
        Test case for attempting to delete a contact with an invalid ID.

        This test tries to delete a contact using an invalid contact ID.

        Parameters:
            api_client (APIClient): The client used to send API requests.

        Asserts:
            - Response status is not OK (failure due to invalid contact ID).
        """
        response: APIResponse = api_client.delete("contacts/invalid_id")

        expect(response).not_to_be_ok()  # Validate failure due to invalid ID
