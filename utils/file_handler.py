import allure
import json5


@allure.step("get_json")
def get_json(filepath: str) -> dict[str, object]:
    with open(f"{filepath}") as file:
        file_data: dict[str, object] = json5.load(file)
        return file_data
