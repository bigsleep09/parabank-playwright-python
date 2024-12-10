import allure
import json5


@allure.step("Get data from JSON file")
def get_json(filepath: str) -> list[dict[str, object]]:
    """
    Reads a JSON5 file and returns its contents as a list of dictionaries.

    Args:
        filepath (str): The path to the JSON5 file.

    Returns:
        list[dict[str, object]]: A list of dictionaries representing the parsed data.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If there is an error decoding the JSON data.

    Example:
        >>> data = get_json("resources/login_data.jsonc")
        >>> print(data)
        [{'email': 'user@example.com', 'password': 'password123'}]
    """
    try:
        with open(filepath, 'r') as file:
            file_data: list[dict[str, object]] = json5.load(file)
            return file_data
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {filepath}. Error: {str(e)}")
    except ValueError as e:
        raise ValueError(f"Error decoding JSON file: {filepath}. Error: {str(e)}")
    except Exception as e:
        raise Exception(f"An unexpected error occurred while reading the JSON file: {str(e)}")
