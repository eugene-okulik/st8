import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_homework(driver):
    text = "QA"
    driver.get('https://www.qa-practice.com/elements/input/simple')
    input = driver.find_element(By.NAME, 'text_string')
    input.send_keys(text)
    input.submit()
    result = driver.find_element(By.NAME, 'result')
    assert result.text == f'Your input was:\n{text}'
