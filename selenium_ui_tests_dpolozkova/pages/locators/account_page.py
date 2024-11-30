from selenium.webdriver.common.by import By


FIRST_NAME = (By.CSS_SELECTOR, '#firstname')
LAST_NAME = (By.CSS_SELECTOR, '#lastname')
EMAIL = (By.CSS_SELECTOR, 'input[title="Email"]')
PWD = (By.CSS_SELECTOR, 'input[title="Password"]')
CONFIRM_PWD = (By.CSS_SELECTOR, 'input[title="Confirm Password"]')
CREATE_ACCOUNT_BTN = (By.CSS_SELECTOR, 'button[title="Create an Account"]')
SUCCESS_MSG = (By.XPATH, '//*[text()="Thank you for registering with Main Website Store."]')
CREATED_ACC = (By.CSS_SELECTOR, 'li.greet.welcome')
FIRST_NAME_ERROR = (By.CSS_SELECTOR, '#firstname-error')
LAST_NAME_ERROR = (By.CSS_SELECTOR, '#lastname-error')
EMAIL_ERROR = (By.CSS_SELECTOR, '#email_address-error')
PWD_ERROR = (By.CSS_SELECTOR, '#password-error')
PWD_CONFIRM_ERROR = (By.CSS_SELECTOR, '#password-confirmation-error')
