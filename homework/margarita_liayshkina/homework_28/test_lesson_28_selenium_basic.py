import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_search_site(driver):

    driver.get('https://www.qa-practice.com/elements/input/simple')
    assert driver.current_url == 'https://www.qa-practice.com/elements/input/simple'


def test_enter_e_word(driver):

    driver.get('https://www.qa-practice.com/elements/input/simple')
    search_field = driver.find_element(By.NAME, 'text_string')
    search_phrase = 'Hello'
    search_field.send_keys(search_phrase)
    search_field.submit()
    time.sleep(2)
    check_input_word = driver.find_element(By.ID, 'result-text')
    assert check_input_word.text == search_phrase, f"word not found {search_phrase}"
    print(f"Current phrase found: {search_phrase}")
