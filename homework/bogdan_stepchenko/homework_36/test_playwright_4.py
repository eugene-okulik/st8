from playwright.sync_api import Page
from functions_for_task_one import LogInWithoutCreds
from functions_for_task_two import CheckChangedTitle
from time import sleep


def test_error_message_at_login_with_incorrect_creds(page: Page):
    login = LogInWithoutCreds(page)
    login.open_web_page()
    login.open_login_screen()
    login.login_with_incorrect_creds('blabla_name', 'blabla_password')
    login.check_if_error_message_correct()


def test_if_card_title_correct(page: Page):
    card = CheckChangedTitle(page)
    card.change_phone_name_in_request()
    card.click_on_first_card()
    card.check_if_title_in_popup_is_correct()
    card.check_if_button_name_contains_changed_phone_name()
