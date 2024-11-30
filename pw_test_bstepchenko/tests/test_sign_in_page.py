from pw_test_bstepchenko.pages.helper.text_to_check import SUCCESS_REG_TEXT
from pw_test_bstepchenko.pages.helper.text_to_check import REQUIRED_FIELD_TEXT, PSWRD_CONFIRMATION_ERROR_TEXT


def test_impossible_to_create_account_without_data(pw_sign_in_page):
    url = pw_sign_in_page.open_by_url()
    pw_sign_in_page.click_on_create_account_button()
    pw_sign_in_page.check_error_appeared_for_all_fields(REQUIRED_FIELD_TEXT)
    pw_sign_in_page.check_url_was_not_changed(url)


def test_account_creation_with_incorrect_password_confirmation(pw_sign_in_page):
    pw_sign_in_page.open_by_url()
    pw_sign_in_page.fill_first_name()
    pw_sign_in_page.fill_last_name()
    pw_sign_in_page.fill_email()
    pw_sign_in_page.fill_password()
    pw_sign_in_page.fill_incorrect_password_confirmation()
    pw_sign_in_page.click_on_create_account_button()
    pw_sign_in_page.check_if_password_confirmation_error_appeared(PSWRD_CONFIRMATION_ERROR_TEXT)


def test_correct_account_creation(pw_sign_in_page, pw_account_page):
    url = pw_sign_in_page.open_by_url()
    pw_sign_in_page.fill_all_fields_with_correct_data()
    pw_sign_in_page.click_on_create_account_button()
    pw_account_page.check_url_was_changed(url)
    pw_account_page.check_success_message_appeared(SUCCESS_REG_TEXT)
