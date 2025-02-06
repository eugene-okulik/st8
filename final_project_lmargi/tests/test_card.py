import allure
from final_project_lmargi.pages.const import const_card as const
from final_project_lmargi.tests.conftest import login_page
from final_project_lmargi.tests.conftest import adlist_page


@allure.feature('Сard_page')
@allure.story('Message display on ignore checkbox interaction')
@allure.title('Проверка сообщения об ошибке при игнорировании чекбокса в форме')
def test_email_form_message_ignor_agree(card_page, adlist_page):
    adlist_page.open_page_bus()
    adlist_page.cookie_accept()
    adlist_page.open_one_card(0)
    card_page.press_dealer_button()
    assert card_page.get_ignore_checkbox_error() == True, f"Message is not visible"


@allure.feature('Сard_page')
@allure.story('Show phone number')
@allure.title('Проверка отображения скрытого телефонного номера')
def test_show_phone_number(card_page, adlist_page):
    adlist_page.open_page_bus()
    adlist_page.cookie_accept()
    adlist_page.open_one_card(0)
    initial_text =card_page.check_phone_number_hidden()
    updated_phone_number = card_page.check_phone_number_visible(initial_text)
    assert updated_phone_number != initial_text, "Phone number did not become visible"


@allure.feature('Сard_page')
@allure.story('Title write in a notebook')
@allure.title('Проверка заголовка перед сохранием в блокнот')
def test_check_text_before_save_notebook(card_page, login_page, adlist_page):
    login_page.make_login()
    adlist_page.open_page_bus()
    adlist_page.open_one_card(0)

    text_before_click = card_page.check_title_notebook()
    assert  text_before_click == const.TITLE_SAVE_NOTEBOOK, "Text not as expected"
    card_page.remove_car_from_notebook()
    login_page.click_on_logout_button()

@allure.feature('Сard_page')
@allure.story('Title delete from notepad')
@allure.title('Проверка заголовка после сохрания в блокнот')
def test_check_text_after_save_notebook(card_page, login_page, adlist_page):
    login_page.make_login()
    adlist_page.open_page_bus()
    adlist_page.open_one_card(0)

    text_after_click = card_page.check_title_notebook()
    assert text_after_click == const.TITLE_DELETE_NOTEBOOK, "Text not as expected"
    card_page.remove_car_from_notebook()
    login_page.click_on_logout_button()


@allure.feature('Сard_page')
@allure.story("Click next page then return to prev ")
@allure.title('Проверка перехода на следующую страницу ')
def test_check_next_page(card_page, adlist_page, driver):
    adlist_page.open_page_bus()
    adlist_page.cookie_accept()
    first_car_link = adlist_page.open_first_card()
    card_page.click_next_page()
    card_page.click_prev_page()
    current_link = card_page.get_current_pure_url()

    assert first_car_link == current_link, f"links don't match : {current_link}"
