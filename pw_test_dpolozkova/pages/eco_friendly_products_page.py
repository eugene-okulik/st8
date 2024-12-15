from playwright.sync_api import expect

from pw_test_dpolozkova.pages.base_page import BasePage
from pw_test_dpolozkova.pages.locators import eco_friendly_page as loc
import re


class EcoPage(BasePage):
    def open_by_url(self, postfix=None):
        self.page.goto(f'{self.base_url}{postfix}')

    def search_for_product_by_name(self, value):
        input = self.find(loc.SEARCH)
        input.press_sequentially(value)
        input.press('Enter')

    def results_are_displayed(self):
        expect(self.find(loc.SEARCH_RESULTS)).to_be_visible()

    def check_found_results(self, text):
        results = self.find(loc.FOUND_ITEM).get_attribute('alt')
        assert results == text

    def apply_list_view_option(self):
        list_view = self.find(loc.LIST_VIEW).nth(0)
        list_view.click()

    def check_grid_is_switched_to_list(self):
        list_len = len(self.find(loc.PRODUCTS_LIST).all())
        expect(self.page).to_have_url(re.compile(f"product_list_mode=list$"), timeout=20000)
        assert list_len == 10

    def sort_by_filter(self, filter=None):
        self.find(loc.SELECT_SORTING).first.press_sequentially(f"{filter}")
        expect(self.page).to_have_url(re.compile(f"product_list_order={filter}"), timeout=5000)

    def check_products_sorted_by_price(self):
        product_cards = self.find(loc.PRODUCTS_LIST).all()
        prices = [
            float(
                product.locator('.price').text_content().replace('$', '')
            ) for product in product_cards
        ]
        assert prices == sorted(prices)
