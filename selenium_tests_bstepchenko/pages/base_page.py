from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, locator: tuple, timeout=20, parent=None):
        context = parent if parent else self.driver
        element = WebDriverWait(context, timeout).until(ec.visibility_of_element_located(locator))
        return element

    def find_all_elements(self, locator: tuple, timeout=20):
        WebDriverWait(self.driver, timeout).until(ec.presence_of_all_elements_located(locator))
        elements = self.driver.find_elements(*locator)
        visible_elements = [element for element in elements if element.is_displayed()]
        return visible_elements

    def find_and_click(self, locator: tuple, timeout=20):
        element = self.find_element(locator)
        WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(element))
        element.click()

    def wait_until_url_changes(self, timeout=20):
        WebDriverWait(self.driver, timeout).until(ec.url_changes(self.driver.current_url))

    def check_url_was_not_changed(self, previous_url: str):
        current_url = self.driver.current_url
        assert current_url == previous_url, "URL has changed!"

    def check_url_was_changed(self, previous_url: str):
        current_url = self.driver.current_url
        assert current_url != previous_url, "URL has NOT changed!"
