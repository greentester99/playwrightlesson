import playwright
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest



@pytest.mark.smoke
@pytest.mark.regression
def test_logged_user_can_view_my_orders_menu(login_set_up) -> None:
    page= login_set_up


    # # page.wait_for_load_state('networkidle')
    # page.get_by_test_id("handle-button").click()
    # # page.click("text=Log In")
    # page.get_by_test_id("signUp.switchToSignUp").click()
    # page.click("'Log in with Email' ")
    # page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").fill("symon.storozhenko@gmail.com")
    # page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").press("Tab")
    # page.get_by_role("textbox", name="Password").fill("test123", )
    # page.get_by_role("textbox", name="Password").press("Enter")
    # expect(page.get_by_role("button", name="Log in with Email")).to_be_hidden()
    expect(page.locator("text=Fashion You’ll Love")).to_be_visible()
    print('yayi')

