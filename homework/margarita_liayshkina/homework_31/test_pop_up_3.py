from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest



@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def open_pop_up(driver):
    driver.get('https://www.qa-practice.com/elements/popup/iframe_popup')
    button_pop_up = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, './/button[@class="btn btn-primary"]'))
    )
    button_pop_up.click()


def get_text_pop_up(driver):
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.XPATH, '//div[@id="exampleModal"][contains(@class, "show")]'))
    )
    iframe = driver.find_element(By.CSS_SELECTOR, 'iframe.embed-responsive-item')
    driver.switch_to.frame(iframe)
    text_element = driver.find_element(By.ID, 'text-to-copy')
    popup_text = text_element.text
    print("Text to copy:", popup_text)
    assert popup_text.strip() != "", "Text from iframe is empty!"
    driver.switch_to.default_content()
    return popup_text


def fill_and_submit_form(driver, popup_text):
    button_check = WebDriverWait(driver,10).until(
        ec.element_to_be_clickable((By.XPATH, './/button[@type="submit"]'))
    )
    button_check.click()
    field_text = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.XPATH, './/input[@class="textinput textInput form-control"]'))
    )
    field_text.send_keys(popup_text)
    submit_button = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.ID, 'submit-id-submit'))
    )
    submit_button.click()


def check_result(driver):
    correct = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.ID, 'check-result'))
    )
    assert correct.text == "Correct!", f"Expected 'Correct!', but got {correct.text}"


def pop_up(driver):
    open_pop_up(driver)
    popup_text = get_text_pop_up(driver)
    fill_and_submit_form(driver, popup_text)
    result = check_result(driver)

    return result
