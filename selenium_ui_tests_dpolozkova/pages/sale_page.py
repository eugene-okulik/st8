from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait
from selenium_ui_tests_dpolozkova.pages.base_page import BasePage
from selenium_ui_tests_dpolozkova.pages.locators import sale_page as loc
from abc import abstractmethod


class SalePage(BasePage):
    def open_by_url(self, postfix=None):
        if postfix:
            self.driver.get(f'{self.base_url}{postfix}')
            WebDriverWait(self.driver, 10).until(
                element_to_be_clickable(
                    loc.DROP_DOWN_ITEMS
                )
            )
        else:
            raise TypeError('TypeError: open_by_url() in class ProductsPage requires positional argument: "postfix"')

    def check_current_url(self):
        assert self.driver.current_url == 'https://magento.softwaretestingboard.com/sale.html'

    def check_name_of_promos(self, text: list):
        headers = list(self.find_all(loc.PROMOS))
        assert headers[0].text == text[0]
        assert headers[1].text == text[1]
        assert headers[2].text == text[2]
        assert headers[3].text == text[3]
        assert headers[4].text == text[4]

    def main_button_is_clickable(self):
        self.find_and_click(loc.WOMEN_SALE)
        assert self.driver.current_url == 'https://magento.softwaretestingboard.com/promotions/women-sale.html'

    def check_home_sale_breadcrumb(self):
        breadcrumb = self.find(loc.BREADCRUMBS)
        assert breadcrumb.text == "Home Sale"
        back = self.find(loc.HOME)
        assert back.get_attribute('href') == 'https://magento.softwaretestingboard.com/'
