from selenium.webdriver.common.by import By

COOKIE_ELEMENT = (By.ID, 'cookiescript_accept')
DROPDOWN_PRICE_1 = (By.ID, 'pr1S')
DROPDOWN_PRICE_2 = (By.ID, 'pr2S')
DROPDOWN_YEAR_1 = (By.NAME, 'year')
DROPDOWN_YEAR_2 = (By.NAME, 'year1')
DROPDOWN_BRAND = (By.NAME, "marka")
DROPDOWN_LOAD_FROM = (By.NAME, 'loading')
DROPDOWN_LOAD_TO = (By.NAME, 'loading1')
DROPDOWN_REGION = (By.NAME, "locat")
DROPDOWN_SECTION = (By.NAME, 'cat')

SELECT_USED = (By.XPATH, "//form[@name='search']//input[@name='nup' and @type='hidden']")
TEXT_FILTER = (By.CSS_SELECTOR, "div.text")
POWER_FROM = (By.NAME, "engine_power")
POWER_TO = (By.NAME, "engine_power1")
TITLE_SEARCH = (By.CLASS_NAME, "titleBig")
SELECT_GEARBOX = (By.NAME, 'transmission')
INPUT_NEW_CHECKBOX = (By.ID, "nup1")
INPUT_USED_CHECKBOX = (By.ID, "nup0")
INPUT_PARTS_CHECKBOX = (By.ID, "nup2")
BUTTON_SUBMIT_SEARCH = (By.CSS_SELECTOR, "button[type='submit']")
BUTTON_MAKE_A_SELECTION= (By.CLASS_NAME, "uk-button-primary")




INPUT_NUMBER = (By.XPATH, "(//input[@class='InputNumber'])[1]")
INPUT_NUMBER_2 = (By.XPATH, "(//input[@class='InputNumber'])[2]")

