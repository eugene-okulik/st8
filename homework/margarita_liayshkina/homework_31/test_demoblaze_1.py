from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_demoblaze(driver):
    driver.get('https://www.demoblaze.com/index.html')
    link = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, "a[href='prod.html?idp_=1']"))
    )
    assert link is not None, "Product link is not visible on the main page"
    ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()

    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    assert driver.current_url.endswith('prod.html?idp_=1'), "The new window did not open the expected product page"

    addcard_button = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, "//a[@onclick='addToCart(1)']"))
    )
    addcard_button.click()
    WebDriverWait(driver, 10).until(ec.alert_is_present())
    alert = Alert(driver)
    alert.accept()

    driver.close()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[0])
    button_cart = WebDriverWait(driver, 20).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, "a[href='cart.html']"))
    )
    button_cart.click()

    WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, '//tr[@class="success"]')))
    expected_name_product = "Samsung galaxy s6"
    product_cart_name = driver.find_element(By.XPATH,  ".//td[text()='Samsung galaxy s6']")
    assert product_cart_name.text== expected_name_product, f"Expected result '{expected_name_product}', but found {product_cart_name.text}"
