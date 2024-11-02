from selenium_tests_eokulik.pages.base_page import BasePage
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium_tests_eokulik.pages.locators import products_page as loc


class ProductsPage(BasePage):

    def open_by_url(self, postfix=None):
        if postfix:
            self.driver.get(f'{self.base_url}{postfix}')
            WebDriverWait(self.driver, 10).until(
                ec.text_to_be_present_in_element_attribute(
                    loc.FILTER_OPTION_TITLE,
                    'aria-expanded', 'false'
                )
            )
        else:
            raise TypeError('TypeError: open_by_url() in class ProductsPage requires positional argument: "postfix"')

    def sort_by_price(self):
        select = Select(self.find(loc.SELECT_SORTING))
        select.select_by_value('price')
        WebDriverWait(self.driver, 10).until(ec.url_contains('product_list_order=price'))

    def check_products_sorted_by_price(self):
        product_cards = self.find_all(loc.PRODUCT_CARDS)
        prices = [
            float(
                product.find_element(By.CSS_SELECTOR, '.price').text.replace('$', '')
            ) for product in product_cards
        ]
        assert prices == sorted(prices)

    def check_page_header_is_(self, text):
        assert self.find(loc.PAGE_HEADER).text == text
