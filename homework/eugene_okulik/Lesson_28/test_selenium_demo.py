import time

from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_demo(driver):
    # driver = webdriver.Firefox()
    driver.get('https://www.google.com/')
    # driver.maximize_window()
    # driver.set_window_size(500, 300)
    # time.sleep(2)
    assert driver.current_url == 'https://www.google.com/'
    assert driver.title == 'Google'
    # driver.quit()


def test_google(driver):
    search_phrase = 'cat'
    driver.get('https://www.google.com/')
    search_field = driver.find_element(By.NAME, 'q')
    search_field.send_keys(search_phrase)
    # search_field.send_keys(Keys.ENTER)
    search_field.submit()
    time.sleep(1)
    assert driver.title.startswith(search_phrase)
