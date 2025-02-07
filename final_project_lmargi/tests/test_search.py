import  allure
from final_project_lmargi.pages.const import const_search as const


@allure.feature('Car search functionality')
@allure.story('Price filter range')
@allure.title('Поиск авто по диапазону цен')
def test_check_car_price(search_page, adlist_page):
    search_page.open_page()
    search_page.cookie_accept()
    search_page.field_price_from(const.CHEKCED_PRICE_MIN)
    search_page.field_price_to(const.CHEKCED_PRICE_MAX)
    search_page.press_button_search()

    car_list = adlist_page.get_filtered_cars()
    for one_car in car_list:
        assert const.CHEKCED_PRICE_MIN <= one_car['price'] <= const. CHEKCED_PRICE_MAX, "Invalid price range"


@allure.feature('Car search functionality')
@allure.story('Power filter range')
@allure.title('Поиск авто по диапазону мощности')
def test_check_car_power(search_page, adlist_page):
    search_page.open_page()
    search_page.cookie_accept()
    search_page.field_power_from(const.CHEKCED_POWER_MIN)
    search_page.field_power_to(const.CHEKCED_POWER_MAX)
    search_page.press_button_search()

    car_list = adlist_page.get_filtered_cars()
    for one_car in car_list:
        assert const.CHEKCED_POWER_MIN <= one_car['power'] <= const.CHEKCED_POWER_MAX, "Invalid power range"


@allure.feature('Car search functionality')
@allure.story('Gearbox filter')
@allure.title('Фильтр поиска  авто по коробке передач')
def test_check_car_gearbox(search_page, adlist_page):
    search_page.open_page()
    search_page.cookie_accept()
    search_page.field_gearbox(const.CHECKED_GEARBOX)
    search_page.press_button_search()

    car_list = adlist_page.get_filtered_cars()
    for one_car in car_list:
        assert one_car['gearbox'] == const.CHECKED_GEARBOX, "Invalid car gearbox"


@allure.feature('Car search functionality')
@allure.story('Brand filter')
@allure.title('Фильтр поиска  авто по марке')
def test_check_car_brand(search_page, adlist_page):
    search_page.open_page()
    search_page.cookie_accept()
    search_page.field_brand(const.CHECKED_BRAND)
    search_page.press_button_search()

    car_list = adlist_page.get_filtered_cars()
    for one_car in car_list:
        for one_car in car_list:
            assert const.CHECKED_BRAND in one_car[
                'title'], f"Brand '{const.CHECKED_BRAND}' not found in car title: {one_car['title']}"


@allure.feature('Car search functionality')
@allure.story('Region filter')
@allure.title('Фильтр поиска  авто по региону')
def test_check_region(search_page, adlist_page):
    search_page.open_page()
    search_page.cookie_accept()
    search_page.field_region(const.CHECKED_REGION)
    search_page.press_button_search()
    car_list = adlist_page.get_filtered_cars()

    for one_car in car_list:
        assert one_car['region'] == const.CHECKED_REGION, "Invalid car region"


@allure.feature('Car search functionality')
@allure.story('Section transport filter')
@allure.title('Фильтр поиска по  виду транспорта')
def test_select_transport(search_page):
    search_page.open_page()
    search_page.cookie_accept()
    search_page.field_section(const.FIELD_SECTION)
    search_page.title_h1(const.TITLE_H_1)
    assert search_page.title_h1(const.TITLE_H_1), "Title H1 not displayed"


@allure.feature('Car search functionality')
@allure.story('Condition transport filter')
@allure.title('Фильтр поиска по состоянию машины: Б/у')
def test_condithion_car_used(search_page):
    search_page.open_page()
    search_page.cookie_accept()
    search_page.reset_checkboxes_on_page()
    search_page.check_condithion_input_used(const.INPUT_USED)
    search_page.press_button_search()
    result = search_page.search_result()
    assert const.TITLE_USED_CAR in result, f"Not found: {const.TITLE_USED_CAR} in search results"


@allure.feature('Car search functionality')
@allure.story('Condition transport filter')
@allure.title('Фильтр поиска по состоянию машины: новая')
def test_condithion_car_new(search_page):
    search_page.open_page()
    search_page.cookie_accept()
    search_page.reset_checkboxes_on_page()
    search_page.check_condithion_input_new(const.INPUT_NEW)
    search_page.press_button_search()
    result = search_page.search_result()
    assert const.TITLE_NEW_CAR in result, f"Not found: {const.TITLE_NEW_CAR} in search results"


@allure.feature('Car search functionality')
@allure.story('Condition transport filter')
@allure.title('Фильтр поиска по состоянию машины: новая, б/у, на запчасти')
def test_condithion_car_all(search_page):
    search_page.open_page()
    search_page.cookie_accept()
    search_page.reset_checkboxes_on_page()
    search_page.select_all_checkboxes_on_page(const.UNPUT_ALL_CHECKBOX)
    search_page.press_button_search()
    result = search_page.search_result()
    assert const.ALL_TITLE_CHECKBOX in result, f"Not found: {const.ALL_TITLE_CHECKBOX} in search results"
