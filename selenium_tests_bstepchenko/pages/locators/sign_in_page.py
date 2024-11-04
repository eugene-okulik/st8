from selenium.webdriver.common.by import By

FIRST_NAME = (By.ID, 'firstname')
FIRST_NAME_ERROR = (By.ID, 'firstname-error')

LAST_NAME = (By.ID, 'lastname')
LAST_NAME_ERROR = (By.ID, 'lastname-error')

EMAIL = (By.ID, 'email_address')
EMAIL_ERROR = (By.ID, 'email_address-error')

PASSWORD = (By.ID, 'password')
PASSWORD_ERROR = (By.ID, 'password-error')

CONF_PASSWORD = (By.ID, 'password-confirmation')
CONF_PASSWORD_ERROR = (By.ID, 'password-confirmation-error')

ERROR_MESSAGE = (By.CSS_SELECTOR, "div[role='alert'] .message-error")
CREATE_ACCOUNT_BUTTON = (By.XPATH, '//button[contains(@class, "action submit primary")]')
