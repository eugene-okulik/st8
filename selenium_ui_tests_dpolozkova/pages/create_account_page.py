from selenium_ui_tests_dpolozkova.pages.base_page import BasePage
from selenium_ui_tests_dpolozkova.pages.locators import account_page as loc


class AccountPage(BasePage):
    def open_by_url(self, postfix=None):
        self.driver.get(f'{self.base_url}{postfix}')
        self.driver.implicitly_wait(10)

    def check_success_message_is_displayed(self):
        assert self.find(loc.SUCCESS_MSG).is_displayed()

    def hint_for_required_field_is_displayed(self, field, text):
        assert self.find(field).text == text

    def validation_hint_for_email_is_displayed(self):
        assert self.find(loc.EMAIL_ERROR).text == 'Please enter a valid email address (Ex: johndoe@domain.com).'
