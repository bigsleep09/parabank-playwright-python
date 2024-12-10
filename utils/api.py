from datetime import datetime
from typing import Literal

import allure
import json5
import requests


@allure.step("send_request")
def send_request(
        method: str,
        url: str,
        options_type: str = Literal["params", "data", "json"],
        options: dict[str, object] | None = {},
        print_response: bool = True,
        print_request: bool = True,
        print_headers: bool = False,
) -> dict[str, object] | str:
    send_time = datetime.now()

    if print_request:
        print(f"\nSending request at {send_time} to: {url} with params:\n{options}")

    method = method.lower()
    options_type = options_type.lower()

    request_type = {"get": requests.get, "post": requests.post}

    if method not in request_type:
        raise ValueError(f"Unsupported method: {method}")

    if options_type not in {"params", "data", "json"}:
        raise ValueError(f"Unsupported options type: {options_type}")

    response: requests.Response = request_type[method](
        url=url, **{options_type: options}
    )

    response_time = datetime.now()

    response_content: str = response.content.decode(encoding="utf-8")
    response_content_body: dict[str, object] = {}
    try:
        response_content_body = json5.loads(response_content)
    except Exception:
        print("Exception raised while trying to json load the response_content.")

    if print_response:
        if print_headers:
            print(
                f"\nResponse headers: {response.headers}"
            )
        print(
            f"\nResponse body received at {response_time}: {response_content_body}"
        )

    if bool(response_content_body):
        return response_content_body
    else:
        return response_content
