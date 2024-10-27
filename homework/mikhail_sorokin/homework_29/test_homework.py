import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class TestHomework:
    USER_NAME_INPUT = (By.XPATH, "//input[@id='firstName']")
    USER_LAST_NAME_INPUT = (By.XPATH, "//input[@id='lastName']")
    USER_EMAIL_INPUT = (By.XPATH, "//input[@id='userEmail']")
    CHOOSE_MALE_GENDER = (By.XPATH, "//input[@id='gender-radio-1']")
    USER_NUMBER_INPUT = (By.XPATH, "//input[@id='userNumber']")
    USER_DATE_OF_BIRTH_INPUT = (By.XPATH, "//input[@id='dateOfBirthInput']")
    SUBJECT_INPUT = (By.XPATH, "//input[@id='subjectsInput']")
    CHOOSE_HOBIE = (By.XPATH, "//input[@id='hobbies-checkbox-1']")
    SELECT_23_OCTOBER_IN_CALENDAR = (By.XPATH, "//div[@aria-label='Choose Wednesday, October 23rd, 2024']")

    def test_homework(self, driver):
        driver.get("https://demoqa.com/automation-practice-form")
        driver.find_element(*self.USER_NAME_INPUT).send_keys("test")
        driver.find_element(*self.USER_LAST_NAME_INPUT).send_keys("test")
        driver.find_element(*self.USER_EMAIL_INPUT).send_keys("test@mail.ru")
        gender_male_element = driver.find_element(*self.CHOOSE_MALE_GENDER)
        actions = ActionChains(driver)
        actions.move_to_element(gender_male_element).click().perform()
        #date_of_birth_input = driver.find_element(*self.USER_DATE_OF_BIRTH_INPUT)
        #actions.move_to_element(date_of_birth_input).click()
        #driver.find_element(self.SELECT_23_OCTOBER_IN_CALENDAR).click()
        subject = driver.find_element(self.SUBJECT_INPUT)
        subject.send_keys("test")
        #date_of_birth_input.send_keys(Keys.COMMAND + 'a')
        #date_of_birth_input.send_keys(Keys.BACKSPACE)
        #actions.send_keys(Keys.COMMAND + 'v')
        time.sleep(10)
