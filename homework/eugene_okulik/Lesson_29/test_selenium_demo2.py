import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_by_link(driver):
    driver.get('https://www.qa-practice.com/')
    # link = driver.find_element(By.LINK_TEXT, 'Contact')
    link = driver.find_element(By.PARTIAL_LINK_TEXT, 'ntact')
    link.click()
    time.sleep(3)


def test_tag_name(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    header = driver.find_element(By.TAG_NAME, 'h1')
    # header = driver.find_element(By.CSS_SELECTOR, 'h1')
    print(header.text)
    print(header.get_attribute('innerText'))


def test_class_name(driver):
    driver.get('https://magento.softwaretestingboard.com/')
    # shop_new_yoga_button = driver.find_element(By.CLASS_NAME, 'button')
    # shop_new_yoga_button = driver.find_element(By.CSS_SELECTOR, '.button')
    shop_new_yoga_button = driver.find_element(By.CSS_SELECTOR, '.button.more')
    shop_new_yoga_button.click()
    time.sleep(3)


def test_google(driver):
    search_phrase = 'cat'
    driver.get('https://www.google.com/')
    search_field = driver.find_element(By.CSS_SELECTOR, '[name="q"]')
    search_field.send_keys(search_phrase)


def test_by_id_css(driver):
    driver.get('https://magento.softwaretestingboard.com/')
    search = driver.find_element(By.CSS_SELECTOR, '#search')
    search.send_keys('sss')


def test_css_selector(driver):
    driver.get('https://magento.softwaretestingboard.com/')
    # cart = driver.find_element(By.CSS_SELECTOR, 'a[data-bind="scope: \'minicart_content\'"]')
    cart = driver.find_element(By.CSS_SELECTOR, 'a[class="action showcart"]')
    cart.click()
    time.sleep(3)


def test_xpath(driver):
    driver.get('https://magento.softwaretestingboard.com/')
    # cart = driver.find_element(By.XPATH, '//a[@data-bind="scope: \'minicart_content\'"]')
    cart = driver.find_element(By.XPATH, '//a[@class="action showcart"]')
    print(cart.get_attribute('data-bind'))
    assert cart.get_attribute('data-bind') == "scope: 'minicart_content'"


def test_attributes(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    field = driver.find_element(By.CSS_SELECTOR, '#id_text_string')
    field.send_keys('qwerty')
    print(field.get_attribute('value'))
    field.clear()
    print(field.get_attribute('value') + '\n')
    print(field.value_of_css_property('background-color'))
