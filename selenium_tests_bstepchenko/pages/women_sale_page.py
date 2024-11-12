from selenium_tests_bstepchenko.pages.base_page import BasePage
from selenium_tests_bstepchenko.pages.locators import women_sale


class WomenSale(BasePage):
    women_sale_page = 'https://magento.softwaretestingboard.com/promotions/women-sale.html'

    def open_by_url(self):
        self.driver.get(self.women_sale_page)
        return self.driver.current_url

    def check_if_page_title_is_displayed(self, expected_title_text):
        title = self.find_element(women_sale.WOMEN_SALE_TITLE)
        assert title.text == expected_title_text
