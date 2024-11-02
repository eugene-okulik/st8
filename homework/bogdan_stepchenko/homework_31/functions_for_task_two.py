from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from functions_for_task_one import wait_for_element


def wait_for_1st_product_and_get_name(driver):
    products = wait_for_element(driver, By.XPATH, './/div[@class="products wrapper grid products-grid"]')

    first_product_element = wait_for_element(driver, By.XPATH, "//li[contains(@class, 'product-item')][1]",
                                             parent=products)
    first_product_name_element = wait_for_element(driver, By.XPATH, ".//a[@class='product-item-link']",
                                                  parent=first_product_element)

    return first_product_element, first_product_name_element.text


def hover_on_card_and_click_compare_button(driver, product):
    actions = ActionChains(driver)
    actions.move_to_element(product).perform()

    add_to_compare_button = wait_for_element(driver, By.XPATH,
                                             "//li[contains(@class, 'product-item')][1]//a[@class='action tocompare']")
    add_to_compare_button.click()


def find_compare_count_and_product_name(driver):
    compare_count_element = wait_for_element(driver, By.XPATH, './/span[@class="counter qty"]')
    compare_count = compare_count_element.text

    compare_item_name_element = wait_for_element(driver, By.XPATH, ".//ol[@id='compare-items']//a")
    compare_item_name = compare_item_name_element.text
    return compare_count, compare_item_name
