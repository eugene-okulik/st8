from pw_test_msorokin.config.links import PagesLinksForAssertion


def test_navigate_to_jackets(home_page, women_catalog_page):
    home_page.open_by_url()
    women_catalog_page.open_women_tops_jackets()
    number_of_card = women_catalog_page.product_cards_are_present()
    assert number_of_card == 12


def test_check_hot_sellers_list(home_page, women_catalog_page):
    home_page.open_by_url()
    women_catalog_page.open_women_store_page()
    hot_sellers = women_catalog_page.product_cards_are_present_in_hot_sellers_list()
    assert hot_sellers == 4


def test_check_links_for_main_categories(home_page, women_catalog_page):
    home_page.open_by_url()
    women_catalog_page.open_women_store_page()
    subcategories_links = women_catalog_page.get_main_categories_items_links()
    assert subcategories_links == PagesLinksForAssertion.WOMEN_PAGE_CATEGORIES_LINKS


def test_check_links_for_subcategories(home_page, women_catalog_page):
    home_page.open_by_url()
    women_catalog_page.open_women_store_page()
    subcategories_links = women_catalog_page.get_subcategories_items_links()
    assert subcategories_links == PagesLinksForAssertion.WOMEN_PAGE_SUBCATEGORIES_LINKS


def test_check_categories_text(home_page, women_catalog_page):
    home_page.open_by_url()
    women_catalog_page.open_women_store_page()
    categories_text = women_catalog_page.get_categories_items_text()
    assert categories_text == ['Tops', 'Bottoms']


def test_check_subcategories_text(home_page, women_catalog_page):
    home_page.open_by_url()
    women_catalog_page.open_women_store_page()
    subcategories_text = women_catalog_page.get_subcategories_items_text()
    assert subcategories_text == ['Hoodies & Sweatshirts', 'Jackets', 'Tees', 'Bras & Tanks', 'Pants', 'Shorts']


def test_check_product_prices(home_page, women_catalog_page):
    home_page.open_by_url()
    women_catalog_page.open_women_bottoms_pants_page()
    prices = women_catalog_page.get_products_prices()
    assert prices != []
    assert all('$' in price for price in prices)
    assert len(prices) == 12
