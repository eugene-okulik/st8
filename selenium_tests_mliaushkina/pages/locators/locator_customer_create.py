from selenium.webdriver.common.by import By

FIRST_NAME = (By.CSS_SELECTOR, '#firstname')
SECOND_NAME = (By.CSS_SELECTOR, '#lastname')
EMAIL = (By.CSS_SELECTOR, '#email_address')
PASSWORD = (By.CSS_SELECTOR, '#password')
CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#password-confirmation')
CREATE_ACCOUNT_BUTTON = (By.XPATH, '//*[@id="form-validate"]/div/div[1]/button')
SUCCESS_MESSAGE = (By.XPATH, '//*[text()="Thank you for registering with Main Website Store."]')
EMAIL_ERROR = (By.CSS_SELECTOR, '#email_address-error')
CONFIRM_PASSWORD_ERROR = (By.CSS_SELECTOR, '#password-confirmation-error')
