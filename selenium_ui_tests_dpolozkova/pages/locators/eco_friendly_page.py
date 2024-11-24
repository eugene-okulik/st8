from selenium.webdriver.common.by import By


SEARCH = (By.CSS_SELECTOR, "input[id='search']")
SEARCH_RESULTS = (By.XPATH, '//*[contains(text(),"Related search terms")]')
FOUND_ITEM = (By.XPATH, '//img[@class="product-image-photo"]')
LIST_VIEW = (By.CSS_SELECTOR, 'div[class="modes"] > a')
PRODUCTS_LIST = (By.XPATH, './/li[@class="item product product-item"]')
SELECT_SORTING = (By.CSS_SELECTOR, '.sorter-options')
