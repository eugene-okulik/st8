import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_add_items(driver):
    driver.get('https://www.demoblaze.com/index.html')
    new_product = driver.find_element(By.CSS_SELECTOR, 'a[href="prod.html?idp_=1"]')
    ActionChains(driver).key_down(Keys.CONTROL).click(new_product).key_up(Keys.CONTROL).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    add_to_cart = driver.find_element(By.CSS_SELECTOR, "a[onclick='addToCart(1)']")
    add_to_cart.click()
    driver.switch_to.window(tabs[0])
    cart = driver.find_element(By.ID, 'cartur')
    cart.click()
    products = driver.find_element(By.CLASS_NAME, 'success')
    text = products.get_attribute('innerText')
    assert text.startswith('\tSamsung galaxy s6\t')


def test_compare_products(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    products = driver.find_elements(By.XPATH, './/div[@class="products wrapper grid products-grid"]')
    product_one = products[0].find_element(By.XPATH, "//li[contains(@class, 'product-item')][1]")
    time.sleep(5)
    compare_button = product_one.find_element(By.XPATH, '//*[@class="action tocompare"]')
    actions = ActionChains(driver)
    actions.move_to_element(product_one)
    actions.click(compare_button)
    actions.perform()
    compare_cart = driver.find_element(By.XPATH, ".//ol[@id='compare-items']//a")
    assert compare_cart.text == 'Push It Messenger Bag'


def test_iframe(driver):
    driver.get('https://www.qa-practice.com/elements/popup/iframe_popup')
    button = driver.find_element(By.XPATH, "//button[@class='btn btn-primary' and contains(text(),'Launch Pop-Up')]")
    button.click()
    iframe = driver.find_element(By.CSS_SELECTOR, 'iframe')
    driver.switch_to.frame(iframe)
    text_to_copy = driver.find_element(By.ID, 'text-to-copy')
    text = text_to_copy.get_attribute('innerText')
    driver.switch_to.default_content()
    check_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    check_button.click()
    input = driver.find_element(By.XPATH, "//input[@name='text_from_iframe']")
    input.send_keys(text)
    submit_button = driver.find_element(By.ID, 'submit-id-submit')
    submit_button.click()
    success = driver.find_element(By.ID, 'check-result').text
    assert success == 'Correct!'
