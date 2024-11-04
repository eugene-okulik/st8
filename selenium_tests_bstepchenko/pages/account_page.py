from selenium_tests_bstepchenko.pages.locators import account_page as account
from selenium_tests_bstepchenko.pages.base_page import BasePage


class AccountPage(BasePage):
    account_url = 'https://magento.softwaretestingboard.com/customer/account/'

    def open_by_url(self):
        self.driver.get(self.account_url)
        return self.driver.current_url

    def check_success_message_appeared(self):
        success_message = self.find_element(account.SUCCESS_MESSAGE)
        assert success_message.text == 'Thank you for registering with Main Website Store.'
