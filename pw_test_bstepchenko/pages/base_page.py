from playwright.sync_api import Page, expect
from pw_test_bstepchenko.pages.locators.sign_in_page import CONSENT_BUTTON


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def open_by_url(self, url):
        self.page.goto(url)
        self.click_on_consent_button()
        return self.page.url

    def find_element(self, locator: str, parent=None):
        context = parent if parent else self.page
        return context.locator(locator)

    def find_all_elements(self, locator: str, timeout=20000):
        self.page.wait_for_selector(locator, timeout=timeout)
        elements = self.page.locator(locator).all()
        visible_elements = [element for element in elements if element.is_visible()]
        return visible_elements

    def find_and_click(self, locator, timeout=20000):
        self.page.wait_for_selector(locator, timeout=timeout)
        element = self.page.locator(locator)
        element.click()

    def wait_until_url_changes(self):
        expect(self.page).not_to_have_url(self.page.url)

    def check_url_was_not_changed(self, previous_url: str):
        current_url = self.page.url
        assert current_url == previous_url, "URL has changed!"

    def check_url_was_changed(self, previous_url: str):
        current_url = self.page.url
        assert current_url != previous_url, "URL has NOT changed!"

    def click_on_consent_button(self):
        self.page.wait_for_selector(CONSENT_BUTTON)
        try:
            self.find_and_click(CONSENT_BUTTON)
        except Exception as e:
            print("Consent button not found or not clickable:", e)
            pass
