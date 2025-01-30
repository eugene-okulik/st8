import time

# 11 test case, ok
def check_car_price(search_page, adlist_page):
    checked_price_min = 2000
    checked_price_max = 4000
    search_page.open_page()
    search_page.cookie_accept()
    search_page.field_price_from(checked_price_min)
    search_page.field_price_to(checked_price_max)
    search_page.press_button_search()

    car_list = adlist_page.get_filtered_cars()
    for one_car in car_list:
        assert checked_price_min <= one_car['price'] <=  checked_price_max, "Invalid price range"

# 12 test case, ok
def check_car_year(search_page, adlist_page):
    checked_year_min = 2005
    checked_year_max = 2010
    search_page.open_page()
    search_page.cookie_accept()
    search_page.field_year_from(checked_year_min)
    search_page.field_year_to(checked_year_max)
    search_page.press_button_search()

    car_list = adlist_page.get_filtered_cars()
    for one_car in car_list:
        assert checked_year_min <= one_car['year'] <= checked_year_max, "Invalid year range"

# 13 test case, ok
def check_car_power(search_page, adlist_page):
    checked_power_min = 130
    checked_power_max = 150
    search_page.open_page()
    search_page.cookie_accept()
    search_page.field_power_from(checked_power_min)
    search_page.field_power_to(checked_power_max)
    search_page.press_button_search()

    car_list = adlist_page.get_filtered_cars()
    for one_car in car_list:
        assert checked_power_min <= one_car['power'] <= checked_power_max, "Invalid power range"

# 14 test case, ok
def check_car_gearbox(search_page, adlist_page):
    checked_gearbox = "Автоматична"
    search_page.open_page()
    search_page.cookie_accept()
    search_page.field_gearbox(checked_gearbox)
    search_page.press_button_search()

    car_list = adlist_page.get_filtered_cars()
    for one_car in car_list:
        assert one_car['gearbox'] == checked_gearbox, "Invalid car gearbox"

# 15 test case, ok
def check_car_brand(search_page, adlist_page):
    checked_brand = "Chevrolet"
    search_page.open_page()
    search_page.cookie_accept()
    search_page.field_brand(checked_brand)
    search_page.press_button_search()

    car_list = adlist_page.get_filtered_cars()
    for one_car in car_list:
        for one_car in car_list:
            assert checked_brand in one_car[
                'title'], f"Brand '{checked_brand}' not found in car title: {one_car['title']}"

# 16 test case, ok
def check_region(search_page, adlist_page):
    checked_region = "Разград"
    search_page.open_page()
    search_page.cookie_accept()
    search_page.field_region(checked_region)
    search_page.press_button_search()
    car_list = adlist_page.get_filtered_cars()

    for one_car in car_list:
        assert one_car['region'] == checked_region, "Invalid car region"

# 17 test case, ok
def select_transport(search_page):
    search_page.open_page()
    search_page.cookie_accept()
    search_page.field_section("3")
    time.sleep(3)
    search_page.title_h1("Търсене на Бусове")
    assert search_page.title_h1("Търсене на Бусове"), "Title H1 not displayed"

# 18 test case, ok
def condithion_car_used(search_page):
    search_page.open_page()
    search_page.cookie_accept()
    search_page.reset_checkboxes_on_page()
    search_page.check_condithion_input_used("03")
    search_page.press_button_search()
    result = search_page.search_result("Употребяван")
    assert "Употребяван" in result, f"Not found: Употребяван"


# 19 test case, ok
def condithion_car_new(search_page):
    search_page.open_page()
    search_page.cookie_accept()
    search_page.reset_checkboxes_on_page()
    search_page.check_condithion_input_new("13")
    search_page.press_button_search()
    result = search_page.search_result("Нов")
    assert "Нов" in result, f"Not found: Нов"

# 20 test case, ok
def condithion_car_all(search_page):
    search_page.open_page()
    search_page.cookie_accept()
    search_page.reset_checkboxes_on_page()
    search_page.select_all_checkboxes_on_page("0123")
    search_page.press_button_search()
    result = search_page.search_result("Употребяван, Нов, За части")
    assert "Употребяван, Нов, За части" in result, f"Not found: Употребяван, Нов, За части"
