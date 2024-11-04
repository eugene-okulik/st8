from selenium.webdriver.common.by import By


MAIN_SALE = (By.XPATH, ".//a[@class='block-promo sale-main']")
MAIN_SALE_INFO = (By.XPATH, ".//span[@class='info']")
MAIN_SALE_TITLE = (By.XPATH, ".//strong[@class='title']")
MAIN_SALE_BUTTON = (By.XPATH, ".//span[@class='more button']")

MEN_SALE = (By.XPATH, ".//a[@class='block-promo sale-mens']")

WOMEN_SALE = (By.XPATH, ".//a[@class='block-promo sale-women']")

SALE_20_OFF = (By.XPATH, ".//a[@class='block-promo sale-20-off']")

FREE_SHIPPING_SALE = (By.XPATH, ".//a[@class='block-promo sale-free-shipping']")

T_SHIRTS_SALE = (By.XPATH, ".//a[@class='block-promo sale-womens-t-shirts']")
