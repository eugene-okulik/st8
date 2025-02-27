from playwright.sync_api import expect

from pw_test_mliaushkina.pages.base_page import BasePage
from pw_test_mliaushkina.pages.locators import locator_sale as loc_const


class SalePage(BasePage):

    def open_page(self):
        self.open_by_url('sale.html')
        self.page.reload()

    def check_breadcrumb_sale(self, title):
        breadcrumb_ui = self.find(loc_const.BREADCRUMB_ITEM)
        expect(breadcrumb_ui).to_have_text(title)

    def check_sale_links(self, check_sale_href):

        list_all_href = []
        main_div = self.find(loc_const.BLOCKS_PROMO_ITEM)
        all_a_hrefs = main_div.locator("a").all()
        for one_a in all_a_hrefs:
            one_href = one_a.get_attribute("href")
            if one_href is not None:
                list_all_href.append(one_href)

        assert check_sale_href == list_all_href, "Sale links are broken"

    def check_woman_sale_img(self, checked_img):
        a_item = self.find(loc_const.WOMAN_SALE_ITEM)
        img_item = a_item.locator("img")

        expect(img_item).to_have_attribute("src", checked_img)

    def check_woman_sale_title(self, checked_title):
        a_item = self.find(loc_const.WOMAN_SALE_ITEM)
        strong_item = a_item.locator(loc_const.MAIN_SALE_TITLE_ITEM)

        expect(strong_item).to_have_text(checked_title)
