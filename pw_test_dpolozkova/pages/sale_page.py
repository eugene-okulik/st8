from playwright.sync_api import expect

from pw_test_dpolozkova.pages.base_page import BasePage
from pw_test_dpolozkova.pages.locators import sale_page as loc


class SalePage(BasePage):
    def open_by_url(self, postfix=None):
        if postfix:
            self.page.goto(f'{self.base_url}{postfix}')
        else:
            raise TypeError('TypeError: open_by_url() in class ProductsPage requires positional argument: "postfix"')

    def check_current_url(self):
        assert self.check_current_url() == 'https://magento.softwaretestingboard.com/sale.html'

    def check_name_of_promos(self, text: list):
        headers = list(self.find(loc.PROMOS).all())
        assert headers[0].text_content() == text[0]
        assert headers[1].text_content() == text[1]
        assert headers[2].text_content() == text[2]
        assert headers[3].text_content() == text[3]
        assert headers[4].text_content() == text[4]

    def main_button_is_clickable(self):
        self.find(loc.WOMEN_SALE).click()
        expect(self.page).to_have_url('https://magento.softwaretestingboard.com/promotions/women-sale.html')


    def check_home_sale_breadcrumb(self):
        breadcrumb = self.find(loc.BREADCRUMBS)
        expect(breadcrumb).to_have_text("Home Sale")
        back = self.find(loc.HOME).get_attribute('href')
        assert back == 'https://magento.softwaretestingboard.com/'
