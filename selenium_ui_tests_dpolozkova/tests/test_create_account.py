from selenium_ui_tests_dpolozkova.pages.locators import account_page as loc


def test_create_new_customer_account(account_page):
    account_page.open_by_url('customer/account/create/')
    account_page.scroll()
    account_page.find(loc.FIRST_NAME)
    account_page.fill_input(loc.FIRST_NAME, 'Etofirstname')
    account_page.fill_input(loc.LAST_NAME, 'Etosecondname')
    account_page.fill_input(loc.EMAIL, 'qatestname12345@qa.com')
    account_page.fill_input(loc.PWD, 'qwerty123!1')
    account_page.fill_input(loc.CONFIRM_PWD, 'qwerty123!1')
    account_page.find_and_click(loc.CREATE_ACCOUNT_BTN)
    account_page.check_success_message_is_displayed()


def test_required_fields(account_page):
    account_page.open_by_url('customer/account/create/')
    account_page.scroll()
    account_page.find_and_click(loc.CREATE_ACCOUNT_BTN)
    account_page.hint_for_required_field_is_displayed(loc.FIRST_NAME_ERROR, 'This is a required field.')
    account_page.hint_for_required_field_is_displayed(loc.LAST_NAME_ERROR, 'This is a required field.')
    account_page.hint_for_required_field_is_displayed(loc.EMAIL_ERROR, 'This is a required field.')
    account_page.hint_for_required_field_is_displayed(loc.PWD_ERROR, 'This is a required field.')
    account_page.hint_for_required_field_is_displayed(loc.PWD_CONFIRM_ERROR, 'This is a required field.')


def test_fields_validation(account_page):
    account_page.open_by_url('customer/account/create/')
    account_page.fill_input(loc.EMAIL, 'abcABC')
    account_page.scroll()
    account_page.find_and_click(loc.CREATE_ACCOUNT_BTN)
    account_page.validation_hint_for_email_is_displayed()
