import os

import allure
import pytest
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page, APIRequestContext

from utils.api import APIClient

MAIN_URL: str = "https://thinking-tester-contact-list.herokuapp.com"


@pytest.fixture(scope="function")
def setup():
    """
    Fixture to initialize the Playwright browser page instance.

    This fixture launches a Chromium browser with the provided configuration (headless=False for visual debugging,
    slow motion enabled, maximized window) and navigates to the main URL of the application.
    The page object is returned for use in the test and ensures browser cleanup after test execution.

    Scope: 'function' (Each test will have a fresh browser page instance)

    Returns:
        page (Page): The Playwright page instance that represents the browser tab.

    Cleanup:
        The browser is closed after the test completes.
    """
    with sync_playwright() as playwright:
        browser: Browser = playwright.chromium.launch(headless=False, slow_mo=500, args=['--start-maximized'])
        context: BrowserContext = browser.new_context(no_viewport=True)
        page: Page = context.new_page()
        page.goto(MAIN_URL)
        yield page  # Return the 'page' object to be used in the test
        browser.close()


@pytest.fixture(scope="session")
def api_client():
    """
    Fixture to create an API client for making requests to the backend.

    This fixture sets up an APIClient instance, which uses Playwright's request context for interacting with the API.
    The fixture is scoped to the session, meaning the same instance is shared across multiple tests.

    Scope: 'session' (The same client instance will be used throughout the session)

    Returns:
        client (APIClient): The APIClient instance for making API requests.

    Cleanup:
        The request context is disposed after the session ends.
    """
    with sync_playwright() as playwright:
        request_context: APIRequestContext = playwright.request.new_context()
        client = APIClient(request_context, MAIN_URL)
        yield client
        request_context.dispose()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Hook to capture a screenshot in case of test failure.

    This hook adds functionality to capture a screenshot when a test fails, provided the test is not marked as
    an API test (via @pytest.mark.api). The screenshot is stored in the 'allure-results/screenshots' directory
    and attached to the Allure report.

    This hook runs after each test case execution to check the outcome and determine if a screenshot should be captured.

    Args:
        item: The test item (test function) being executed.

    Note:
        If the test fails, a screenshot is captured and attached to the Allure report for visual inspection.
    """
    outcome = yield
    report = outcome.get_result()
    if "api" in item.keywords:  # Skip API tests
        return
    if report.when == "call" and report.failed:
        try:
            page = item.funcargs["setup"]  # Access 'setup' fixture (the page object)
            screenshot_dir = "allure-results/screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)  # Ensure the directory exists
            screenshot_path = f"{screenshot_dir}/{item.name}.png"
            page.screenshot(path=screenshot_path)  # Capture screenshot
            allure.attach.file(screenshot_path, name="Screenshot on Failure",
                               attachment_type=allure.attachment_type.PNG)  # Attach to Allure report
        except Exception as e:
            print(f"Error capturing screenshot: {e}")
