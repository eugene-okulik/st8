import time


# 1 test case, ok
def check_next_prev_page(adlist_page, card_page):
    adlist_page.open_page_bus()
    adlist_page.cookie_accept()
    adlist_page.open_one_card(0)
    card_page.by_search_check_next_and_prev_page()

# 2 test case, ok
def check_car_price(adlist_page):
    checked_price_min = 2000
    checked_price_max = 4000
    adlist_page.open_page_bus()
    adlist_page.cookie_accept()
    adlist_page.set_filter_by_prices(checked_price_min, checked_price_max)

    car_list = adlist_page.get_filtered_cars()
    for one_car in car_list:
        assert checked_price_min <= one_car['price'] <=  checked_price_max, "Invalid price range"

#3 test  case, ok
def check_car_gearbox(adlist_page):
    checked_gearbox = "Автоматична"
    adlist_page.open_page_bus()
    adlist_page.cookie_accept()
    adlist_page.set_filter_by_gearbox(checked_gearbox)
    car_list = adlist_page.get_filtered_cars()
    for one_car in car_list:
        assert one_car['gearbox'] == checked_gearbox, "Invalid car gearbox"

# 4 test case, ok
def check_car_year(adlist_page):
    checked_year_min = 2005
    checked_year_max = 2008
    adlist_page.open_page_bus()
    adlist_page.cookie_accept()
    adlist_page.set_filter_by_years(checked_year_min, checked_year_max)

    car_list = adlist_page.get_filtered_cars()
    for one_car in car_list:
        assert checked_year_min <= one_car['year'] <=  checked_year_max, "Invalid year range"

# 5 test case, ok
def check_car_power(adlist_page):
    checked_power_min = 100
    checked_power_max = 150
    adlist_page.open_page_bus()
    adlist_page.cookie_accept()
    adlist_page.set_filter_by_power(checked_power_min, checked_power_max)

    car_list = adlist_page.get_filtered_cars()
    print(f"car_list: {car_list}")
    for one_car in car_list:
        assert checked_power_min <= one_car['power'] <=  checked_power_max, "Invalid power range"

# 6 test case, ok
def check_car_color(adlist_page, card_page):
    checked_color = "Бял"
    adlist_page.open_page_bus()
    adlist_page.cookie_accept()
    adlist_page.set_filter_by_color(checked_color)
    car_links = adlist_page.get_filtered_cars()
    for one_car in car_links:
        this_car_link = one_car['link']
        card_page.open_card(this_car_link)
        one_car_color = card_page.get_color()
        assert one_car_color == checked_color, "Colors are not equal"

# 7 test  case, ok
def check_car_region(adlist_page):
    checked_region = "Бургас"
    adlist_page.open_page_bus()
    adlist_page.cookie_accept()
    adlist_page.set_filter_by_region(checked_region)
    adlist_page.press_button_refresh()
    car_list = adlist_page.get_filtered_cars()
    for one_car in car_list:
        assert one_car['region'] == checked_region, "Invalid car region"

# 8 test  case, ok
def sort_by_price_asc(adlist_page):
    adlist_page.open_page_bus()
    adlist_page.cookie_accept()
    time.sleep(2)
    adlist_page.change_sort_by_price_asc()
    adlist_page.press_button_refresh()
    price_list = []
    sort_price_list = []
    car_list = adlist_page.get_filtered_cars()
    for one_car in car_list:
        one_price = one_car['price']
        price_list.append(one_price)
        sort_price_list.append(one_price)

    sorted(sort_price_list)

    assert sort_price_list == price_list, "Invalid price order"

# 9 test  case, ok
def sort_by_price_desc(adlist_page):
    adlist_page.open_page_bus()
    adlist_page.cookie_accept()
    adlist_page.change_sort_by_price_desc()
    adlist_page.press_button_refresh()

    price_list = []
    sort_price_list = []
    car_list = adlist_page.get_filtered_cars()

    for one_car in car_list:
        one_price = one_car['price']
        price_list.append(one_price)
        sort_price_list.append(one_price)

    sort_price_list = sorted(sort_price_list, reverse=True)

    assert sort_price_list == price_list, "Invalid price order"

# 10 test  case, ok
def sort_by_year(adlist_page):
    adlist_page.open_page_bus()
    adlist_page.cookie_accept()
    adlist_page.change_sort_by_year()
    adlist_page.press_button_refresh()

    year_list = []
    sort_year_list = []
    car_list = adlist_page.get_filtered_cars()
    for one_car in car_list:
        one_year = one_car['year']
        year_list.append(one_year)
        sort_year_list.append(one_year)

    sort_year_list = sorted(sort_year_list, reverse=True)

    assert sort_year_list == year_list, "Invalid year order"


