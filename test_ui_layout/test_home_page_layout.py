from playwright.sync_api import Playwright, sync_playwright, expect
from pom.home_page_elements import HomePageElements
import pytest

@pytest.mark.integration
def test_about_us_section_verbiage(login_set_up)-> None:
    page=login_set_up
    # browser = playwright.chromium.launch(headless=False)
    # page = browser.new_page()
    # page.goto("https://symonstorozhenko.wixsite.com/website-1")
    # page.set_default_timeout(2000)
    home_page = HomePageElements(page)
    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()


    print("About the section verbiage")


@pytest.mark.regression
def test_about_us_section_verbiage_2(login_set_up)->None:
    page=login_set_up
    # browser = playwright.chromium.launch(headless=False)
    # page = browser.new_page()
    # page.goto("https://symonstorozhenko.wixsite.com/website-1")
    # page.set_default_timeout(2000)
    home_page = HomePageElements(page)
    # expect(page.locator("text=yooo")).not_to_be_visible()
    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()



    print("About the section verbiage")

