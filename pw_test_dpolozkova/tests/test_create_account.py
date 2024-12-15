def test_create_new_customer_account(account_page):
    account_page.open_by_url('customer/account/create/')
    account_page.scroll()
    account_page.fill_first_name('John')
    account_page.fill_second_name('Doe')
    account_page.fill_email('doejohn12@qa.com')
    account_page.fill_password('qwerty12312312!')
    account_page.fill_confirm_password('qwerty12312312!')
    account_page.click_create_account_button()
    account_page.check_success_message_is_displayed()


def test_required_fields(account_page):
    account_page.open_by_url('customer/account/create/')
    account_page.scroll()
    account_page.click_create_account_button()
    account_page.hint_for_required_fields_is_displayed('This is a required field.')


def test_fields_validation(account_page):
    account_page.open_by_url('customer/account/create/')
    account_page.fill_email('abcABC')
    account_page.scroll()
    account_page.click_create_account_button()
    account_page.validation_hint_for_email_is_displayed('Please enter a valid email address (Ex: johndoe@domain.com).')
