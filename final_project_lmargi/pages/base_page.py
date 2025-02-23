from abc import abstractmethod
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from final_project_lmargi.pages.locators import locator_base as locator
from final_project_lmargi.pages.const import const_base_page as const


class BasePage:
    base_url = const.BASE_URL

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_by_url(self, postfix=None):
        self.driver.get(f'{self.base_url}{postfix}')

    @abstractmethod
    def open_page(self):
        pass

    def cookie_accept(self):
        cookie_element = self.find(locator.COOKIE_ELEMENT)
        cookie_element.click()
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(cookie_element))

    def find(self, locator: tuple[str, str], parent=None):
        used_parent = parent
        if used_parent is None:
            used_parent = self.driver

        element = WebDriverWait(used_parent, 20).until(ec.presence_of_element_located(locator))
        return element

    def find_clickable(self, locator: tuple[str, str], parent=None):
        used_parent = parent
        if used_parent is None:
            used_parent = self.driver

        element = WebDriverWait(used_parent, 20).until(ec.element_to_be_clickable(locator))
        return element

    def find_all_elements(self, locator: tuple[str, str]):
        WebDriverWait(self.driver, 20).until(ec.presence_of_all_elements_located(locator))
        elements = self.driver.find_elements(*locator)
        return elements
