import  time
from time import sleep

import  selenium
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_my_site(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    assert driver.current_url == 'https://demoqa.com/automation-practice-form', "URL does not match!"
    time.sleep(1)

    check_firstname(driver)
    check_lastname(driver)
    check_female(driver)
    check_email(driver)
    check_phone(driver)
    check_date_bitrthday(driver)
    check_subject(driver)
    check_hobbies(driver)
    check_address(driver)
    check_state(driver)
    check_city(driver)
    check_submit(driver)


def check_firstname(driver):
    try:
        first_name = driver.find_element(By.ID, 'firstName')
        first_name.send_keys('Veronika')
        assert first_name.get_attribute('value') == 'Veronika', "First name not entered correctly"
    except NoSuchElementException:
        assert False, "Element 'firstName' not found on the page"


def check_lastname(driver):
    try:
        last_name = driver.find_element(By.ID, 'lastName')
        last_name.send_keys('Ivanova')
        time.sleep(1)
        assert last_name.get_attribute('value') == 'Ivanova', "Last name not entered correctly"
    except NoSuchElementException:
        assert False, "Element 'lastName' not found on the page"


def check_female(driver):
    try:
        gender_female = driver.find_element(By.XPATH, '//label[contains(text(), "Female")]')
        gender_female.click()
        time.sleep(1)
        assert gender_female.is_displayed(), "Gender 'Female' not selected"
    except NoSuchElementException:
        assert False, "Element 'Gender Female' not found on the page"


def check_email(driver):
    try:
        email_field = driver.find_element(By.ID, 'userEmail')
        email_field.send_keys('veronika123@mail.ru')
        time.sleep(1)
        assert email_field.get_attribute('value') == 'veronika123@mail.ru', "Email not entered correctly"
    except NoSuchElementException:
        assert False, "Element 'Email' not found on the page"


def check_phone(driver):
    try:
        phone_field = driver.find_element(By.ID, 'userNumber')
        phone_field.send_keys('1345890762')
        time.sleep(1)
        assert phone_field.get_attribute('value') == '1345890762', "Mobile number not entered correctly"
    except NoSuchElementException:
        assert False, "Element 'Phone' not found on the page"


def check_date_bitrthday(driver):
    try:
        date_of_birth = driver.find_element(By.CSS_SELECTOR, '#dateOfBirthInput')
        date_of_birth.click()
        time.sleep(1)

        month_select = driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select')
        month_select.send_keys('May')
        time.sleep(1)

        year_select = driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select')
        year_select.send_keys('1995')
        time.sleep(1)

        day_select = driver.find_element(By.CSS_SELECTOR, ".react-datepicker__day--015")
        day_select.click()

        selected_date = date_of_birth.get_attribute('value')
        assert selected_date == '15 May 1995', f"Date of birth not set correctly, got {selected_date}"
    except NoSuchElementException as e:
        assert False, f"Date selection element not found: {str(e)}"


def  check_subject(driver):
    try:
        subject_field = driver.find_element(By.CSS_SELECTOR, '#subjectsInput')
        subject_field.send_keys('Chemistry')
        subject_field.send_keys(Keys.RETURN)
        time.sleep(1)
        selected_subject = driver.find_element(By.XPATH, "//div[contains(@class, 'subjects-auto-complete__multi-value__label')]").text
        assert selected_subject == 'Chemistry', "Subject not entered correctly"
    except NoSuchElementException:
        assert False, "Element 'Subject' not found on the page"


def check_hobbies(driver):
    try:
        hobbies_checkbox = driver.find_element(By.ID, 'hobbies-checkbox-2')
        actions = ActionChains(driver)
        actions.click(hobbies_checkbox).perform()
        time.sleep(1)
        assert hobbies_checkbox.is_selected(), "Hobby checkbox not selected"
    except NoSuchElementException:
        assert False, "Element 'Hobbies' not found on the page"



def check_address(driver):
    try:
        address_field = driver.find_element(By.ID, "currentAddress")
        address_field.send_keys("123 Street-123")
        time.sleep(1)
        assert address_field.get_attribute('value') == "123 Street-123", "Current Address not entered correctly"
    except NoSuchElementException:
        assert False, "Element 'Address' not found on the page"


def check_state(driver):
    try:
        state_dropdown = driver.find_element(By.ID, 'state')
        state_dropdown.click()
        time.sleep(1)

        input_field = driver.find_element(By.ID, 'react-select-3-input')
        input_field.send_keys("NCR")
        input_field.send_keys(Keys.ENTER)
        time.sleep(1)
        selected_state = driver.find_element(By.CSS_SELECTOR, '#state .css-1uccc91-singleValue').text
        assert selected_state== 'NCR', "City not selected correctly"
    except NoSuchElementException:
        assert False, "Element 'State' not found on the page"


def check_city(driver):
    try:
        city_input = driver.find_element(By.ID, "react-select-4-input")
        city_input.send_keys("Delhi")
        city_input.send_keys(Keys.RETURN)
        time.sleep(1)
        selected_city = driver.find_element(By.CSS_SELECTOR, '#city .css-1uccc91-singleValue').text
        assert selected_city == 'Delhi', "City not selected correctly"
    except NoSuchElementException:
        assert False, "Element 'City' not found on the page"


def check_submit(driver):
    try:
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()
        modal_content = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'modal-content'))
        )
        assert modal_content.is_displayed(), "Form submission confirmation modal not displayed"
        rows = modal_content.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) == 2:
                print(f"Name: {cells[0].text}, value: {cells[1].text}")
    except NoSuchElementException:
        assert False, "Submit button not found on the page"
    except TimeoutException:
        assert False, "Modal content did not appear within the expected time"
