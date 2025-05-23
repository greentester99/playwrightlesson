import os

import pytest
import playwright
from playwright.sync_api import Playwright, expect
import time
import pytest
# import utils.secret_config


@pytest.fixture(scope="session")
def set_up(browser):
    # browser = playwright.chromium.launch(headless=False,) #slow_mo=500#
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)



    yield page
    page.close()


@pytest.fixture(scope="session")
def login_set_up(set_up):
    # browser = playwright.chromium.launch(headless=False,) #slow_mo=500#
    # context = browser.new_context()
    # page = context.new_page()
    # page.goto("")
    # page.set_default_timeout(3000)

    page = set_up


    # page.wait_for_load_state('networkidle')
    page.get_by_test_id("handle-button").click()
    # page.click("text=Log In")
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.click("'Log in with Email' ")
    page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").fill("symon.storozhenko@gmail.com")
    page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").press("Tab")
    # page.get_by_role("textbox", name="Password").fill(utils.secret_config.PASSWORD )
    page.get_by_role("textbox", name="Password").fill(os.environ["PASSWORD"] )

    page.get_by_role("textbox", name="Password").press("Enter")
    expect(page.get_by_role("button", name="Log in with Email")).to_be_hidden()
    expect(page.locator("text=Fashion You’ll Love")).to_be_visible()
    print('yayi')


    yield page



@pytest.fixture
def go_to_new_collection(page):
    # browser = playwright.chromium.launch(headless=False,) #slow_mo=500#
    # context = browser.new_context()
    # page = context.new_page()
    page.goto("/new-collection")
    page.set_default_timeout(3000)



    yield page