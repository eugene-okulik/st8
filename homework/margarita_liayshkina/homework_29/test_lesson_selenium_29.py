import  time
import  selenium
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys


def test_enter_e_word(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    assert driver.current_url == 'https://demoqa.com/automation-practice-form', "URL does not mathed!"

    time.sleep(3)

    try:
        try:
            driver.find_element(By.ID, 'firstName').send_keys('Veronika')
        except NoSuchElementException:
            print("Field'First Name' not found")

        try:
            driver.find_element(By.ID, 'lastName').send_keys('Ivanova')
        except NoSuchElementException:
                print("Field 'Last Name' not found")

        try:
            driver.find_element(By.XPATH, '//label[contains(text(), "Female")]').click()
            print("Найден пол")
        except NoSuchElementException:
            print("Field 'Gender' not found")

        try:
            driver.find_element(By.ID, 'userEmail').send_keys('veronika123@mail.ru')
        except NoSuchElementException:
            print("Field 'Email' not found")

        try:
            driver.find_element(By.ID, 'userNumber').send_keys('13458907623')
        except NoSuchElementException:
            print("Field 'Mobile' not found")

        try:
            date_of_birth = driver.find_element(By.CSS_SELECTOR, '#dateOfBirthInput')
            date_of_birth.click()
            time.sleep(1)
        except NoSuchElementException:
            print("Field'Date of Birth' not found")

        try:
            month_select = driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select')
            month_select.click()
            month_select.send_keys('May')
            time.sleep(1)
        except NoSuchElementException:

            print("Field month not found")
        try:
            year_select = driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select')
            year_select.click()
            year_select.send_keys('1995')
            time.sleep(1)
        except NoSuchElementException:
            print("Field year select not found")

        try:
            day_select = driver.find_element(By.CSS_SELECTOR, ".react-datepicker__day--015")
            day_select.click()
        except NoSuchElementException:
            print("No day selection found")

        try:
            subject_field = driver.find_element(By.CSS_SELECTOR, '#subjectsInput')
            subject_field.send_keys('Chemistry')
            subject_field.send_keys(Keys.RETURN)
            print("заполнено Subj")
            time.sleep(1)
            subject_field.send_keys()
        except NoSuchElementException:
            print("field 'Subjects' not found")

        try:
            time.sleep(2)
            hobbies_field = driver.find_element(By.ID, 'hobbies-checkbox-2')
            actions = ActionChains(driver)
            actions.click(hobbies_field).perform()
            time.sleep(1)
        except NoSuchElementException:
            print("Field 'Hobbies' not found")


        try:
            driver.find_element(By.ID, "currentAddress").send_keys("123 Street-123")
            time.sleep(1)
        except NoSuchElementException:
            print("Field 'Current Address' not found")

        try:
            state_input = driver.find_element(By.ID, "react-select-3-input")
            time.sleep(1)
            state_input.click()
            state_input.send_keys("NCR")
            print("заполнено NSR")
            time.sleep(1)
            state_input.send_keys()
        except NoSuchElementException:
            print("Field 'State' not found")

        try:
            city_input = driver.find_element(By.ID, "react-select-4-input")
            city_input.click()
            city_input.send_keys("Delhi")
            time.sleep(1)
            city_input.send_keys()

        except NoSuchElementException:
            print("Field 'City' not found")

        try:
            subimt_button = driver.find_element(By.ID, "submit")
            actions = ActionChains(driver)
            actions.click(subimt_button).perform()
            print("The form has been submitted successfully")
            time.sleep(5)
        except NoSuchElementException:
            print("'Submit' button not found.")

    except Exception as e:
        print(f"Error: {e}")


