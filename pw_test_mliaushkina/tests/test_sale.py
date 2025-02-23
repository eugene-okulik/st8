def test_check_breadcrumb(sale_page):
    sale_page.open_page()
    sale_page.check_breadcrumb_sale("Sale")


def test_check_sale_links(sale_page):
    sale_page.open_page()
    sale_page.check_sale_links(['https://magento.softwaretestingboard.com/promotions/women-sale.html',
                                'https://magento.softwaretestingboard.com/promotions/men-sale.html',
                                'https://magento.softwaretestingboard.com/gear.html',
                                'https://magento.softwaretestingboard.com/women/tops-women/tees-women.html'])


def test_check_woman_sale(sale_page):
    sale_page.open_page()
    sale_page.check_woman_sale_img("https://magento.softwaretestingboard.com/pub/media/wysiwyg/sale/sale-main.jpg")
    sale_page.check_woman_sale_title("Pristine prices on pants, tanks and bras.")
