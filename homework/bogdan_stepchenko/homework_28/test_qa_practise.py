import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.parametrize('search_phrase', ['123', 'HelloWorld', 'H_e_l_l_o'])
def test_input_output(driver, search_phrase):
    driver.get('https://www.qa-practice.com/elements/input/simple')

    search_field = driver.find_element(By.NAME, 'text_string')
    search_field.send_keys(search_phrase)
    search_field.submit()
    time.sleep(1)   # waiting for updating data on web-page

    result_element = driver.find_element(By.ID, 'result-text')

    assert result_element.text == search_phrase
