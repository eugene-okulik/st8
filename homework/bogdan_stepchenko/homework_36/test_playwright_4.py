from playwright.sync_api import Page
from functions_for_task_one import LogInWithoutCreds


def test_error_message_at_login_with_incorrect_creds(page: Page):
    login = LogInWithoutCreds(page)
    login.open_web_page()
    login.open_login_screen()
    login.login_with_incorrect_creds('blabla_name', 'blabla_password')
    login.check_if_error_message_correct()
