from playwright.sync_api import expect

from pw_test_dpolozkova.pages.base_page import BasePage
from pw_test_dpolozkova.pages.locators import account_page as loc


class AccountPage(BasePage):
    def open_by_url(self, postfix=None):
        self.page.goto(f'{self.base_url}{postfix}')

    def check_success_message_is_displayed(self):
        expect(self.find(loc.SUCCESS_MSG)).to_be_visible()

    def hint_for_required_fields_is_displayed(self, text):
        expect(self.find(loc.FIRST_NAME_ERROR)).to_have_text(text)
        expect(self.find(loc.LAST_NAME_ERROR)).to_have_text(text)
        expect(self.find(loc.EMAIL_ERROR)).to_have_text(text)
        expect(self.find(loc.PWD_ERROR)).to_have_text(text)
        expect(self.find(loc.PWD_CONFIRM_ERROR)).to_have_text(text)

    def validation_hint_for_email_is_displayed(self, text):
        expect(self.find(loc.EMAIL_ERROR)).to_have_text(text)

    def fill_first_name(self, value):
        first_name = self.find(loc.FIRST_NAME)
        first_name.fill(value)

    def fill_second_name(self, value):
        second_name = self.find(loc.LAST_NAME)
        second_name.fill(value)

    def fill_email(self, value):
        email = self.find(loc.EMAIL)
        email.fill(value)

    def fill_password(self, PWD):
        password = self.find(loc.PWD)
        password.fill(PWD)

    def fill_confirm_password(self, PWD):
        confirm_pwd = self.find(loc.CONFIRM_PWD)
        confirm_pwd.fill(PWD)

    def click_create_account_button(self):
        create_account = self.find(loc.CREATE_ACCOUNT_BTN)
        create_account.click()
