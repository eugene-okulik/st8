from playwright.sync_api import Page, expect, BrowserContext


def test_text_in_a_new_tab(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    with context.expect_page() as new_tab_event:
        link = page.locator('#new-page-button')
        link.click()
        page2 = new_tab_event.value
    text = page2.locator('#result-text')
    expect(text).to_have_text('I am a new page in a new tab')
    expect(link).to_be_enabled()
