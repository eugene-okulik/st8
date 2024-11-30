def test_search_for_product(eco_products_page):
    eco_products_page.open_by_url('collections/eco-friendly.html')
    eco_products_page.search_for_product_by_name('Fiona')
    eco_products_page.results_are_displayed()
    eco_products_page.check_found_results('Fiona Fitness Short')


def test_switch_to_list_view(eco_products_page):
    eco_products_page.open_by_url('collections/eco-friendly.html')
    eco_products_page.apply_list_view_option()
    eco_products_page.check_grid_is_switched_to_list()


def test_sort_by_price(eco_products_page):
    eco_products_page.open_by_url('collections/eco-friendly.html')
    eco_products_page.sort_by_filter('price')
    eco_products_page.check_products_sorted_by_price()
