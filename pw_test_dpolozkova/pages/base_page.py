from playwright.sync_api import Page
from abc import abstractmethod


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com/'

    def __init__(self, page: Page):
        self.page = page

    @abstractmethod
    def open_by_url(self):
        pass

    def find(self, locator: str):
        return self.page.locator(locator)

    def scroll(self, pixels=None):
        if pixels:
            self.page.mouse.wheel(0,pixels)
        else:
            # scroll to bottom of the page
            self.page.keyboard.down('End')

    def fill_input(self, locator: str, value):
        self.find(locator).fill(value)
