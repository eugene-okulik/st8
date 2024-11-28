from playwright.sync_api import Page
from pw_test_bstepchenko.pages.locators import sign_in_page as sign_in
from pw_test_bstepchenko.pages.base_page import BasePage
from pw_test_bstepchenko.pages.helper.randomizer import random_password, random_name, random_email


class SignInPage(BasePage):
    sign_in_url = 'https://magento.softwaretestingboard.com/customer/account/create/'

    def __init__(self, page: Page):
        super().__init__(page)
        self.password_value = None

    def open_by_url(self):
        return super().open_by_url(self.sign_in_url)

    def fill_first_name(self, name=None):
        name_element = self.find_element(sign_in.FIRST_NAME)
        if not name:
            name = random_name()
        name_element.fill(name)

    def fill_last_name(self, last_name=None):
        last_name_element = self.find_element(sign_in.LAST_NAME)
        if not last_name:
            last_name = random_name()
        last_name_element.fill(last_name)

    def fill_email(self, email=None):
        email_element = self.find_element(sign_in.EMAIL)
        if not email:
            email = random_email()
        email_element.fill(email)

    def fill_password(self, password_value=None):
        password_element = self.find_element(sign_in.PASSWORD)
        if not password_value:
            self.password_value = random_password()
        password_element.fill(self.password_value)

    def fill_correct_password_confirmation(self):
        conf_password_element = self.find_element(sign_in.CONF_PASSWORD)
        if self.password_value is not None:
            conf_password_element.fill(self.password_value)
        else:
            raise ValueError("Password has not been set. Please fill the password first.")

    def fill_incorrect_password_confirmation(self, conf_password=None):
        conf_password_element = self.find_element(sign_in.CONF_PASSWORD)
        if not conf_password:
            conf_password = random_password()
        conf_password_element.fill(conf_password)

    def fill_all_fields_with_correct_data(self):
        self.fill_first_name()
        self.fill_last_name()
        self.fill_email()
        self.fill_password()
        self.fill_correct_password_confirmation()

    def click_on_create_account_button(self):
        self.find_and_click(sign_in.CREATE_ACCOUNT_BUTTON)

    def check_error_appeared_for_all_fields(self, expected_error_message):
        first_name_error = self.find_element(sign_in.FIRST_NAME_ERROR)
        assert first_name_error.text_content() == expected_error_message

        last_name_error = self.find_element(sign_in.LAST_NAME_ERROR)
        assert last_name_error.text_content() == expected_error_message

        email_error = self.find_element(sign_in.EMAIL_ERROR)
        assert email_error.text_content() == expected_error_message

        password_error = self.find_element(sign_in.PASSWORD_ERROR)
        assert password_error.text_content() == expected_error_message

        conf_password_error = self.find_element(sign_in.CONF_PASSWORD_ERROR)
        assert conf_password_error.text_content() == expected_error_message

    def check_if_password_confirmation_error_appeared(self, expected_error_message):
        password_confirmation_error = self.find_element(sign_in.CONF_PASSWORD_ERROR)
        assert password_confirmation_error.text_content() == expected_error_message
