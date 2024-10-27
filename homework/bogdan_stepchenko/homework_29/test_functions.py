import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def fill_first_name(driver, name):
    first_name = driver.find_element(By.ID, 'firstName')
    first_name.send_keys(name)


def fill_last_name(driver, surname):
    last_name = driver.find_element(By.ID, 'lastName')
    last_name.send_keys(surname)


def fill_email(driver, email):
    user_email = driver.find_element(By.ID, 'userEmail')
    user_email.send_keys(email)


def fill_phone(driver, phone):
    user_phone = driver.find_element(By.ID, 'userNumber')
    user_phone.send_keys(phone)


def fill_address(driver, address):
    current_address = driver.find_element(By.ID, 'currentAddress')
    current_address.send_keys(address)


def select_random_gender(driver):
    gender_radio_buttons = [
        (By.CSS_SELECTOR, 'label[for="gender-radio-1"]'),  # Male
        (By.CSS_SELECTOR, 'label[for="gender-radio-2"]'),  # Female
        (By.CSS_SELECTOR, 'label[for="gender-radio-3"]')  # Other
    ]
    selected_locator = random.choice(gender_radio_buttons)
    selected_radio_button = driver.find_element(*selected_locator)
    selected_radio_button.click()


def select_random_hobby(driver):
    hobbies_checkboxes = [
        (By.CSS_SELECTOR, 'label[for="hobbies-checkbox-1"]'),   # Sports
        (By.CSS_SELECTOR, 'label[for="hobbies-checkbox-1"]'),   # Reading
        (By.CSS_SELECTOR, 'label[for="hobbies-checkbox-1"]')    # Music
    ]
    selected_locator = random.choice(hobbies_checkboxes)
    selected_checkbox = driver.find_element(*selected_locator)
    selected_checkbox.click()


def select_random_date(driver):
    driver.find_element(By.ID, 'dateOfBirthInput').click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".react-datepicker__month-select")))

    random_year = random.randint(1950, 2024)
    random_month = random.randint(0, 11)
    random_day = random.randint(1, 29)

    month_select = driver.find_element(By.CSS_SELECTOR, ".react-datepicker__month-select")
    month_select.click()
    month_option = month_select.find_element(By.CSS_SELECTOR, f"option[value='{random_month}']")
    month_option.click()

    year_select = driver.find_element(By.CSS_SELECTOR, ".react-datepicker__year-select")
    year_select.click()
    year_option = year_select.find_element(By.CSS_SELECTOR, f"option[value='{random_year}']")
    year_option.click()

    day_element = driver.find_element(By.XPATH,
                                      f"//div[contains(@class, 'react-datepicker__day') and text()='{random_day}']")
    day_element.click()


def select_subject(driver, subject):
    subjects = driver.find_element(By.ID, 'subjectsInput')
    subjects.click()
    subjects.send_keys(subject)
    subjects.send_keys(Keys.ENTER)


def select_state(driver, state_name):
    state_container = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'state'))
    )
    state_container.click()

    input_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'react-select-3-input'))
    )

    input_field.send_keys(state_name)
    input_field.send_keys(Keys.ENTER)


def select_city(driver, city_name):
    state_container = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'city'))
    )
    state_container.click()

    input_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'react-select-4-input'))
    )

    input_field.send_keys(city_name)
    input_field.send_keys(Keys.ENTER)


def print_results(driver, expected_first_name, expected_last_name, expected_email, expected_subject,
                  expected_phone, expected_address, expected_state, expected_city):
    expected_values = {
        "Student Name": f"{expected_first_name} {expected_last_name}",
        "Student Email": expected_email,
        "Mobile": expected_phone,
        "Subjects": expected_subject,
        "Address": expected_address,
        "State and City": f'{expected_state} {expected_city}'
    }
    for row in range(1, 11):
        name = f"/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[{row}]/td[1]"
        value = f"/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[{row}]/td[2]"

        name_element = driver.find_element(By.XPATH, name)
        value_element = driver.find_element(By.XPATH, value)
        print(f"{name_element.text}: {value_element.text}")

        if name_element is expected_values.keys():
            assert value_element.text == expected_values[name_element.text]
