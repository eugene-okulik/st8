from playwright.sync_api import Page, expect
from abc import abstractmethod
from pw_test_msorokin.config.links import Links


class BasePage:
    base_url = Links.HOME_PAGE_URL

    def __init__(self, page: Page):
        self.page = page

    @abstractmethod
    def open_by_url(self, postfix=None):
        pass

    def find_element(self, locator: str):
        return self.page.locator(locator)

    def find_elements(self, locator: str):
        return self.page.locator(locator).all()

    def wait_until_url_changes(self):
        expect(self.page).not_to_have_url(self.page.url)

    def scroll(self, pixels=None):
        if pixels:
            self.page.mouse.wheel(0, pixels)
        else:
            self.page.keyboard.down('End')

    def scroll_to_element(self, locator: str):
        element = self.page.locator(locator)
        element.scroll_into_view_if_needed()

    def get_links_from_elements(self, locator: str):
        elements = self.page.locator(locator)
        links = elements.evaluate_all("els => els.map(el => el.href)")
        return links
