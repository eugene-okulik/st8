import allure
from final_project_lmargi.pages.const import const_adlist as const


@allure.feature('Car obiavi functionality')
@allure.story('Pricer transport range')
@allure.title('Фильтр поиска авто по диапазону цен')
def test_check_car_price(adlist_page):
    adlist_page.open_page_bus()
    adlist_page.cookie_accept()
    adlist_page.set_filter_by_prices(const.CHEKCED_PRICE_MIN, const.CHEKCED_PRICE_MAX)
    adlist_page.press_button_refresh()

    car_list = adlist_page.get_filtered_cars()
    for one_car in car_list:
        assert const.CHEKCED_PRICE_MIN <= one_car['price'] <= const.CHEKCED_PRICE_MAX, "Invalid price range"


@allure.feature('Car obiavi functionality')
@allure.story('Gearboxt ransport filter')
@allure.title('Фильтр поиска авто по коробке передач')
def test_check_car_gearbox(adlist_page):
    adlist_page.open_page_bus()
    adlist_page.cookie_accept()
    adlist_page.set_filter_by_gearbox(const.CHECKED_GEARBOX)
    adlist_page.press_button_refresh()
    car_list = adlist_page.get_filtered_cars()
    for one_car in car_list:
        assert one_car['gearbox'] == const.CHECKED_GEARBOX, "Invalid car gearbox"


@allure.feature('Car obiavi functionality')
@allure.story('Year car range')
@allure.title('Фильтр поиска авто по диапазону лет')
def test_check_car_year(adlist_page):
    adlist_page.open_page_bus()
    adlist_page.cookie_accept()
    adlist_page.set_filter_by_years(const.CHEKCED_YEAR_MIN, const.CHEKCED_YEAR_MAX)
    adlist_page.press_button_refresh()

    car_list = adlist_page.get_filtered_cars()
    for one_car in car_list:
        assert const.CHEKCED_YEAR_MIN <= one_car['year'] <=  const.CHEKCED_YEAR_MAX, "Invalid year range"


@allure.feature('Car obiavi functionality')
@allure.story('Power car range')
@allure.title('Фильтр поиска авто по диапазону мощности')
def test_check_car_power(adlist_page):
    adlist_page.open_page_bus()
    adlist_page.cookie_accept()
    adlist_page.set_filter_by_power(const.CHEKCED_POWER_MIN, const.CHEKCED_POWER_MAX)
    adlist_page.press_button_refresh()

    car_list = adlist_page.get_filtered_cars()
    for one_car in car_list:
        assert const.CHEKCED_POWER_MIN <= one_car['power'] <=  const.CHEKCED_POWER_MAX, "Invalid power range"


@allure.feature('Car obiavi functionality')
@allure.story('Color transport filter')
@allure.title('Фильтр поиска по цвету авто')
def test_check_car_color(adlist_page, card_page):
    adlist_page.open_page_bus()
    adlist_page.cookie_accept()
    adlist_page.set_filter_by_color(const.CHECKED_COLOR)
    adlist_page.press_button_refresh()
    car_links = adlist_page.get_filtered_cars()
    for one_car in car_links:
        this_car_link = one_car['link']
        card_page.open_card(this_car_link)
        one_car_color = card_page.get_color()
        assert one_car_color == const.CHECKED_COLOR, "Colors are not equal"


@allure.feature('Car obiavi functionality')
@allure.story('Region transport filter')
@allure.title('Фильтр поиска по региону')
def test_check_car_region(adlist_page):
    adlist_page.open_page_bus()
    adlist_page.cookie_accept()
    adlist_page.set_filter_by_region(const.CHECKED_REGION)
    car_list = adlist_page.get_filtered_cars()
    for one_car in car_list:
        assert one_car['region'] == const.CHECKED_REGION, "Invalid car region"


@allure.feature('Car obiavi functionality')
@allure.story('Sort by price filter')
@allure.title('Сортировка авто по цене: возрастание')
def test_sort_by_price_asc(adlist_page):
    adlist_page.open_page_bus()
    adlist_page.cookie_accept()
    adlist_page.change_sort_by_price_asc()

    price_list = []
    sort_price_list = []
    car_list = adlist_page.get_filtered_cars()
    for one_car in car_list:
        one_price = one_car['price']
        price_list.append(one_price)
        sort_price_list.append(one_price)

    sort_price_list = sorted(sort_price_list)

    assert sort_price_list == price_list, "Invalid price order"


@allure.feature('Car obiavi functionality')
@allure.story('Sort by price filter')
@allure.title('Сортировка авто по цене: убывание')
def test_sort_by_price_desc(adlist_page):
    adlist_page.open_page_bus()
    adlist_page.cookie_accept()
    adlist_page.change_sort_by_price_desc()

    price_list = []
    sort_price_list = []
    car_list = adlist_page.get_filtered_cars()

    for one_car in car_list:
        one_price = one_car['price']
        price_list.append(one_price)
        sort_price_list.append(one_price)

    sort_price_list = sorted(sort_price_list, reverse=True)

    assert sort_price_list == price_list, "Invalid price order"


@allure.feature('Car obiavi functionality')
@allure.story('Sort by year filter')
@allure.title('Сортировка авто по году выпуска')
def test_sort_by_year(adlist_page):
    adlist_page.open_page_bus()
    adlist_page.cookie_accept()
    adlist_page.change_sort_by_year()

    year_list = []
    sort_year_list = []
    car_list = adlist_page.get_filtered_cars()
    for one_car in car_list:
        one_year = one_car['year']
        year_list.append(one_year)
        sort_year_list.append(one_year)

    sort_year_list = sorted(sort_year_list, reverse=True)

    assert sort_year_list == year_list, "Invalid year order"
