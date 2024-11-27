from pw_test_eokulik.pages.base_page import BasePage
from pw_test_eokulik.pages.locators import sale_page as loc
from playwright.sync_api import expect


class SalePage(BasePage):
    def open_by_url(self, postfix=None):
        postfix = 'sale.html'
        self.page.goto(f'{self.base_url}{postfix}')

    def check_shop_luma_gear_link_in_viewport(self):
        expect(self.find(loc.SHOP_LUMA_GEAR)).to_be_in_viewport()

    def check_shop_luma_gear_link_not_in_viewport(self):
        expect(self.find(loc.SHOP_LUMA_GEAR)).not_to_be_in_viewport()
