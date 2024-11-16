import time

import pytest

from playwright.sync_api import Page, expect, BrowserContext, Playwright


@pytest.fixture(scope="session")
def browser(playwright: Playwright, launch_browser):
    playwright.selectors.set_test_id_attribute('name')
    browser = launch_browser()
    yield browser
    browser.close()


# @pytest.fixture
# def context(playwright: Playwright, launch_browser):
#     playwright.selectors.set_test_id_attribute('id')
#     browser = launch_browser()
#     # browser = playwright.firefox.launch(headless=False)
#     return browser.new_context()


@pytest.fixture
def page(context: BrowserContext) -> Page:
    page: Page = context.new_page()
    return page


def test_by_label(page: Page):
    page.goto('https://www.qa-practice.com/elements/input/simple')
    field = page.get_by_label('Text string')
    field.fill('alskjdhsd')
    time.sleep(3)


def test_by_id(page: Page):
    page.goto('https://www.qa-practice.com/elements/input/simple')
    # field = page.get_by_test_id('id_text_string')
    field = page.get_by_test_id('text_string')
    field.fill('alskjdhsd')
    time.sleep(3)


def test_by_locator(page: Page):
    page.goto('https://www.qa-practice.com/elements/input/simple')
    # field = page.get_by_test_id('id_text_string')
    # field = page.locator('.textinput')
    field = page.locator('//*[@name="text_string"]')
    field.fill('alskjdhsd')
    time.sleep(3)


def test_enabled(page):
    page.goto('https://www.qa-practice.com/elements/button/disabled')
    button = page.locator('#submit-id-submit')
    expect(button).not_to_be_enabled()
    page.locator('#id_select_state').select_option('enabled')
    expect(button).to_be_enabled()
    expect(button).to_have_text('Submit')


def test_wait(page):
    page_url = 'https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html?product_list_order=price'
    page.goto(page_url)
    print(page.url)
    page.locator('[data-role="direction-switcher"]').first.click()
    print(page.url)
    expect(page).not_to_have_url(page_url)
    print(page.url)
