import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import TimeoutException


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_choose_language(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    select_language = driver.find_element(By.ID, 'id_choose_language')
    dropdown = Select(select_language)
    chosen_language = 'C#'
    dropdown.select_by_visible_text('C#')
    button = driver.find_element(By.ID, 'submit-id-submit')
    assert button.is_enabled()
    button.click()
    you_selected = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.CLASS_NAME, 'result-text'))
    ).text
    print(f"Chosen_language displayed correctly: {chosen_language}")
    assert you_selected == chosen_language, f"Expected '{chosen_language}', got '{you_selected}'"


def test_enter_start(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    button_start = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.XPATH, "//div[@id='start']/button"))
    )
    assert button_start.is_enabled()
    button_start.click()
    try:
        result_text = WebDriverWait(driver, 20).until(
            ec.visibility_of_element_located((By.ID, 'finish'))
        ).text
    except TimeoutException:
        assert False, "Timeout: The expected current text did not appear in time"

    finish_phrase = 'Hello World!'
    print(f"Current Phrase is displayed correctly: {result_text}")
    assert result_text == finish_phrase, f"Expected {finish_phrase}, got '{result_text}'"
