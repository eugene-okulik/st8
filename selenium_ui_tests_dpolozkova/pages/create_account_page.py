from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium_ui_tests_dpolozkova.pages.base_page import BasePage
from selenium_ui_tests_dpolozkova.pages.locators import account_page as loc


class AccountPage(BasePage):
    def open_by_url(self, postfix=None):
        self.driver.get(f'{self.base_url}{postfix}')
        self.driver.implicitly_wait(10)

    def check_success_message_is_displayed(self):
        assert self.find(loc.SUCCESS_MSG).is_displayed()

    def hint_for_required_fields_is_displayed(self, text):
        assert self.find(loc.FIRST_NAME_ERROR).text == text
        assert self.find(loc.LAST_NAME_ERROR).text == text
        assert self.find(loc.EMAIL_ERROR).text == text
        assert self.find(loc.PWD_ERROR).text == text
        assert self.find(loc.PWD_CONFIRM_ERROR).text == text

    def validation_hint_for_email_is_displayed(self, text):
        assert self.find(loc.EMAIL_ERROR).text == text

    def fill_first_name(self, value):
        first_name = self.find(loc.FIRST_NAME)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(first_name))
        first_name.click()
        first_name.send_keys(value)

    def fill_second_name(self, value):
        second_name = self.find(loc.LAST_NAME)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(second_name))
        second_name.click()
        second_name.send_keys(value)

    def fill_email(self, value):
        email = self.find(loc.EMAIL)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(email))
        email.click()
        email.send_keys(value)

    def fill_password(self, PWD):
        password = self.find(loc.PWD)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(password))
        password.click()
        password.send_keys(PWD)

    def fill_confirm_password(self, PWD):
        confirm_pwd = self.find(loc.CONFIRM_PWD)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(confirm_pwd))
        confirm_pwd.click()
        confirm_pwd.send_keys(PWD)

    def click_create_account_button(self):
        create_account = self.find(loc.CREATE_ACCOUNT_BTN)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(create_account))
        create_account.click()
