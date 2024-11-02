from selenium.webdriver.common.by import By
from functions_for_task_one import wait_for_element


def find_launch_button_and_click(driver):
    launch_button = wait_for_element(driver, By.XPATH, './/button[@class="btn btn-primary"]')
    launch_button.click()


def copy_text_from_iframe_and_close_iframe(driver):
    iframe = wait_for_element(driver, By.XPATH, './/iframe[@class="embed-responsive-item"]')
    driver.switch_to.frame(iframe)
    text_in_iframe = wait_for_element(driver, By.ID, 'text-to-copy')
    text_for_copying = text_in_iframe.text
    print(text_for_copying)
    driver.switch_to.default_content()
    check_button = wait_for_element(driver, By.XPATH, './/button[@type="submit"]')
    check_button.click()
    return text_for_copying


def find_input_field_and_enter_text(driver, text):
    input_field = wait_for_element(driver, By.XPATH, './/input[@class="textinput textInput form-control"]')
    input_field.send_keys(text)


def find_and_click_submit_button(driver):
    submit_button = wait_for_element(driver, By.ID, 'submit-id-submit')
    submit_button.click()


def find_result(driver):
    result = wait_for_element(driver, By.ID, 'check-result')
    return result.text
