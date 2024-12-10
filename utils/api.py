import allure
from playwright.sync_api import APIRequestContext, APIResponse


class APIClient:
    def __init__(self, request_context: APIRequestContext, base_url: str):
        """
        Initializes the APIClient with a request context and base URL.

        Args:
            request_context (APIRequestContext): The Playwright API request context to handle requests.
            base_url (str): The base URL for API requests.
        """
        self.request = request_context
        self.base_url = base_url
        self.token = None
        self.contact_id = None

    @allure.step("Set the API token")
    def set_token(self, token: str):
        """
        Set the token to be used for authentication in subsequent requests.

        Args:
            token (str): The token to authenticate API requests.
        """
        self.token = token

    @allure.step("Set contact ID")
    def set_contact_id(self, contact_id: str):
        """
        Set the contact ID for use in requests.

        Args:
            contact_id (str): The contact ID to use in API requests.
        """
        self.contact_id = contact_id

    def get_contact_id(self):
        """
        Retrieves the current contact ID.

        Returns:
            str: The current contact ID.
        """
        return self.contact_id

    def _headers(self) -> dict[str, str]:
        """
        Construct headers for API requests.

        Returns:
            dict: The headers dictionary including authorization if a token is set.
        """
        headers = {
            "Content-Type": "application/json",
            "Cookie": "token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NzU2ZjkyNWRlY2U3NjAwMTNkZjczYmQiLCJpYXQiOjE3MzM4MjQ0OTd9.LPYdGcfqZZG6eywmVRQR4AGjspEVkwTsbiOr9He4rDs"
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    @allure.step("Send POST request to {endpoint}")
    def post(self, endpoint: str, payload: dict) -> APIResponse:
        """
        Send a POST request to the specified endpoint with the provided payload.

        Args:
            endpoint (str): The endpoint to send the POST request to.
            payload (dict): The data to send in the request body.

        Returns:
            APIResponse: The response from the API.
        """
        return self.request.post(f"{self.base_url}/{endpoint}", headers=self._headers(), data=payload)

    @allure.step("Send GET request to {endpoint}")
    def get(self, endpoint: str) -> APIResponse:
        """
        Send a GET request to the specified endpoint.

        Args:
            endpoint (str): The endpoint to send the GET request to.

        Returns:
            APIResponse: The response from the API.
        """
        return self.request.get(f"{self.base_url}/{endpoint}", headers=self._headers())

    @allure.step("Send PUT request to {endpoint}")
    def put(self, endpoint: str, payload: dict) -> APIResponse:
        """
        Send a PUT request to the specified endpoint with the provided payload.

        Args:
            endpoint (str): The endpoint to send the PUT request to.
            payload (dict): The data to send in the request body.

        Returns:
            APIResponse: The response from the API.
        """
        return self.request.put(f"{self.base_url}/{endpoint}", headers=self._headers(), data=payload)

    @allure.step("Send DELETE request to {endpoint}")
    def delete(self, endpoint: str) -> APIResponse:
        """
        Send a DELETE request to the specified endpoint.

        Args:
            endpoint (str): The endpoint to send the DELETE request to.

        Returns:
            APIResponse: The response from the API.
        """
        return self.request.delete(f"{self.base_url}/{endpoint}", headers=self._headers())
