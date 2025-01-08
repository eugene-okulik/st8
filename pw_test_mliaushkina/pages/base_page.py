from abc import abstractmethod
from playwright.sync_api import Page


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com/'

    def __init__(self, page: Page):
        self.page = page

    def open_by_url(self, postfix=None):
        self.page.goto(f'{self.base_url}{postfix}')

    @abstractmethod
    def open_page(self):
        pass

    def find(self, locator: str):
        self.page.wait_for_selector(locator, timeout=10000)
        element = self.page.locator(locator)
        return element

    def find_all_elements(self, locator: str):
        self.page.wait_for_selector(locator, timeout=20000)
        elements = self.page.locator(locator).all()
        visible_elements = [element for element in elements if element.is_visible()]
        return visible_elements
