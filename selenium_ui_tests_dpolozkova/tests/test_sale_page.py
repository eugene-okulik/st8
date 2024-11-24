def test_headers_of_promo_banners(sale_page):
    sale_page.open_by_url('sale.html')
    sale_page.check_name_of_promos()

def test_women_sale_button_is_clickable(sale_page):
    sale_page.open_by_url('sale.html')
    sale_page.main_button_is_clickable()

def test_breadcrumbs_are_displayed(sale_page):
    sale_page.open_by_url('sale.html')
    sale_page.breadcrumbs_are_displayed()
