from functions_for_task_three import find_launch_button_and_click, copy_text_from_iframe_and_close_iframe, \
    find_input_field_and_enter_text, find_and_click_submit_button, find_result


def test_check_copy_text(driver):
    driver.get('https://www.qa-practice.com/elements/popup/iframe_popup')

    find_launch_button_and_click(driver)
    target_text = copy_text_from_iframe_and_close_iframe(driver)
    find_input_field_and_enter_text(driver, target_text)
    find_and_click_submit_button(driver)

    result_text = find_result(driver)
    assert result_text == 'Correct!', 'Incorrect text was send to comparing!'
