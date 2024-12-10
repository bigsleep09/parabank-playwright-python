import pytest

from utils.file_handler import get_json


@pytest.mark.parametrize("registration_credentials", get_json("resources/registration_data.jsonc"))
def test_registration(setup, registration_credentials: dict[str, object]):
    pass
