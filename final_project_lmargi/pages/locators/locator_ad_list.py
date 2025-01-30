from selenium.webdriver.common.by import By

PRODUCT_ITEM_FILTER = (By.CLASS_NAME, "resultItem")
PRICE_PRODUCT = (By.CLASS_NAME, "price")
INFO_PRODUCT = (By.CLASS_NAME, "info")
BRAND_PRODUCT = (By.XPATH, "//div[@class='link']/a")
REGION_PRODUCT = (By.XPATH, "//div[@class='info']/span")
SELECT_COLOR = (By.NAME, 'color')
SELECT_GEARBOX = (By.NAME, 'transmission')
SELECT_REGION = (By.NAME, "locat")
BUTTON_REFRESH = (By.ID, 'fBtn')
PRICE_MIN = (By.ID, 'pr1S')
PRICE_MAX = (By.ID, 'pr2S')
SELECT_SORT_BY = (By.NAME, "sort")
YEAR_MIN = (By.NAME, 'year')
YEAR_MAX = (By.NAME, 'year1')
POWER_MIN = (By.NAME, 'engine_power')
POWER_MAX = (By.NAME, 'engine_power1')





