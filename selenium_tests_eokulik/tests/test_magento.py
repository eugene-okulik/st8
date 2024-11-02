def test_elements(products_page):
    products_page.open_by_url()
    products_page.sort_by_price()
    products_page.check_products_sorted_by_price()


def test_hover(home_page, products_page):
    home_page.open_by_url()
    home_page.open_men_jackets_from_menu()
    products_page.check_page_header_is_('Jackets')
