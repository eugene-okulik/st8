def test_check_breadcrumb(sale_page):
    sale_page.open_page()
    sale_page.check_breadcrumb_sale()


def test_check_sale_links(sale_page):
    sale_page.open_page()
    sale_page.check_sale_links()


def test_check_woman_sale(sale_page):
    sale_page.open_page()
    sale_page.check_woman_sale_img()
    sale_page.check_woman_sale_title()
