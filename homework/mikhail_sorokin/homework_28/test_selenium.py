import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestHomework:
    SUBMIT_INPUT_ID = (By.ID, "id_text_string")
    SUBMIT_RESULT = (By.ID, "result-text")

    def test_homework(self, driver):
        driver.get("https://www.qa-practice.com/elements/input/simple")
        submit_input = driver.find_element(*self.SUBMIT_INPUT_ID)
        submit_input.send_keys("test")
        submit_input.send_keys(Keys.ENTER)
        result = driver.find_element(*self.SUBMIT_RESULT).text
        assert result == "test"
