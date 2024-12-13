import pytest


@pytest.mark.smoke
def test_elements(products_page):
    products_page.open_by_url('/men/tops-men/jackets-men.html')
    products_page.sort_by_price()
    products_page.check_products_sorted_by_price()


@pytest.mark.regression
def test_hover(home_page, products_page):
    home_page.open_by_url()
    home_page.open_men_jackets_from_menu()
    products_page.check_page_header_is_('Jackets')
