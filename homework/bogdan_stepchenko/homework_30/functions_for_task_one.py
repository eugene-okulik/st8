import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def find_and_open_dropdown(driver):
    language_dropdown = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'id_choose_language'))
    )
    language_dropdown.click()
    return language_dropdown


def select_random_option_from_dropdown(dropdown):
    select = Select(dropdown)
    options = select.options[1:]

    random_option = random.choice(options)
    random_option_text = random_option.text

    select.select_by_visible_text(random_option_text)
    return random_option_text


def find_and_click_submit_button(driver):
    submit_button = driver.find_element(By.ID, 'submit-id-submit')
    submit_button.click()


def wait_for_result_text(driver):
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'result-text'))
    )

    result_text = driver.find_element(By.ID, 'result-text').text
    return result_text
