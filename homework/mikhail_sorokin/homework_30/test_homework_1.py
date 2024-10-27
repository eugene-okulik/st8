from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class TestHomeWorkOne:
    LANGUAGE_SELECTOR = (By.XPATH, "//select[@id='id_choose_language']")
    CHOOSE_PYTHON = (By.XPATH, "//select/option[text()='Python']")
    SUBMIT_BUTTON = (By.XPATH, "//input[@id='submit-id-submit']")
    MULTIPLE_SELECT = (By.XPATH, "//li[@class='tab']")
    RESULT = (By.XPATH, "//div/p[@id='result-text']")

    def test_homework_1(self, driver):
        driver.get("https://www.qa-practice.com/elements/select/single_select")
        language_selector = driver.find_element(*self.LANGUAGE_SELECTOR)
        select = Select(language_selector)
        select.select_by_visible_text("Python")
        driver.find_element(*self.SUBMIT_BUTTON).click()
        result = driver.find_element(*self.RESULT).text
        assert result == "Python"
