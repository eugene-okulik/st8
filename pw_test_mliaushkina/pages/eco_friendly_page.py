import re
import time

from pw_test_mliaushkina.pages.base_page import BasePage
from pw_test_mliaushkina.pages.locators import locator_eco_friendly as loc_const
from playwright.sync_api import expect


class EcoFriendlyPage(BasePage):

    def open_page(self):
        self.open_by_url('collections/eco-friendly.html')
        self.page.reload()

    def search_by_name(self, product_name):
        search_input = self.find(loc_const.PRODUCT_SEARCH)
        search_input.press_sequentially(product_name)
        search_input.press('Enter')
        expect(self.page).to_have_url(re.compile(r".*/catalogsearch"), timeout=5000)

    def check_if_product_found(self, product_title: str):
        is_found_product = False
        founded_products = self.find(loc_const.PRODUCT_FOUND_TITLE).all()
        for one_product in founded_products:
            one_product_name = one_product.inner_text().strip()
            if one_product_name == product_title:
                is_found_product = True
                break

        assert is_found_product is True, "Product not found"

    def check_is_grid_view(self):
        div_grid = self.find(loc_const.DIV_GRID_ITEM)
        assert div_grid is not None, "Invalid grid view item"

    def check_is_list_view(self):
        div_list = self.find(loc_const.DIV_LIST_ITEM)
        assert div_list is not None, "Invalid list view item"

    def change_to_list_view(self):
        switch_a = self.find(loc_const.SWITCH_A_ITEM).first
        switch_a.click()
        expect(self.page).to_have_url(re.compile("product_list_mode=list"), timeout=5000)

    def change_sort_by_price_asc(self):
        select_ui_element = self.find(loc_const.PRODUCT_SORT_SELECT).first
        select_ui_element.select_option('price')
        expect(self.page).to_have_url(re.compile('product_list_order=price'), timeout=10000)

    def check_if_prices_are_asc(self):
        product_price_list = []
        sort_price_list = []
        all_product_price_spans = self.find_all_elements(loc_const.PRODUCT_ITEM_PRICE)
        for one_product_price_span in all_product_price_spans:
            price_amount = one_product_price_span.get_attribute("data-price-amount")
            product_price_list.append(price_amount)
            sort_price_list.append(price_amount)

        sorted(sort_price_list)
        assert product_price_list == sort_price_list, "Lists are not equal"

    def change_sort_by_price_desc(self):
        select_ui_element = self.find(loc_const.SORT_ARROW_SELECT).first
        select_ui_element.click()
        expect(self.page).to_have_url(re.compile('product_list_dir=desc'), timeout=10000)

    def check_if_prices_are_desc(self):
        product_price_list = []
        sort_price_list = []
        all_product_price_spans = self.find_all_elements(loc_const.PRODUCT_ITEM_PRICE)
        for one_product_price_span in all_product_price_spans:
            price_amount = one_product_price_span.get_attribute("data-price-amount")
            product_price_list.append(price_amount)
            sort_price_list.append(price_amount)

        sorted(sort_price_list, reverse=True)
        assert product_price_list == sort_price_list, "Lists are not equal"
