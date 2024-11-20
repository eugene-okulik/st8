import time

import pytest

from playwright.sync_api import Page, expect, BrowserContext, Playwright
# from playwright.sync_api import Dialog


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


def test_hover(page: Page):
    page.goto('https://magento.softwaretestingboard.com/')
    men = page.locator('#ui-id-5')
    tops = page.locator('#ui-id-17')
    jackets = page.locator('#ui-id-19')
    men.hover()
    tops.hover()
    jackets.click()
    time.sleep(3)


def test_d_n_d(page):
    page.goto('https://www.qa-practice.com/elements/dragndrop/boxes')
    drag_me = page.locator('#rect-draggable')
    drop_here = page.locator('#rect-droppable')
    drag_me.drag_to(drop_here)


def test_iframe(page):
    page.goto('https://www.qa-practice.com/elements/iframe/iframe_page')
    iframe = page.frame_locator('iframe')
    burger_button = iframe.locator('.navbar-toggler-icon')
    burger_button.click()
    time.sleep(3)


def test_tabs(page, context: BrowserContext):
    # time.sleep(3)
    page.goto('https://www.qa-practice.com/elements/new_tab/link')
    with context.expect_page() as new_tab_event:
        link = page.locator('#new-page-link')
        link.click()
        page2 = new_tab_event.value

    result_text = page2.locator('#result-text')
    expect(result_text).to_have_text('I am a new page in a new tab')
    link.click()


def test_alert(page):
    # def handle_dialog(dialog: Dialog):
    #     dialog.dismiss()
    #
    # page.on('dialog', handle_dialog)
    # page.on('dialog', lambda dialog: dialog.dismiss())
    # page.on('dialog', lambda dialog: dialog.accept())
    page.on('dialog', lambda dialog: dialog.accept('some text'))

    page.goto('https://www.qa-practice.com/elements/alert/prompt')
    page.locator('.a-button').click()
    time.sleep(3)


def test_vivino(page):
    page.goto('https://www.vivino.com/', wait_until="domcontentloaded")
    chevron = page.locator('[class="chevron_chevron__GAztI chevron_down__1KPaT"]')
    chevron.click()
    time.sleep(2)
