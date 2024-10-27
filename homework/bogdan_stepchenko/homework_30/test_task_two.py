from functions_for_task_two import driver, find_and_click_start_button, find_finish_text


def test_waiting_for_result(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')

    find_and_click_start_button(driver)

    finish_text = find_finish_text(driver)

    assert finish_text == 'Hello World!', f"Expected 'Hello World!', but got '{finish_text}'"
