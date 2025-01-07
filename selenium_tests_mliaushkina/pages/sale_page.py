from selenium_tests_mliaushkina.pages.base_page import BasePage
from selenium_tests_mliaushkina.pages.locators import locator_sale as locator
from selenium.webdriver.common.by import By


class SalePage(BasePage):

    def open_page(self):
        self.open_by_url('sale.html')

    def check_breadcrumb_sale(self):
        breadcrumb_ui = self.find(locator.BREADCRUMB_ITEM)
        assert breadcrumb_ui.text == "Sale"

    def check_sale_links(self):
        check_sale_href = ['https://magento.softwaretestingboard.com/promotions/women-sale.html',
                           'https://magento.softwaretestingboard.com/promotions/men-sale.html',
                           'https://magento.softwaretestingboard.com/gear.html',
                           'https://magento.softwaretestingboard.com/women/tops-women/tees-women.html']
        list_all_href = []
        main_div = self.find(locator.BLOCKS_PROMO_ITEM)
        all_a_hrefs = main_div.find_elements(By.TAG_NAME, "a")
        for one_a in all_a_hrefs:
            one_href = one_a.get_attribute("href")
            if one_href is not None:
                list_all_href.append(one_href)

        assert check_sale_href == list_all_href, "Sale links are broken"

    def check_woman_sale_img(self):
        a_item = self.find(locator.WOMAN_SALE_ITEM)
        img_item = a_item.find_element(By.TAG_NAME, "img")
        img_item_src = img_item.get_attribute("src")

        assert img_item_src == "https://magento.softwaretestingboard.com/pub/media/wysiwyg/sale/sale-main.jpg", \
            "Not found woman sale img"

    def check_woman_sale_title(self):
        a_item = self.find(locator.WOMAN_SALE_ITEM)
        strong_item = self.find(locator.MAIN_TITLE_NAME, a_item)

        assert strong_item.text == "Pristine prices on pants, tanks and bras.", "Invalid woman sale title"
