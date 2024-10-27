import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from test_functions import fill_first_name, fill_last_name, fill_email, fill_phone, \
    fill_address, select_random_gender, select_random_hobby, select_subject, \
    select_state, select_city, select_random_date, print_results
from test_data import expected_address, expected_email, expected_state, expected_city, \
    expected_phone, expected_subject, expected_last_name, expected_first_name


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.close()


def test_fill_all_fields(driver):
    driver.get('https://demoqa.com/automation-practice-form')

    fill_first_name(driver, expected_first_name)
    fill_last_name(driver, expected_last_name)
    fill_email(driver, expected_email)
    select_random_gender(driver)
    fill_phone(driver, expected_phone)
    select_random_date(driver)
    select_subject(driver, expected_subject)
    select_random_hobby(driver)
    fill_address(driver, expected_address)
    select_state(driver, expected_state)
    select_city(driver, expected_city)

    driver.find_element(By.ID, 'submit').click()
    print_results(driver, expected_first_name, expected_last_name, expected_email, expected_subject,
                  expected_phone, expected_address, expected_state, expected_city)
