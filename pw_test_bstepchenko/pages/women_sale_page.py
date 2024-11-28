from pw_test_bstepchenko.pages.base_page import BasePage
from pw_test_bstepchenko.pages.locators import women_sale


class WomenSale(BasePage):
    women_sale_page = 'https://magento.softwaretestingboard.com/promotions/women-sale.html'

    def open_by_url(self):
        self.page.goto(self.women_sale_page)
        self.click_on_consent_button()
        return self.page.url

    def check_if_page_title_is_displayed(self, expected_title_text):
        title = self.find_element(women_sale.WOMEN_SALE_TITLE)
        assert title.text_content() == expected_title_text
