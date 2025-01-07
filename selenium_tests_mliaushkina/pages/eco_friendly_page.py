import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from selenium_tests_mliaushkina.pages.base_page import BasePage
from selenium_tests_mliaushkina.pages.locators import locator_eco_friendly as locator
from selenium.webdriver.support import expected_conditions as ec


class EcoFriendlyPage(BasePage):

    def open_page(self):
        self.open_by_url('collections/eco-friendly.html')

    def check_product_count(self, value):
        all_products = self.find_all_elements(locator.PRODUCT_ITEM)
        product_count = len(all_products)
        assert product_count == value, "Invalid product count"

    def change_product_count(self, value: str):
        select_ui_element = self.find(locator.PRODUCT_COUNT_SELECT)
        actions = ActionChains(self.driver)
        actions.move_to_element(select_ui_element).perform()
        select_ui_element.click()
        options = select_ui_element.find_elements(By.TAG_NAME, "option")
        for option in options:
            if option.get_attribute("value") == value:
                option.click()
                if value == "12":
                    WebDriverWait(self.driver, 10).until(ec.url_contains('eco-friendly.html'))
                else:
                    WebDriverWait(self.driver, 10).until(ec.url_contains(f'product_list_limit={value}'))
                break

    def check_is_grid_view(self):
        div_grid = self.find(locator.DIV_GRID_ITEM)
        assert div_grid is not None, "Invalid grid view item"

    def check_is_list_view(self):
        div_list = self.find(locator.DIV_LIST_ITEM)
        assert div_list is not None, "Invalid list view item"

    def change_to_list_view(self):
        switch_a = self.find(locator.SWITCH_A_ITEM)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(switch_a))
        actions = ActionChains(self.driver)
        actions.move_to_element(switch_a).perform()
        switch_a.click()
        WebDriverWait(self.driver, 10).until(ec.url_contains('product_list_mode=list'))

    def change_sort_by_price_asc(self):
        select_ui_element = self.find(locator.PRODUCT_SORT_SELECT)
        actions = ActionChains(self.driver)
        actions.move_to_element(select_ui_element).perform()
        select_ui_element.click()
        options = select_ui_element.find_elements(By.TAG_NAME, "option")
        for option in options:
            if option.get_attribute("value") == "price":
                option.click()
                WebDriverWait(self.driver, 10).until(ec.url_contains('product_list_order=price'))
                break

    def check_if_prices_are_asc(self):
        product_price_list = []
        sort_price_list = []
        all_product_price_spans = self.find_all_elements(locator.PRODUCT_ITEM_PRICE)
        for one_product_price_span in all_product_price_spans:
            price_amount = one_product_price_span.get_attribute("data-price-amount")
            product_price_list.append(price_amount)
            sort_price_list.append(price_amount)

        sorted(sort_price_list)
        assert product_price_list == sort_price_list, "Lists are not equal"

    def change_sort_by_price_desc(self):
        select_ui_element = self.find(locator.SORT_ARROW_SELECT)
        actions = ActionChains(self.driver)
        actions.move_to_element(select_ui_element).perform()
        select_ui_element.click()
        WebDriverWait(self.driver, 10).until(ec.url_contains('product_list_dir=desc'))

    def check_if_prices_are_desc(self):
        product_price_list = []
        sort_price_list = []
        all_product_price_spans = self.find_all_elements(locator.PRODUCT_ITEM_PRICE)
        for one_product_price_span in all_product_price_spans:
            price_amount = one_product_price_span.get_attribute("data-price-amount")
            product_price_list.append(price_amount)
            sort_price_list.append(price_amount)

        sorted(sort_price_list, reverse=True)
        assert product_price_list == sort_price_list, "Lists are not equal"
