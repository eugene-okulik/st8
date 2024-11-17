from re import compile
from playwright.sync_api import Page, expect


class ColorChangeButton:
    URL = 'https://demoqa.com/dynamic-properties'
    BUTTON_NAME = 'Color Change'

    def __init__(self, page: Page, base_url=URL):
        self.page = page
        self.base_url = base_url

    def open_web_page(self):
        self.page.goto(self.base_url)

    def wait_for_button_is_colored(self):
        color_change_button = self.page.get_by_role('button', name=self.BUTTON_NAME)
        expect(color_change_button).to_have_class(compile(r".*\btext-danger\b.*"), timeout=10000)

    def click_on_button(self):
        color_change_button = self.page.get_by_role('button', name=self.BUTTON_NAME)
        color_change_button.click()
