from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_tests_bstepchenko.pages.base_page import BasePage
from selenium_tests_bstepchenko.pages.locators import collections_eco_friendly_page as eco_friendly


class EcoFriendly(BasePage):
    eco_friendly_url = 'https://magento.softwaretestingboard.com/collections/eco-friendly.html'

    def open_by_url(self):
        self.driver.get(self.eco_friendly_url)
        return self.driver.current_url

    def change_products_view_to_list(self):
        list_view_button = self.find_element(eco_friendly.LIST_VIEW_BUTTON)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(list_view_button))
        list_view_button.click()
        WebDriverWait(self.driver, 10).until(EC.url_contains('product_list_mode=list'))

    def check_that_number_of_displayed_products_in_counter_is(self, number):
        current_products_in_category_element = self.find_element(eco_friendly.DEFAULT_PRODUCT_QUANTITY)
        print(current_products_in_category_element.text)
        assert current_products_in_category_element.text == str(number)

    def get_quantity_product_cards_on_page(self):
        all_product_cards_on_page_element = self.find_all_elements(eco_friendly.PRODUCT_CARD)
        number_of_product_cards = len(all_product_cards_on_page_element)
        return number_of_product_cards

    def check_that_quantity_product_cards_on_screen_is(self, number):
        all_product_cards = self.get_quantity_product_cards_on_page()
        assert all_product_cards == number

    def open_color_dropdown_and_select_white_color(self):
        color_dropdown = self.find_element(eco_friendly.COLOR_DROPDOWN)
        color_dropdown.click()
        self.find_element(eco_friendly.LIST_OF_COLORS_IN_DROPDOWN)
        white_color = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(eco_friendly.WHITE_COLOR_IN_DROPDOWN))
        self.driver.execute_script("arguments[0].click();", white_color)
        WebDriverWait(self.driver, 10).until(EC.url_contains('color=59'))

    def check_that_all_products_has_white_color(self):
        product_cards = self.find_all_elements(eco_friendly.PRODUCT_CARD)
        for card in product_cards:
            white_color = card.find_elements(*eco_friendly.WHITE_COLOR_INSIDE_PRODUCT_CARD)
            assert len(white_color) > 0

    def check_counter_has_correct_value_of_founded_cards(self):
        product_cards = self.find_all_elements(eco_friendly.PRODUCT_CARD)
        founded_cards_with_white_color = self.find_element(eco_friendly.ALL_PRODUCTS_QUANTITY).text
        assert str(len(product_cards)) == founded_cards_with_white_color

    def open_selector_and_choose_24(self):
        drop_down_per_page = self.find_element(eco_friendly.SELECTOR)
        select = Select(drop_down_per_page)
        select.select_by_value('24')
        WebDriverWait(self.driver, 10).until(EC.url_contains('product_list_limit=24'))
