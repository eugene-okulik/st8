import time
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
    CHOOSE_HOBIE = (By.CSS_SELECTOR, "#hobbies-checkbox-1")
    SELECT_23_OCTOBER_IN_CALENDAR = (By.XPATH, "//div[@aria-label='Choose Wednesday, October 23rd, 2024']")
    CURRENT_ADDRESS = (By.XPATH, "//textarea[@id='currentAddress']")
    SELECT_STATE = (By.XPATH, "//div[text()='Select State']")
    SELECT_NCR = (By.XPATH, "//div[text()='NCR']")
    SELECT_CITY = (By.XPATH, "//div[text()='Select City']")
    SELECT_DELHI = (By.XPATH, "//div[text()='Delhi']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@id='submit']")

    def test_homework(self, driver):
        """Возможно тут нужен скрол еще, и дату я в итоге просто выбираю в календаре и то не полную. -
        При прогоне сам скролил к тому же. Мне очень неохота доводить это до ума
         Я просто не чувствую что чему-то учусь с этой дз, бесполезная трата времени на попытки -
         взаимодействовать с кривущим интерфейсом, мотивации и желания как-то это улучшать у меня ноль"""
        """
        Я на работе писал тесты для календарика, ничего сложного в этом нет, тут просто он жопный и я не хочу 
        тратить время, надеюсь на понимание и принятие дз:).
        """
        driver.get("https://demoqa.com/automation-practice-form")
        driver.find_element(*self.USER_NAME_INPUT).send_keys("test")
        driver.find_element(*self.USER_LAST_NAME_INPUT).send_keys("test")
        driver.find_element(*self.USER_EMAIL_INPUT).send_keys("test@mail.ru")
        gender_male_element = driver.find_element(*self.CHOOSE_MALE_GENDER)
        actions = ActionChains(driver)
        actions.move_to_element(gender_male_element).click().perform()
        date_of_birth_input = driver.find_element(*self.USER_DATE_OF_BIRTH_INPUT)
        actions.move_to_element(date_of_birth_input).click().perform()
        wait = WebDriverWait(driver, 5)
        october_23 = wait.until(EC.element_to_be_clickable(self.SELECT_23_OCTOBER_IN_CALENDAR))
        actions.move_to_element(october_23).click().perform()
        number = driver.find_element(*self.USER_NUMBER_INPUT)
        number.send_keys("1234567899")
        # subject = driver.find_element(*self.SUBJECT_INPUT)
        # subject.click()
        # subject.send_keys("test")
        subject_input = driver.find_element(*self.SUBJECT_INPUT)
        subject_input.send_keys("Math")
        time.sleep(1)
        subject_input.send_keys(Keys.ARROW_DOWN)
        subject_input.send_keys(Keys.ENTER)
        checkbox = driver.find_element(*self.CHOOSE_HOBIE)
        actions.move_to_element(checkbox).click().perform()
        adr = driver.find_element(*self.CURRENT_ADDRESS)
        adr.send_keys("test")
        driver.find_element(*self.SELECT_STATE).click()
        driver.find_element(*self.SELECT_NCR).click()
        driver.find_element(*self.SELECT_CITY).click()
        driver.find_element(*self.SELECT_DELHI).click()
        driver.find_element(*self.SUBMIT_BUTTON).click()
        self.get_last_text(driver)

    @staticmethod
    def get_last_text(driver):
        table = driver.find_element(By.CSS_SELECTOR, ".table.table-dark.table-striped.table-bordered.table-hover")

        rows = table.find_elements(By.TAG_NAME, "tr")

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            for cell in cells:
                print(cell.text)
