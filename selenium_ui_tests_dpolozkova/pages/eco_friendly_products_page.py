from selenium.webdriver.support.wait import WebDriverWait
from selenium_ui_tests_dpolozkova.pages.base_page import BasePage
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium_ui_tests_dpolozkova.pages.locators import eco_friendly_page as loc


class EcoPage(BasePage):
    def open_by_url(self, postfix=None):
        self.driver.get(f'{self.base_url}{postfix}')

    def search_for_product_by_name(self, value):
        input = self.find(loc.SEARCH)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(input))
        input.click()
        input.send_keys(value)
        input.submit()

    def results_are_displayed(self):
        assert self.find(loc.SEARCH_RESULTS).is_displayed()

    def check_found_results(self, text):
        assert self.find(loc.FOUND_ITEM).get_attribute('alt') == text

    def apply_list_view_option(self):
        self.find(loc.LIST_VIEW).click()

    def check_grid_is_switched_to_list(self):
        assert len(self.find_all(loc.PRODUCTS_LIST)) == 10

    def sort_by_filter(self, filter=None):
        select = Select(self.find(loc.SELECT_SORTING))
        select.select_by_value(f'{filter}')
        WebDriverWait(self.driver, 10).until(ec.url_contains(f'product_list_order={filter}'))
        self.find_all(loc.PRODUCTS_LIST)

    def check_products_sorted_by_price(self):
        product_cards = self.find_all(loc.PRODUCTS_LIST)
        prices = [
            float(
                product.find_element(By.CSS_SELECTOR, '.price').text.replace('$', '')
            ) for product in product_cards
        ]
        assert prices == sorted(prices)
