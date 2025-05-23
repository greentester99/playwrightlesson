import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def set_up():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)  # Visual debugging
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://symonstorozhenko.wixsite.com/website-1")
        page.set_default_timeout(5000)
        page.wait_for_load_state("networkidle")  # Ensures page and scripts fully load
        yield page
        context.close()
        browser.close()

@pytest.fixture(scope="session")
def login_set_up(set_up):
    page = set_up

    # Click initial handle button
    page.get_by_test_id("handle-button").click()

    # Wait for and click the sign-up switch button
    page.get_by_test_id("signUp.switchToSignUp").wait_for(state="visible", timeout=5000)
    page.get_by_test_id("signUp.switchToSignUp").click()

    return page
