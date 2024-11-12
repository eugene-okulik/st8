from playwright.sync_api import Page
from functions_for_task_one import LoginTest


def test_open_page(page: Page):
    login = LoginTest(page)
    login.open_web_page()
    login.click_on_form_authentication_button()
    login.check_if_url_was_changed_to_correct_one()

    login.fill_name_field()
    login.fill_password_field()

    login.click_on_login_button()
    login.check_if_error_message_appeared()
