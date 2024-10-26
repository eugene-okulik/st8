# import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_clear(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    field = driver.find_element(By.CSS_SELECTOR, '#id_text_string')
    field.send_keys('qwertysafgdsf')
    # field.clear()
    # field.send_keys(Keys.CONTROL + 'a')
    # field.send_keys(Keys.BACKSPACE)
    word = field.get_attribute('value')
    for _ in word:
        time.sleep(0.5)
        field.send_keys(Keys.BACKSPACE)
    print(field.get_attribute('value'))
    time.sleep(3)


def test_displayed(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    time.sleep(1)
    req_text = driver.find_element(By.ID, 'req_text')
    # print(req_text.get_attribute('innerText'))
    assert not req_text.is_displayed()
    # assert 'This is a required field' in req_text.get_attribute('innerText')
    driver.find_element(By.ID, 'req_header').click()
    assert req_text.is_displayed()


def test_select_enabled(driver):
    driver.get('https://www.qa-practice.com/elements/button/disabled')
    button = driver.find_element(By.ID, 'submit-id-submit')
    assert not button.is_enabled()
    select_element = driver.find_element(By.ID, 'id_select_state')
    dropdown = Select(select_element)
    dropdown.select_by_visible_text('Enabled')
    assert button.is_enabled()


def test_buttons(driver):
    driver.implicitly_wait(5)
    driver.get('https://demoqa.com/dynamic-properties')
    visible_after = driver.find_element(By.ID, 'visibleAfter')
    visible_after.click()
    enable_after = driver.find_element(By.ID, 'enableAfter')
    assert not enable_after.is_enabled()


def test_enable_after(driver):
    driver.get('https://demoqa.com/dynamic-properties')
    enable_after = driver.find_element(By.ID, 'enableAfter')
    assert not enable_after.is_enabled()
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable(enable_after))
    assert enable_after.is_enabled()


def test_enable_after2(driver):
    driver.get('https://demoqa.com/dynamic-properties')
    wait = WebDriverWait(driver, 10)
    enable_after = wait.until(ec.element_to_be_clickable((By.ID, 'enableAfter')))
    assert enable_after.is_enabled()


def test_cookies(driver):
    driver.get('https://demoblaze.com/')
    time.sleep(0.5)
    driver.add_cookie({'name': 'text', 'value': 'testvalue'})
    print(driver.get_cookies())


def test_elements(driver):
    driver.get('https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html')
    products = driver.find_elements(By.CSS_SELECTOR, '.product-item-link')
    prices = driver.find_elements(By.CSS_SELECTOR, '.price-wrapper >.price')
    prices_values = list(map(lambda price: float(price.text.replace('$', '')), prices))
    print(prices_values)
    print(sorted(prices_values))
    assert prices_values == sorted(prices_values)
    # products[-1].click()
    # products[0].click()
    # products[random.randint(1, 11)].click()
    print(products[-1].text)
