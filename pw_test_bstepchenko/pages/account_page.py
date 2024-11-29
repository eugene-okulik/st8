from pw_test_bstepchenko.pages.locators import account_page as account
from pw_test_bstepchenko.pages.base_page import BasePage


class AccountPage(BasePage):
    account_url = 'https://magento.softwaretestingboard.com/customer/account/'

    def open_by_url(self, url=None):
        return super().open_by_url(self.account_url)

    def check_success_message_appeared(self, expected_error_message):
        success_message = self.find_element(account.SUCCESS_MESSAGE)
        assert success_message.text_content() == expected_error_message
