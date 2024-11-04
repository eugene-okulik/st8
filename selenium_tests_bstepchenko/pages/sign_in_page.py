from selenium.webdriver.remote.webdriver import WebDriver
from selenium_tests_bstepchenko.pages.locators import sign_in_page as sign_in
from selenium_tests_bstepchenko.pages.base_page import BasePage
from selenium_tests_bstepchenko.pages.helper.randomizer import random_password, random_name, random_email


class SignInPage(BasePage):
    sign_in_url = 'https://magento.softwaretestingboard.com/customer/account/create/'

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.password_value = None

    def open_by_url(self):
        self.driver.get(self.sign_in_url)
        return self.driver.current_url

    def fill_first_name(self):
        name_element = self.find_element(sign_in.FIRST_NAME)
        name = random_name()
        name_element.send_keys(name)

    def fill_last_name(self):
        last_name_element = self.find_element(sign_in.LAST_NAME)
        last_name = random_name()
        last_name_element.send_keys(last_name)

    def fill_email(self):
        email_element = self.find_element(sign_in.EMAIL)
        email = random_email()
        email_element.send_keys(email)

    def fill_password(self):
        password_element = self.find_element(sign_in.PASSWORD)
        self.password_value = random_password()
        password_element.send_keys(self.password_value)

    def fill_correct_password_confirmation(self):
        conf_password_element = self.find_element(sign_in.CONF_PASSWORD)
        if self.password_value is not None:
            conf_password_element.send_keys(self.password_value)
        else:
            raise ValueError("Password has not been set. Please fill the password first.")

    def fill_incorrect_password_confirmation(self):
        conf_password_element = self.find_element(sign_in.CONF_PASSWORD)
        conf_password = random_password()
        conf_password_element.send_keys(conf_password)

    def fill_all_fields_with_correct_data(self):
        self.fill_first_name()
        self.fill_last_name()
        self.fill_email()
        self.fill_password()
        self.fill_correct_password_confirmation()

    def click_on_create_account_button(self):
        self.find_and_click(sign_in.CREATE_ACCOUNT_BUTTON)

    def check_error_appeared_for_all_fields(self):
        first_name_error = self.find_element(sign_in.FIRST_NAME_ERROR)
        assert first_name_error.text == 'This is a required field.'

        last_name_error = self.find_element(sign_in.LAST_NAME_ERROR)
        assert last_name_error.text == 'This is a required field.'

        email_error = self.find_element(sign_in.EMAIL_ERROR)
        assert email_error.text == 'This is a required field.'

        password_error = self.find_element(sign_in.PASSWORD_ERROR)
        assert password_error.text == 'This is a required field.'

        conf_password_error = self.find_element(sign_in.CONF_PASSWORD_ERROR)
        assert conf_password_error.text == 'This is a required field.'

    def check_if_password_confirmation_error_appeared(self):
        password_confirmation_error = self.find_element(sign_in.CONF_PASSWORD_ERROR)
        assert password_confirmation_error.text == 'Please enter the same value again.'
