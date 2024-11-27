from pw_test_eokulik.pages.base_page import BasePage
from pw_test_eokulik.pages.locators import home_page as loc


class HomePage(BasePage):
    def open_by_url(self, postfix=None):
        self.page.goto(self.base_url)

    def open_men_jackets_from_menu(self):
        # self.driver.get('https://magento.softwaretestingboard.com/')
        self.find(loc.MEN).hover()
        self.find(loc.TOPS).hover()
        self.find(loc.JACKETS).click()
        # self.wait_until_url_changes()
