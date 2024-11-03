import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    # неявное ожидание - длится сколько нужно для кейса, если найдет сразу, то ждать не будет
    driver.implicitly_wait(100)
    yield driver
    driver.quit()


def test_language_selector_hw_1(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    selector = driver.find_element(By.CLASS_NAME, 'form-select')
    dropdown = Select(selector)
    dropdown.select_by_visible_text('Python')
    variant = driver.find_element(By.CSS_SELECTOR, "option[value='1']")
    text = variant.get_attribute('innerText')
    assert selector.is_enabled()
    selector.submit()
    result = driver.find_element(By.CLASS_NAME, 'result-text')
    assert result.text == text


def test_print_hw_2(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    button = driver.find_element(By.XPATH, '//button[contains(text(),"Start")]')
    button.click()
    result = WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.ID, 'finish')))
    assert result.text == 'Hello World!'
