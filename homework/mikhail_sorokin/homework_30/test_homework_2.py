from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestHomeWorkTwo:
    START_BUTTON = (By.XPATH, "//div[@id='start']/button[text()='Start']")
    FINISH = (By.XPATH, "//div[@id='finish']/h4")

    def test_homework_2(self, driver):
        driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
        wait = WebDriverWait(driver, 15)
        start_button = wait.until(EC.element_to_be_clickable(self.START_BUTTON))
        start_button.click()
        finish_element = wait.until(EC.visibility_of_element_located(self.FINISH))
        assert finish_element.text == "Hello World!"
