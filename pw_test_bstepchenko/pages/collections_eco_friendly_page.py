import re
from playwright.sync_api import expect
from pw_test_bstepchenko.pages.base_page import BasePage
from pw_test_bstepchenko.pages.locators import collections_eco_friendly_page as eco_friendly


class EcoFriendly(BasePage):
    eco_friendly_url = 'https://magento.softwaretestingboard.com/collections/eco-friendly.html'

    def open_by_url(self):
        return super().open_by_url(self.eco_friendly_url)

    def change_products_view_to_list(self):
        list_view_button = self.find_element(eco_friendly.LIST_VIEW_BUTTON).nth(0)
        list_view_button.click()
        expect(self.page).to_have_url(re.compile('product_list_mode=list$'), timeout=20000)

    def check_that_number_of_displayed_products_in_counter_is(self, number):
        current_products_in_category_element = self.find_element(eco_friendly.DEFAULT_PRODUCT_QUANTITY).nth(1)
        assert current_products_in_category_element.text_content() == str(number)

    def get_quantity_product_cards_on_page(self):
        self.page.wait_for_selector(eco_friendly.PRODUCT_CARD, timeout=20000)
        all_product_cards_on_page_element = self.find_all_elements(eco_friendly.PRODUCT_CARD)
        number_of_product_cards = len(all_product_cards_on_page_element)
        return number_of_product_cards

    def check_that_quantity_product_cards_on_screen_is(self, number):
        all_product_cards = self.get_quantity_product_cards_on_page()
        assert all_product_cards == number

    def open_color_dropdown_and_select_white_color(self):
        color_dropdown = self.find_element(eco_friendly.COLOR_DROPDOWN)
        color_dropdown.click()
        white_color = self.page.locator(eco_friendly.WHITE_COLOR_IN_DROPDOWN)
        white_color.wait_for(state="visible", timeout=20000)
        white_color.click()
        expect(self.page).to_have_url(re.compile('color=59$'), timeout=20000)

    def check_that_all_products_has_white_color(self):
        product_cards = self.find_all_elements(eco_friendly.PRODUCT_CARD)
        for card in product_cards:
            white_color = card.locator(eco_friendly.WHITE_COLOR_INSIDE_PRODUCT_CARD)
            assert white_color.count() > 0

    def check_counter_has_correct_value_of_founded_cards(self):
        product_cards = self.find_all_elements(eco_friendly.PRODUCT_CARD)
        founded_cards_with_white_color = self.find_element(eco_friendly.ALL_PRODUCTS_QUANTITY).nth(1).text_content()
        assert str(len(product_cards)) == founded_cards_with_white_color

    def open_selector_and_choose_24(self):
        drop_down_per_page = self.find_element(eco_friendly.SELECTOR).nth(1)

        drop_down_per_page.wait_for(state="visible", timeout=20000)
        drop_down_per_page.select_option(value="24")
        expect(self.page).to_have_url(re.compile('product_list_limit=24$'), timeout=20000)
