import os
import pytest
from playwright.sync_api import expect

print("⚙️ Loading conftest.py...")

@pytest.fixture(scope="session")
def get_password():
    """
    Securely retrieves the PASSWORD environment variable.
    """
    print("🔐 Checking PASSWORD environment variable...")
    password = os.getenv("PASSWORD")
    if not password:
        raise EnvironmentError("❌ PASSWORD environment variable is not set.")
    return password


@pytest.fixture(scope="session")
def set_up(browser):
    """
    Launches the site and returns the page object.
    """
    print("🌐 Setting up browser context...")
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(15000)
    page.wait_for_load_state("networkidle")
    yield page
    context.close()


@pytest.fixture(scope="session")
def login_set_up(set_up, get_password):
    """
    Logs in using the provided credentials and returns an authenticated page.
    """
    print("🔑 Setting up login...")
    page = set_up
    password = get_password

    expect(page.get_by_test_id("handle-button")).to_be_visible()
    page.get_by_test_id("handle-button").click()

    expect(page.get_by_test_id("signUp.switchToSignUp")).to_be_visible()
    page.get_by_test_id("signUp.switchToSignUp").click()

    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").fill("symon.storozhenko@gmail.com")
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("textbox", name="Password").press("Enter")

    expect(page.get_by_role("button", name="Log in with Email")).to_be_hidden()
    expect(page.locator("text=Fashion You’ll Love")).to_be_visible()

    yield page
