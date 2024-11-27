from playwright.sync_api import expect
from pw_test_eokulik.pages.base_page import BasePage
from pw_test_eokulik.pages.locators import products_page as loc
import re


class ProductsPage(BasePage):

    def open_by_url(self, postfix=None):
        if postfix:
            self.page.goto(f'{self.base_url}{postfix}')
        else:
            raise TypeError('TypeError: open_by_url() in class ProductsPage requires positional argument: "postfix"')

    def sort_by_price(self):
        self.find(loc.SELECT_SORTING).first.select_option('price')
        expect(self.page).to_have_url(re.compile('product_list_order=price'))

    def check_products_sorted_by_price(self):
        product_cards = self.find(loc.PRODUCT_CARDS).all()
        prices = [
            float(
                product.locator('.price').text_content().replace('$', '')
            ) for product in product_cards
        ]
        assert prices == sorted(prices)

    def check_page_header_is_(self, text):
        expect(self.find(loc.PAGE_HEADER)).to_have_text(text)
