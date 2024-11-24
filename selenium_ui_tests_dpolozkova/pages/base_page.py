from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from abc import abstractmethod


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com/'

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @abstractmethod
    def open_by_url(self):
        pass

    def find(self, locator: tuple):
        element = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(locator))
        return element

    def find_and_click(self, locator: tuple):
        element = self.find(locator)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(element))
        element.click()

    def find_all(self, locator: tuple):
        return self.driver.find_elements(*locator)

    def scroll(self, pixels=None):
        if pixels:
            self.driver.execute_script(f'window.scrollBy(0,{pixels})')
        else:
            #scroll to bottom of the page
            self.driver.execute_script(f'window.scrollBy(0,document.body.scrollHeight)')

    def fill_input(self, locator: tuple, value):
        input = self.find(locator)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(input))
        input.click()
        input.send_keys(value)

