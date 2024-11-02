from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from abc import abstractmethod


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com/'

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @abstractmethod
    def open_by_url(self, postfix=None):
        pass

    def find(self, locator: tuple):
        element = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(locator))
        return element

    def find_all(self, locator: tuple):
        return self.driver.find_elements(*locator)

    def find_and_click(self, locator: tuple):
        element = self.find(locator)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(element))
        element.click()

    def wait_until_url_changes(self):
        WebDriverWait(self.driver, 10).until(ec.url_changes(self.driver.current_url))

    def scroll(self, pixels=None):
        if pixels:
            self.driver.execute_script(f'window.scrollBy(0, {pixels})')
        else:
            self.driver.execute_script('window.scrollBy(0, document.body.scrollHeight)')
