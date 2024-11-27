import re

from playwright.sync_api import Page


class LogInWithoutCreds:
    URL = 'https://www.demoblaze.com/index.html'
    LOGIN_URL = 'https://api.demoblaze.com/login'

    def __init__(self, page: Page, base_url=URL, login_url=LOGIN_URL):
        self.page = page
        self.base_url = base_url
        self.login_url = login_url

    def open_web_page(self):
        self.page.goto(self.base_url)

    def open_login_screen(self):
        login_button = self.page.get_by_role("link", name="Log in")
        login_button.click()

    def login_with_incorrect_creds(self, name, email):
        username_field = self.page.locator('#loginusername')
        password_field = self.page.locator('#loginpassword')
        username_field.fill(name)
        password_field.fill(email)
        log_in_button = self.page.get_by_role("button", name="Log in")
        log_in_button.click()

    def check_if_error_message_correct(self):
        with self.page.expect_response(re.compile('/login$')) as response_event:
            response = response_event.value.json()
        assert response['errorMessage'] == 'User does not exist.', 'Error message is incorrect or missing!'
