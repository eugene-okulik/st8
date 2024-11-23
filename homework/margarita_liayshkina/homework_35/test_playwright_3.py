import pytest
from playwright.sync_api import Page, expect, BrowserContext, Playwright


@pytest.fixture(scope="session")
def browser(playwright: Playwright, launch_browser):
    playwright.selectors.set_test_id_attribute('name')
    browser = launch_browser()
    yield browser
    browser.close()


@pytest.fixture
def page(context: BrowserContext) -> Page:
    page: Page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    return page


def test_alert(page):
    page.on('dialog', lambda dialog: dialog.accept())
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.locator('a.a-button').click()
    selected_message = page.locator('#result')
    expect(selected_message).to_be_visible()
    result_text = page.locator('#result-text')
    expect(result_text).to_be_visible()
    expect(result_text).to_have_text('Ok')


def test_new_tabe(page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    with context.expect_page() as new_tab_event:
        page.locator('.a-button').click()
        page2 = new_tab_event.value

    result_text = page2.locator('#result-text')
    expect(result_text).to_have_text('I am a new page in a new tab')
    expect(page.locator('a.a-button')).to_be_enabled()
