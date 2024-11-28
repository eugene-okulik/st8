from pw_test_bstepchenko.pages.base_page import BasePage
from pw_test_bstepchenko.pages.locators import sale_page as sales


class SalePage(BasePage):
    sale_page_url = 'https://magento.softwaretestingboard.com/sale.html'

    def open_by_url(self):
        return super().open_by_url(self.sale_page_url)

    def check_all_sales_cards_are_displayed(self):
        self.find_element(sales.MAIN_SALE)
        self.find_element(sales.MEN_SALE)
        self.find_element(sales.WOMEN_SALE)
        self.find_element(sales.SALE_20_OFF)
        self.find_element(sales.FREE_SHIPPING_SALE)
        self.find_element(sales.T_SHIRTS_SALE)

    def find_all_elements_inside_main_sale_card(self):
        main_sale_card = self.find_element(sales.MAIN_SALE)
        info = self.find_element(sales.MAIN_SALE_INFO, parent=main_sale_card)
        title = self.find_element(sales.MAIN_SALE_TITLE, parent=main_sale_card)
        button = self.find_element(sales.MAIN_SALE_BUTTON, parent=main_sale_card)
        return info, title, button

    def check_if_text_inside_main_sale_card_is_correct(self, expected_info_text,
                                                       expected_title_text, expected_button_text):
        info, title, button = self.find_all_elements_inside_main_sale_card()
        assert info.text_content() == expected_info_text
        assert title.text_content() == expected_title_text
        assert button.text_content() == expected_button_text

    def click_on_show_main_deal_button(self):
        info, title, button = self.find_all_elements_inside_main_sale_card()
        button.click()
