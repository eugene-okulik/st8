def test_product_per_page(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.check_product_count(12)
    eco_friendly_page.change_product_count("24")
    eco_friendly_page.check_product_count(18)
    eco_friendly_page.change_product_count("36")
    eco_friendly_page.check_product_count(18)
    eco_friendly_page.change_product_count("12")
    eco_friendly_page.check_product_count(12)


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
