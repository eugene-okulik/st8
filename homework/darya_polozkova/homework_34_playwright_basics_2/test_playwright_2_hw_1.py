from playwright.sync_api import Page, expect


def test_color_change_button(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    button = page.locator('#colorChange')
    expect(button).to_have_class('mt-4 text-danger btn btn-primary')
    button.click()
