from playwright.sync_api import Page, expect


def test_ok_on_alert(page: Page):
    page.on("dialog", lambda dialog: dialog.accept())
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.locator('.a-button').click()
    result = page.locator('.result-text')
    expect(result).to_have_text('Ok')
