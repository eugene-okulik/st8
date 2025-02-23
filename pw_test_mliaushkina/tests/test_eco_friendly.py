def test_search_product_by_name(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.search_by_name("Tiffany")
    eco_friendly_page.check_if_product_found("Tiffany Fitness Tee")


def test_product_view_mode(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.check_is_grid_view()
    eco_friendly_page.change_to_list_view()
    eco_friendly_page.check_is_list_view()


def test_sort_by_price(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.change_sort_by_price_asc()
    eco_friendly_page.check_if_prices_are_asc()
    eco_friendly_page.change_sort_by_price_desc()
    eco_friendly_page.check_if_prices_are_desc()
