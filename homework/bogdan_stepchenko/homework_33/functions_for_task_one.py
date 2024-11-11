from playwright.sync_api import Page


class LoginTest:
    BASE_URL = 'https://the-internet.herokuapp.com/'
    USERNAME_ERROR = 'Your username is invalid!'
    LOGIN_URL = 'https://the-internet.herokuapp.com/login'

    def __init__(self, page: Page, base_url = BASE_URL):
        self.page = page
        self.base_url = base_url

    def open_web_page(self, url=None):
        url = url or self.base_url
        self.page.goto(url)

    def click_on_form_authentication_button(self):
        form_authentication_button = self.page.get_by_role(role='link', name='Form Authentication')
        form_authentication_button.click()

    def check_if_url_was_changed_to_correct_one(self):
        assert self.page.url == self.LOGIN_URL, 'Url does not match expected url!'

    def fill_name_field(self, name='BlaBlaBla'):
        user_name_field = self.page.get_by_role(role='textbox', name='username')
        user_name_field.fill(name)

    def fill_password_field(self, password='BlaBlaBla123!'):
        password_field = self.page.get_by_role(role='textbox', name='password')
        password_field.fill(password)

    def click_on_login_button(self):
        login_button = self.page.get_by_role(role='button').filter(has_text="Login")
        login_button.click()

    def check_if_error_message_appeared(self):
        error_message = self.page.locator('#flash')
        error_text = error_message.text_content().strip().replace('\n', '').replace('×', '').strip()
        assert error_text == self.USERNAME_ERROR
