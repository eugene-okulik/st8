from playwright.sync_api import Page
from functions_for_task_one import ColorChangeButton
from functions_for_task_two import RegistrationsForm
from test_data import expected_first_name, expected_last_name, expected_email, \
    expected_phone, expected_subject, expected_address, expected_state, expected_city


def test_click_on_color_button(page: Page):
    color_button = ColorChangeButton(page)
    color_button.open_web_page()
    color_button.wait_for_button_is_colored()
    color_button.click_on_button()


def test_fill_all_fields_on_page(page: Page):
    registration = RegistrationsForm(page)
    registration.open_web_page()
    registration.fill_all_registration_fields(expected_first_name, expected_last_name,
                                              expected_email, expected_subject, expected_phone,
                                              expected_address, expected_state, expected_city)
    registration.click_submit_button()
    registration.check_user_data_in_result_table(expected_first_name, expected_last_name,
                                                 expected_email, expected_subject, expected_phone,
                                                 expected_address, expected_state, expected_city)
