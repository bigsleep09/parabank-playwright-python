from playwright.sync_api import APIRequestContext, APIResponse


class APIClient:
    def __init__(self, request_context: APIRequestContext, base_url: str):
        self.request = request_context
        self.base_url = base_url
        self.token = None
        self.contact_id = None

    def set_token(self, token: str):
        self.token = token

    def set_contact_id(self, contact_id: str):
        self.contact_id = contact_id

    def get_contact_id(self):
        return self.contact_id

    def _headers(self) -> dict[str, str]:
        headers = {"Content-Type": "application/json",
                   "Cookie": "token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NzU2ZjkyNWRlY2U3NjAwMTNkZjczYmQiLCJpYXQiOjE3MzM4MjQ0OTd9.LPYdGcfqZZG6eywmVRQR4AGjspEVkwTsbiOr9He4rDs"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def post(self, endpoint: str, payload: dict) -> APIResponse:
        return self.request.post(f"{self.base_url}/{endpoint}", headers=self._headers(), data=payload)

    def get(self, endpoint: str) -> APIResponse:
        return self.request.get(f"{self.base_url}/{endpoint}", headers=self._headers())

    def put(self, endpoint: str, payload: dict) -> APIResponse:
        return self.request.put(f"{self.base_url}/{endpoint}", headers=self._headers(), data=payload)

    def delete(self, endpoint: str) -> APIResponse:
        return self.request.delete(f"{self.base_url}/{endpoint}", headers=self._headers())
