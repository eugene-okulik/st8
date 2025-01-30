def search_by_price_year_filter(search_page):
    search_page.open_page()
    search_page.cookie_accept()
    search_page.field_price_from("3000")
    search_page.field_price_to("4000")
    search_page.field_year_from("2000")
    search_page.field_year_to("2003")
    search_page.press_button_search()
    search_page.check_change_url("obiavi")
