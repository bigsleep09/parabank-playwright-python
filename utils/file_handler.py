import allure
import json5


@allure.step("get_json")
def get_json(filepath: str) -> list[dict[str, object]]:
    with open(f"{filepath}") as file:
        file_data: list[dict[str, object]] = json5.load(file)
        return file_data
