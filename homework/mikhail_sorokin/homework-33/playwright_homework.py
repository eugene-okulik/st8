from playwright.sync_api import sync_playwright


def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://the-internet.herokuapp.com')
        auth_page_link = page.get_by_role("link", name="Form Authentication")
        username_input = page.get_by_role("textbox", name="username")
        password_input = page.get_by_role("textbox", name="password")
        login_button = page.get_by_role("button", name="Login")
        auth_page_link.click()
        username_input.fill('test')
        password_input.fill('test')
        login_button.click()
        alert = page.get_by_text("Your username is invalid!")
        assert alert.is_visible()
        browser.close()
