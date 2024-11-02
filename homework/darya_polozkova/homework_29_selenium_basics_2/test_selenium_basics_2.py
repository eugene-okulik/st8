import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_page(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    name = driver.find_element(By.ID, 'firstName')
    surname = driver.find_element(By.ID, 'lastName')
    name.send_keys('Qa name')
    surname.send_keys('Qa surname')
    email = driver.find_element(By.ID, 'userEmail')
    email.send_keys('test@qa.com')
    gender = driver.find_element(By.XPATH, '//label[@class="custom-control-label" and text()="Female"]')
    gender.click()
    phone = driver.find_element(By.XPATH, '//input[@id="userNumber"]')
    phone.send_keys('375111222455')
    birthday_picker = driver.find_element(By.CSS_SELECTOR, 'input[id="dateOfBirthInput"]')
    birthday_picker.click()
    birthday_picker.send_keys(Keys.CONTROL + Keys.PAGE_DOWN)
    month = driver.find_element(By.CSS_SELECTOR, ".react-datepicker__month-select")
    month.click()
    birthday_month = driver.find_element(By.XPATH, "//option[@value=9]")
    birthday_month.click()
    year = driver.find_element(By.CSS_SELECTOR, '.react-datepicker__year-select')
    year.click()
    birthday_year = driver.find_element(By.XPATH, '//option[@value=1989]')
    birthday_year.click()
    day = driver.find_element(By.CSS_SELECTOR, '.react-datepicker__day.react-datepicker__day--021')
    day.click()
    hobby = driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")
    hobby.click()
    address = driver.find_element(By.XPATH, '//textarea[@id="currentAddress"]')
    address.send_keys('Planet Earth, Best City')
    address.send_keys(Keys.CONTROL + Keys.END)
    state = driver.find_element(By.XPATH, '//*[text()="Select State"]')
    state.click()
    selected_state = driver.find_element(By.CSS_SELECTOR, 'div[id="react-select-3-option-1"]')
    selected_state.click()
    city = driver.find_element(By.XPATH, '//*[text()="Select City"]')
    city.click()
    selected_city = driver.find_element(By.CSS_SELECTOR, 'div[id="react-select-4-option-0"]')
    selected_city.click()
    submit = driver.find_element(By.ID, 'submit')
    submit.click()
    submitted_form = driver.find_element(By.TAG_NAME, 'tbody')
    print(submitted_form.text)
