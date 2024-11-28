from playwright.sync_api import Page, expect


def test_get_by_role(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    search_field = page.get_by_role('link', name='Form Authentication')
    search_field.press('Enter')
    username = page.get_by_role('textbox', name='username')
    username.fill('tomsmith')
    username.press('Enter')
    password = page.get_by_role('textbox', name='password')
    password.fill('SuperSecretPassword!')
    password.press('Enter')
    expect(page).to_have_url('https://the-internet.herokuapp.com/login')
