from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import NoSuchElementException
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def softwaretestingboard(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    products = WebDriverWait(driver, 10).until(
        ec.visibility_of_all_elements_located((By.XPATH, "//li[contains(@class, 'product-item')]"))
    )
    try:
        first_product = products[0]
        actions = ActionChains(driver)
        actions.move_to_element(first_product).click().perform()

        compare_button = WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, '//*[@class="action tocompare"]'))
        )
        compare_button.click()

        compare_products = WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, '//a[@title ="Compare Products"]/span'))
        )
        print(f"compare_products.text = {compare_products.text}")
        assert compare_products.text == "1 item", "Expected"

    except NoSuchElementException:
        assert False, "Elements not found"
