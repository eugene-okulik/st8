import allure
from final_project_lmargi.pages.const import const_add_announc as const
from final_project_lmargi.pages.const import const_my_offers as const_off


@allure.feature('New offer page functionality')
@allure.story('Checkbox  is not selected')
@allure.title('Проверка что чекбокс не активен')
def model_dropdown_disabled_without_brand(add_announcement_page, login_page):
    login_page.make_login()
    add_announcement_page.open_page()
    add_announcement_page.field_section(const.SECTION)
    model_dropdown_count = add_announcement_page.get_field_model_option_count()
    assert model_dropdown_count == 0, "Model dropdown should be disabled without brand"


@allure.feature('New offer page functionality')
@allure.story('Select price by agreement')
@allure.title('Проверка визуализации предупреждающего сообщения')
def visible_allert_message(add_announcement_page, login_page):
    login_page.make_login()
    add_announcement_page.open_page()
    add_announcement_page.check_checkbox_price()
    allert_message = add_announcement_page.wait_allert()
    assert  allert_message, "Alert message negotiation is not visible"


@allure.feature('New offer page functionality')
@allure.story('Required fields are not filled in')
@allure.title('Проверка вывода сообщения об ошибке при незаполненных обязательных полях')
def visible_message_error(add_announcement_page, login_page):
    login_page.make_login()
    add_announcement_page.open_page()
    add_announcement_page. field_section(const.SECTION)
    add_announcement_page.field_price(const.PRICE)
    add_announcement_page.field_currency(const.CURRENCY)
    add_announcement_page.field_brand(const.BRAND)
    add_announcement_page.field_month(const.MONTH)
    add_announcement_page.field_year(const.YEAR)
    add_announcement_page.field_type(const.TYPE)
    add_announcement_page.field_model(const.MODEL)
    add_announcement_page.field_engine_type(const.ENGINE_TYPE)
    add_announcement_page.field_gearbox(const.GEARBOX)
    add_announcement_page.field_region(const.REGION)
    add_announcement_page.field_place(const.PLACE)
    add_announcement_page.field_mileage(const.MILEAGE)
    add_announcement_page.press_button_create_ad()
    invalid_message = add_announcement_page.wait_message_invalid_check()
    expected_message = const.INVALID_MESSAGE_STATUS
    assert invalid_message == expected_message, "Invalid message negotiation  is not visible"


@allure.feature('New offer page functionality')
@allure.story('Check visible big title')
@allure.title('Визуализация заголовка  публикации объявления')
def check_the_presence_title(add_announcement_page, login_page):
    login_page.make_login()
    title_announcement = add_announcement_page.check_title_big(const.TITLE_BIG)
    expected_title = const.TITLE_BIG
    assert title_announcement == expected_title, "Title BIG not displayed"


@allure.feature('New offer page functionality')
@allure.story('Validation of additional info field')
@allure.title('Визуализация сообщения об ошибке при заполнении поля доп.инфо')
def check_add_information(add_announcement_page, login_page):
    login_page.make_login()
    add_announcement_page.field_text_add_info(const.TEXT_ADD_INFO)
    add_announcement_page.press_button_create_ad()
    invalid_message = add_announcement_page.wait_message_invalid_check()
    expected_message = const.INVALID_MESSAGE_LETTER_FORMAT
    assert invalid_message == expected_message, "Invalid message negotiation  is not visible"


@allure.feature('New offer page functionality')
@allure.story('Add correct new offer')
@allure.title('Успешное добавление нового объявления')
def check_add_correct_info(add_announcement_page, login_page, my_offers_page):
    login_page.make_login()
    add_announcement_page.open_page()
    add_announcement_page.field_section(const.SECTION)
    add_announcement_page.field_price(const.PRICE)
    add_announcement_page.field_currency(const.CURRENCY)
    add_announcement_page.field_brand(const.BRAND)
    add_announcement_page.field_month(const.MONTH)
    add_announcement_page.field_year(const.YEAR)

    add_announcement_page.field_type(const.TYPE)
    add_announcement_page.field_model(const.MODEL)
    add_announcement_page.field_engine_type(const.ENGINE_TYPE)
    add_announcement_page.field_gearbox(const.GEARBOX)
    add_announcement_page.field_region(const.REGION)
    add_announcement_page.field_place(const.PLACE)

    add_announcement_page.check_condithion_input_used(const.USED_CHECKBOX)
    add_announcement_page.field_mileage(const.MILEAGE)
    add_announcement_page.press_button_create_ad()
    add_announcement_page.check_change_url(const.POSTFIX)
    add_announcement_page.press_button_create_ad_2()

    my_offers_page.open_by_url(const_off.MY_OFFERS)
    product_title = const_off.PRODUCT_TITLE
    car_list = my_offers_page.get_filtered_title()

    for one_car in car_list:
        assert one_car['title'] == product_title, "Invalid car title"
    my_offers_page.delete_all_cars()
    my_offers_page.wait_allert_for_delete()
