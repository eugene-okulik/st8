import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select


class TestHomeWorkOne:
    FIRST_PRODUCT = (By.XPATH, "//a[contains(text(), 'Samsung galaxy s6')]")
    ADD_TO_CART = (By.XPATH, "//a[contains(text(), 'Add to cart')]")
    CART = (By.XPATH, "//a[contains(text(), 'Cart')]")

    # в теории работает, корзина не грузится так что не могу убедиться
    def test_demoblaze_homework(self, driver):
        driver.get('https://www.demoblaze.com/index.html')
        wait = WebDriverWait(driver, 10)
        first_product = wait.until(EC.element_to_be_clickable(self.FIRST_PRODUCT))
        driver.execute_script("window.open(arguments[0].href, '_blank');", first_product)
        driver.switch_to.window(driver.window_handles[1])
        ad_to_cart_button = wait.until(EC.element_to_be_clickable(self.ADD_TO_CART))
        ad_to_cart_button.click()
        driver.switch_to.window(driver.window_handles[0])
        cart = wait.until(EC.element_to_be_clickable(self.CART))
        cart.click()
        tbody = driver.find_element(By.ID, "tbodyid")
        tds = tbody.find_elements(By.TAG_NAME, "td")
        text_to_check = "Samsung galaxy s6"
        for td in tds:
            assert text_to_check in td.text
            print(f"Найден текст: {text_to_check}")

