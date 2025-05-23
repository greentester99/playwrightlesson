import pytest
from playwright.sync_api import expect
from pom.home_page_elements import HomePageElements


@pytest.mark.integration
def test_about_us_section_verbiage(login_set_up):
    """
    Verifies that the About Us section header and body are visible (integration test).
    """
    page = login_set_up
    home_page = HomePageElements(page)

    page.wait_for_load_state('networkidle')

    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()

    print("✅ Checked About Us verbiage - integration test")


@pytest.mark.regression
def test_about_us_section_verbiage_2(login_set_up):
    """
    Verifies the About Us section is still visible under regression test context.
    """
    page = login_set_up
    home_page = HomePageElements(page)

    page.wait_for_load_state('networkidle')

    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()

    print("✅ Checked About Us verbiage - regression test")
