from abc import abstractmethod
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com/'

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_by_url(self, postfix=None):
        self.driver.get(f'{self.base_url}{postfix}')

    @abstractmethod
    def open_page(self):
        pass

    def find(self, locator: tuple[str, str], parent=None):
        used_parent = parent
        if used_parent is None:
            used_parent = self.driver

        element = WebDriverWait(used_parent, 20).until(ec.presence_of_element_located(locator))
        return element

    def find_all_elements(self, locator: tuple[str, str]):
        WebDriverWait(self.driver, 20).until(ec.presence_of_all_elements_located(locator))
        elements = self.driver.find_elements(*locator)
        return elements
