from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains


def wait_for_element(driver, by, element, timeout=10, parent=None):
    context = parent if parent else driver
    return WebDriverWait(context, timeout).until(EC.visibility_of_element_located((by, element)))


def opening_product_in_new_tab(driver, product_card):
    ActionChains(driver).key_down(Keys.COMMAND).click(product_card).key_up(Keys.COMMAND).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])


def find_product_card_and_get_name_and_price(driver):
    product_card = wait_for_element(driver, By.XPATH, "//div[@class='card h-100'][.//a[text()='Samsung galaxy s6']]")

    card_name_element = wait_for_element(driver, By.XPATH, ".//h4[@class='card-title']/a", parent=product_card)
    card_price_element = wait_for_element(driver, By.XPATH, ".//h5", parent=product_card)

    card_name = card_name_element.text
    card_price = card_price_element.text

    return product_card, card_name, card_price


def find_product_and_get_name_and_price(driver):
    product_content = wait_for_element(driver, By.ID, "tbodyid")
    product_name_element = wait_for_element(driver, By.XPATH, './/h2[@class="name"]',
                                            parent=product_content)
    product_price_element = wait_for_element(driver, By.XPATH, './/h3[@class="price-container"]',
                                             parent=product_content)

    product_name = product_name_element.text
    product_price = product_price_element.text.split()[0]

    return product_content, product_name, product_price


def find_add_to_cart_button_and_click(content):
    add_to_cart_button = content.find_element(By.XPATH, '//a[@class="btn btn-success btn-lg"]')
    add_to_cart_button.click()


def wait_for_alert_and_accept(driver):
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = Alert(driver)
    alert.accept()


def close_active_tab_and_switch_to_another(driver):
    tabs = driver.window_handles
    driver.close()
    driver.switch_to.window(tabs[0])


def find_cart_button_and_click(driver):
    cart_button = driver.find_element(By.ID, 'cartur')
    cart_button.click()


def find_product_in_cart_and_get_name_and_price(driver):
    products_in_cart = wait_for_element(driver, By.XPATH, '//tr[@class="success"]')

    product_name_in_cart_element = wait_for_element(driver, By.XPATH, ".//td[text()='Samsung galaxy s6']",
                                                    parent=products_in_cart)

    product_price_in_cart_element = wait_for_element(driver, By.XPATH, ".//td[text()='360']", parent=products_in_cart)

    product_name_in_cart = product_name_in_cart_element.text
    product_price_in_cart = product_price_in_cart_element.text

    return product_name_in_cart, product_price_in_cart
