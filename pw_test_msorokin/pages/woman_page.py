from pw_test_msorokin.pages.base_page import BasePage


class WomenCatalogPage(BasePage):
    # elements of subpages in woman catalog
    WOMEN_PAGE = "#ui-id-4"
    WOMEN_TOPS_PAGE = "#ui-id-9"
    WOMEN_TOPS_JACKETS_PAGE = "#ui-id-11"
    WOMEN_TOPS_HOODIES_PAGE = "#ui-id-12"
    WOMEN_TOPS_TEES_PAGE = "#ui-id-13"
    WOMEN_TOPS_BRA_PAGE = "#ui-id-14"
    WOMEN_BOTTOM_PAGE = "#ui-id-10"
    WOMEN_BOTTOM_PANTS_PAGE = "#ui-id-15"
    WOMEN_BOTTOM_SHORTS_PAGE = "#ui-id-16"
    PRODUCT_CARDS_LIST = "//ol[@class='products list items product-items']/li"

    # elements of woman catalog page
    HOT_SELLERS = "//ol[@class='product-items widget-product-grid']"
    HOT_SELLERS_CARDS_LIST = "//ol[@class='product-items widget-product-grid']/li"
    CATEGORIES_MENU_TITLES = "//div[@class='categories-menu']/strong[@class='title']/span"
    SUBCATEGORIES_MENU_ITEMS = "//div[@class='categories-menu']/ul/li/a"
    CATEGORIES_ITEMS = "//ol[@class='items']/li[@class='item']/a"
    PRODUCT_PRICE = "//span[@class='price-wrapper ']/span[@class='price']"

    def choose_page_title_locator(self, title: str):
        locator = f"//span[@class='base' and @data-ui-id='page-title-wrapper' and text()='{title}']"
        title_element = self.find_element(locator)
        return title_element

    def get_women_store_page_element(self):
        return self.find_element(self.WOMEN_PAGE)

    def get_women_store_tops_page_element(self):
        return self.find_element(self.WOMEN_TOPS_PAGE)

    def get_women_tops_jacket_page_element(self):
        return self.find_element(self.WOMEN_TOPS_JACKETS_PAGE)

    def get_women_tops_hoodies_page_element(self):
        return self.find_element(self.WOMEN_TOPS_HOODIES_PAGE)

    def get_women_tops_tees_page_element(self):
        return self.find_element(self.WOMEN_TOPS_TEES_PAGE)

    def get_women_tops_bras_page_element(self):
        return self.find_element(self.WOMEN_TOPS_BRA_PAGE)

    def get_women_store_bottoms_page_element(self):
        return self.find_element(self.WOMEN_BOTTOM_PAGE)

    def get_women_bottoms_pants_page_element(self):
        return self.find_element(self.WOMEN_BOTTOM_PANTS_PAGE)

    def get_women_store_bottoms_shorts_page_element(self):
        return self.find_element(self.WOMEN_BOTTOM_SHORTS_PAGE)

    def hover_women_tops_page_element(self):
        self.get_women_store_page_element().hover()
        return self.get_women_store_tops_page_element().hover()

    def hover_women_bottom_page_element(self):
        self.get_women_store_page_element().hover()
        return self.get_women_store_bottoms_page_element().hover()

    def open_women_store_page(self):
        self.get_women_store_page_element().click()

    def open_women_tops(self):
        self.get_women_store_page_element().hover()
        self.get_women_store_tops_page_element().click()

    def open_women_tops_jackets(self):
        self.hover_women_tops_page_element()
        self.get_women_tops_jacket_page_element().click()

    def open_women_tops_hoodies(self):
        self.hover_women_tops_page_element()
        self.get_women_tops_hoodies_page_element().click()

    def open_women_tops_tees_page(self):
        self.hover_women_tops_page_element()
        self.get_women_tops_tees_page_element().click()

    def open_women_tops_bras_page(self):
        self.hover_women_tops_page_element()
        self.get_women_tops_bras_page_element().click()

    def open_women_bottoms_page(self):
        self.hover_women_bottom_page_element().click()

    def open_women_bottoms_pants_page(self):
        self.hover_women_bottom_page_element()
        self.get_women_bottoms_pants_page_element().click()

    def open_women_bottoms_shorts_page(self):
        self.hover_women_bottom_page_element()
        self.get_women_store_bottoms_shorts_page_element().click()

    def product_cards_are_present(self):
        return len(self.find_elements(self.PRODUCT_CARDS_LIST))

    def product_cards_are_present_in_hot_sellers_list(self):
        self.scroll_to_element(self.HOT_SELLERS)
        return len(self.find_elements(self.HOT_SELLERS_CARDS_LIST))

    def get_page_title(self, title: str):
        title_locator = self.choose_page_title_locator(title)
        return self.find_element(title_locator).inner_text()

    def get_categories_titles(self):
        return self.page.locator(self.CATEGORIES_MENU_TITLES).all_text_contents()

    def get_subcategories_items_text(self):
        return self.page.locator(self.SUBCATEGORIES_MENU_ITEMS).all_text_contents()

    def get_categories_items_text(self):
        return self.page.locator(self.CATEGORIES_ITEMS).all_text_contents()

    def get_main_categories_items_links(self) -> list:
        main_categories_links = self.get_links_from_elements(self.CATEGORIES_ITEMS)
        return main_categories_links

    def get_subcategories_items_links(self):
        subcategories_links = self.get_links_from_elements(self.SUBCATEGORIES_MENU_ITEMS)
        return subcategories_links

    def get_products_prices(self):
        return self.page.locator(self.PRODUCT_PRICE).all_text_contents()
