import  time
from final_project_lmargi.pages.const import const_card as const
from final_project_lmargi.tests.conftest import login_page
from final_project_lmargi.tests.conftest import notebook_page
from final_project_lmargi.tests.conftest import adlist_page


# 26 Test ok
def email_form_message_ignor_agree(card_page, adlist_page):
    adlist_page.open_page_bus()
    adlist_page.cookie_accept()
    adlist_page.open_one_card(0)
    card_page.press_dealer_button()
    assert card_page.get_ignore_checkbox_error() == True, f"Message is not visible"

#решить проблемы итерации
# def test_send_requst_invalid(card_page):
#     card_page.open_card('56772749/mercedes-benz-vito')
#     card_page.cookie_accept()
#     card_page.press_dealer_button()
#     time.sleep(2)
#     card_page.fill_send_request_field_message("test message")
#     time.sleep(2)
#     card_page.fill_send_request_field_name("margi")
#     card_page.press_send_request()
#     card_page.check_invalid_send_request_message()

# 27 ok
def show_phone_number(card_page, adlist_page):
    adlist_page.open_page_bus()
    adlist_page.cookie_accept()
    adlist_page.open_one_card(0)
    initial_text =card_page.check_phone_number_hidden()
    updated_phone_number = card_page.check_phone_number_visible(initial_text)
    assert updated_phone_number != initial_text, "Phone number did not become visible"

# 28 ok
def check_text_before_save_notebook(card_page, login_page, adlist_page):
    login_page.make_login()
    adlist_page.open_page_bus()
    adlist_page.open_one_card(0)

    text_before_click = card_page.check_title_notebook()
    assert  text_before_click == "Запиши в бележника", "Text not as expected"
    card_page.remove_car_from_notebook()


# 29 ok
def check_text_after_save_notebook(card_page, login_page, adlist_page):
    login_page.make_login()
    adlist_page.open_page_bus()
    adlist_page.open_one_card(0)

    text_after_click = card_page.check_title_notebook()
    assert text_after_click == "Изтрий от бележника", "Text not as expected"
    card_page.remove_car_from_notebook()


#не всегда в добавляется в бележник машина
# def test_check_list_save_notebook(card_page, notebook_page):


def test_ignore_privacy_policy_warning(card_page, adlist_page ):
    adlist_page.open_page_bus()
    card_page.cookie_accept()
    adlist_page.open_one_card(0)
    card_page.press_dealer_button()
    card_page.fill_send_request_field_message("ffggg")
    card_page.fill_send_request_field_name("VBBBGg")
    card_page.press_send_request()
    card_page.status_message_ignor_privacy_policy()
