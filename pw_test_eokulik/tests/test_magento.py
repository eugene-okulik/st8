def test_elements(products_page):
    products_page.open_by_url('men/tops-men/hoodies-and-sweatshirts-men.html')
    products_page.sort_by_price()
    products_page.check_products_sorted_by_price()


def test_hover(home_page, products_page):
    home_page.open_by_url()
    home_page.open_men_jackets_from_menu()
    products_page.check_page_header_is_('Jackets')


def test_shop_luma_gear_link_visibility(sale_page):
    sale_page.open_by_url()
    sale_page.check_shop_luma_gear_link_not_in_viewport()
    sale_page.scroll(650)
    sale_page.check_shop_luma_gear_link_in_viewport()
