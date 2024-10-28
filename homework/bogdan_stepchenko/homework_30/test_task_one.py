import pytest
from selenium import webdriver
from functions_for_task_one import find_and_open_dropdown, select_random_option_from_dropdown, \
    find_and_click_submit_button, wait_for_result_text


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_chosen_language_is_displayed(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')

    language_dropdown = find_and_open_dropdown(driver)

    text_of_selected_option = select_random_option_from_dropdown(language_dropdown)

    find_and_click_submit_button(driver)

    result_text = wait_for_result_text(driver)

    assert text_of_selected_option == result_text, f"Ожидался: {text_of_selected_option}, получили: {result_text}"
