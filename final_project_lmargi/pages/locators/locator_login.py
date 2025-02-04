from selenium.webdriver.common.by import By

BUTTON_WITH_PHONE = (By.CSS_SELECTOR, 'input[name="regtype"][value="2"]')
BUTTON_WITH_EMAIL = (By.CSS_SELECTOR, 'input[name="regtype"][value="1"]')
EMAIL_INPUT = (By.NAME, 'email_phone')
PASSWORD = (By.NAME, 'passw')
BUTTON_SUBMIT= (By.CLASS_NAME, 'btBlue')
ERROR_MESSAGE_INVALID_METHOD = (By.XPATH, "//input[@name='email_phone']/following-sibling::span")
ERROR_MESSAGE_INVALID_PASSW = (By.XPATH, "//input[@name='passw']/following-sibling::span")
ERROR_MESSAGE_INVALID_PHONE = (By.XPATH, "//input[@name='email_phone']/following-sibling::span")
LOGIN_ERROR_MESSAGE = (By.CLASS_NAME, 'regMessage ')
ACCOUNT_NAME = (By.CSS_SELECTOR,  'span.clever-link[data-link="/myadverts"]')
LOGIN_BUTTON = (By.CSS_SELECTOR,  'span.clever-link[data-link="/login"]')
LOGOUT_BUTTON = (By.CSS_SELECTOR,  'span.clever-link[data-link="/login?act=3"]')

