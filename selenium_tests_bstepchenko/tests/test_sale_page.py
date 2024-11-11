from selenium_tests_bstepchenko.pages.helper.text_to_check import MAIN_SALE_WOMAN_INFO, \
    MAIN_SALE_WOMAN_BUTTON, MAIN_SALE_WOMAN_TITLE, WOMAN_SALE_TITLE


def test_all_sales_blocks_are_displayed(sales_page):
    sales_page.open_by_url()
    sales_page.check_all_sales_cards_are_displayed()


def test_main_sales_card_ui(sales_page):
    sales_page.open_by_url()
    sales_page.find_all_elements_inside_main_sale_card()
    sales_page.check_if_text_inside_main_sale_card_is_correct(MAIN_SALE_WOMAN_INFO,
                                                              MAIN_SALE_WOMAN_TITLE, MAIN_SALE_WOMAN_BUTTON)


def test_open_main_sale_screen_via_clicking_on_button(sales_page, women_sale_page):
    sales_url = sales_page.open_by_url()
    sales_page.click_on_show_main_deal_button()
    women_sale_page.check_url_was_changed(sales_url)
    women_sale_page.check_if_page_title_is_displayed(WOMAN_SALE_TITLE)
