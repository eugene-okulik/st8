from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class TestHomeWorkOne:
    FIRST_PRODUCT_CART = (By.XPATH, "(//div[@class='product-item-info'])[1]")
    ADD_TO_COMPARE = (By.XPATH, "(//a[@aria-label='Add to Compare'])[1]")
    COMPARE_LIST = (By.XPATH, "//ol[@id='compare-items']//strong[@class='product-item-name']")

    def test_luma_homework(self, driver):
        driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
        wait = WebDriverWait(driver, 10)
        actions = ActionChains(driver)
        first_product = wait.until(EC.element_to_be_clickable(self.FIRST_PRODUCT_CART))
        actions.move_to_element(first_product).perform()
        add_to_compare_button = wait.until(EC.element_to_be_clickable(self.ADD_TO_COMPARE))
        actions.send_keys(Keys.PAGE_DOWN).perform()
        add_to_compare_button.click()
        compare_list = wait.until(EC.visibility_of_element_located(self.COMPARE_LIST))
        compare_item = compare_list.text
        assert compare_item == 'Push It Messenger Bag'