from selenium.webdriver.support.wait import WebDriverWait

from selenium_tests_mliaushkina.pages.base_page import BasePage
from selenium_tests_mliaushkina.pages.locators import locator_customer_create as locator
from selenium.webdriver.support import expected_conditions as ec


class CustomerCreatePage(BasePage):

    def open_page(self):
        self.open_by_url('customer/account/create/')

    def set_first_name(self, value):
        input_element = self.find(locator.FIRST_NAME)
        input_element.click()
        input_element.send_keys(value)

    def set_second_name(self, value):
        input_element = self.find(locator.SECOND_NAME)
        input_element.click()
        input_element.send_keys(value)

    def set_email(self, value):
        input_element = self.find(locator.EMAIL)
        input_element.click()
        input_element.send_keys(value)

    def set_password(self, value):
        input_element = self.find(locator.PASSWORD)
        input_element.click()
        input_element.send_keys(value)

    def set_confirm_password(self, value):
        input_element = self.find(locator.CONFIRM_PASSWORD)
        input_element.click()
        input_element.send_keys(value)

    def click_on_create_button(self):
        button_element = self.find(locator.CREATE_ACCOUNT_BUTTON)
        button_element.click()

    def check_if_success_message_visible(self):
        ui_element = self.find(locator.SUCCESS_MESSAGE)
        assert ui_element.is_displayed() is True, "Success message is not visible"

    def check_if_email_error_visible(self):
        ui_element = self.find(locator.EMAIL_ERROR)
        assert ui_element.is_displayed() is True, "Email error message is not visible"

    def check_if_confirm_password_error_visible(self):
        ui_element = self.find(locator.CONFIRM_PASSWORD_ERROR)
        assert ui_element.is_displayed() is True, "Confirm password error message is not visible"
