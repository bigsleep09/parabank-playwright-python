import os

import allure
import pytest
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page, APIRequestContext

from utils.api import APIClient

MAIN_URL: str = "https://thinking-tester-contact-list.herokuapp.com"


@pytest.fixture(scope="function")
def setup():
    with sync_playwright() as playwright:
        browser: Browser = playwright.chromium.launch(headless=False, slow_mo=500, args=['--start-maximized'])
        context: BrowserContext = browser.new_context(no_viewport=True)
        page: Page = context.new_page()
        page.goto(MAIN_URL)
        yield page  # Return the 'page' object
        browser.close()


@pytest.fixture(scope="session")
def api_client():
    with sync_playwright() as playwright:
        request_context: APIRequestContext = playwright.request.new_context()
        client = APIClient(request_context, MAIN_URL)
        yield client
        request_context.dispose()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    # Hook to add a screenshot to Allure in case of test failure
    outcome = yield
    report = outcome.get_result()
    if "api" in item.keywords:  # Check for the @pytest.mark.api marker
        return
    if report.when == "call" and report.failed:
        try:
            page = item.funcargs["setup"]  # Access 'setup' fixture (the page object)
            screenshot_dir = "allure-results/screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)  # Ensure directory exists
            screenshot_path = f"{screenshot_dir}/{item.name}.png"
            page.screenshot(path=screenshot_path)
            allure.attach.file(screenshot_path, name="Screenshot on Failure",
                               attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(f"Error capturing screenshot: {e}")
