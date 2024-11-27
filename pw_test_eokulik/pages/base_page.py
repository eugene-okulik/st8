from playwright.sync_api import Page, expect

from abc import abstractmethod


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com/'

    def __init__(self, page: Page):
        self.page = page

    @abstractmethod
    def open_by_url(self, postfix=None):
        pass

    def find(self, locator: str):
        return self.page.locator(locator)

    def wait_until_url_changes(self):
        expect(self.page).not_to_have_url(self.page.url)

    def scroll(self, pixels=None):
        if pixels:
            self.page.mouse.wheel(0, pixels)
        else:
            self.page.keyboard.down('End')
