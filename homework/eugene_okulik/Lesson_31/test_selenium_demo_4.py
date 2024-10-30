import time

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
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()


def test_elements(driver):
    driver.get('https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html')
    product_cards = driver.find_elements(By.CSS_SELECTOR, '[data-container="product-grid"]')
    price1 = product_cards[0].find_element(By.CSS_SELECTOR, '.price').text
    last_price = product_cards[-1].find_element(By.CSS_SELECTOR, '.price').text
    prices = [product.find_element(By.CSS_SELECTOR, '.price').text for product in product_cards]
    print(price1)
    print(last_price)
    print(prices)


def test_tabs(driver):
    driver.get('https://www.qa-practice.com/elements/new_tab/link')
    link = driver.find_element(By.CSS_SELECTOR, '#new-page-link')
    link.click()
    time.sleep(1)
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    result = driver.find_element(By.CSS_SELECTOR, '#result-text')
    assert result.text == 'I am a new page in a new tab'
    driver.close()
    time.sleep(1)
    driver.switch_to.window(tabs[0])
    link.click()
    time.sleep(1)


def test_stale(driver):
    driver.get('https://www.qa-practice.com/elements/button/simple')
    button = driver.find_element(By.CSS_SELECTOR, '#submit-id-submit')
    button.click()
    result = driver.find_element(By.CSS_SELECTOR, '#result-text')
    assert result.text == 'Submitted'
    button = driver.find_element(By.CSS_SELECTOR, '#submit-id-submit')
    button.click()


def test_iframe(driver):
    driver.get('https://www.qa-practice.com/elements/iframe/iframe_page')
    iframe = driver.find_element(By.CSS_SELECTOR, 'iframe')
    driver.switch_to.frame(iframe)
    burger_button = driver.find_element(By.CSS_SELECTOR, '.navbar-toggler-icon')
    burger_button.click()
    time.sleep(1)
    driver.switch_to.default_content()
    tab_iframe = driver.find_element(By.CSS_SELECTOR, '.tab.active>a')
    tab_iframe.click()
    time.sleep(1)


def test_alert(driver):
    driver.get('https://www.qa-practice.com/elements/alert/alert')
    button = driver.find_element(By.CSS_SELECTOR, '.a-button')
    button.click()
    time.sleep(1)
    WebDriverWait(driver, 10).until(ec.alert_is_present())
    alert = Alert(driver)
    alert.accept()
    time.sleep(1)


def test_hover(driver):
    driver.get('https://magento.softwaretestingboard.com/')
    men = driver.find_element(By.CSS_SELECTOR, '#ui-id-5')
    tops = driver.find_element(By.CSS_SELECTOR, '#ui-id-17')
    jackets = driver.find_element(By.CSS_SELECTOR, '#ui-id-19')
    # ActionChains(driver).move_to_element(men).move_to_element(tops).click(jackets).perform()
    actions = ActionChains(driver)
    actions.move_to_element(men)
    actions.move_to_element(tops)
    actions.click(jackets)
    actions.perform()
    time.sleep(2)


def test_key_down(driver):
    driver.get('https://www.qa-practice.com/')
    link = driver.find_element(By.LINK_TEXT, 'Homepage')
    ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
    time.sleep(2)


def test_dnd(driver):
    driver.get('https://www.qa-practice.com/elements/dragndrop/boxes')
    drag_me = driver.find_element(By.CSS_SELECTOR, '#rect-draggable')
    drop_here = driver.find_element(By.CSS_SELECTOR, '#rect-droppable')
    # ActionChains(driver).drag_and_drop(drag_me, drop_here).perform()
    actions = ActionChains(driver)
    actions.click_and_hold(drag_me)
    actions.move_to_element(drop_here)
    actions.release()
    actions.perform()
    time.sleep(2)


def test_upload(driver):
    driver.get('https://the-internet.herokuapp.com/upload')
    file_upload = driver.find_element(By.CSS_SELECTOR, '#file-upload')
    file_upload.send_keys('/home/eugene/Downloads/yt.svg')
    time.sleep(5)
