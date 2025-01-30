from final_project_lmargi.pages.base_page import BasePage
from final_project_lmargi.pages.locators import locator_login as locator
from final_project_lmargi.pages.const import const_login as const


class LoginPage(BasePage):

    def open_page(self):
        self.open_by_url('login')

    def click_on_phone_button(self):
        input_radiobutton = self.find(locator.BUTTON_WITH_PHONE)
        input_radiobutton.click()

    def click_on_email_button(self):
        email_radiobutton = self.find(locator.BUTTON_WITH_EMAIL)
        email_radiobutton.click()

    def set_phone(self, value):
        input_element = self.find(locator.EMAIL_INPUT)
        input_element.click()
        input_element.send_keys(value)

    def set_password(self, value):
        input_element = self.find(locator.PASSWORD)
        input_element.click()
        input_element.send_keys(value)

    def click_on_submit_button(self):
        button_element = self.find(locator.BUTTON_SUBMIT)
        button_element.click()

    def click_on_logout_button(self):
        button_element = self.find(locator.LOGOUT_BUTTON)
        button_element.click()


    def check_account_name_visible(self):
        account_name =  self.find(locator.ACCOUNT_NAME)
        return  account_name

    def check_login_button_visible(self):
        login_button = self.find(locator.LOGIN_BUTTON)
        return login_button

    def check_if_radiobutton_error_visible(self):
        error_message_metod = self.find(locator.ERROR_MESSAGE_INVALID_METHOD)
        return error_message_metod

    def check_login_failed_message(self):
        error_message_login = self.find(locator.LOGIN_ERROR_MESSAGE)
        return error_message_login


    def check_invalid_phone_message(self):
        error_message_phone = self.find(locator.ERROR_MESSAGE_INVALID_PHONE)
        return error_message_phone

    def check_invalid_password_message(self):
        error_message_passw = self.find(locator.ERROR_MESSAGE_INVALID_PASSW)
        return error_message_passw

    def make_login(self):
        self.open_page()
        self.cookie_accept()
        self.click_on_phone_button()
        self.set_phone(const.LOGIN_PHONE)
        self.set_password(const.PASSWORD)
        self.click_on_submit_button()
