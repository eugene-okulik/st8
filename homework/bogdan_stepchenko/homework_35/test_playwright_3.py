from playwright.sync_api import Page, BrowserContext
from functions_for_task_one import Alert
from functions_for_task_two import ChangingPage


def test_closing_alert(page: Page):
    alert = Alert(page)
    alert.open_web_page()
    alert.click_on_button()
    alert.check_if_text_correct()


def test_changing_page(page: Page, context: BrowserContext):
    new_page = ChangingPage(page)
    new_page.open_web_page()
    new_page.click_on_new_tab_button()
    new_page.check_if_new_tab_contain_correct_text(context)
    new_page.check_if_new_tab_button_is_active()
