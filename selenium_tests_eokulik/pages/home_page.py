from selenium_tests_eokulik.pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium_tests_eokulik.pages.locators import home_page as loc


class HomePage(BasePage):
    def open_by_url(self, postfix=None):
        self.driver.get(self.base_url)

    def open_men_jackets_from_menu(self):
        self.driver.get('https://magento.softwaretestingboard.com/')
        men = self.find(loc.MEN)
        tops = self.find(loc.TOPS)
        jackets = self.find(loc.JACKETS)
        ActionChains(self.driver).move_to_element(men).move_to_element(tops).click(jackets).perform()
        # self.wait_until_url_changes()
