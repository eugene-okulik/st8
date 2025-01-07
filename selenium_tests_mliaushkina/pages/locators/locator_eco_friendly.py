from selenium.webdriver.common.by import By


PRODUCT_ITEM = (By.XPATH, './/li[@class="item product product-item"]')
PRODUCT_COUNT_SELECT = (By.XPATH, "(//div[@class='control']//select[@id='limiter'])[2]")
DIV_GRID_ITEM = (By.XPATH, "//div[@class='products wrapper grid products-grid']")
DIV_LIST_ITEM = (By.XPATH, "//div[@class='products wrapper list products-list']")
SWITCH_A_ITEM = (By.ID, "mode-list")
PRODUCT_SORT_SELECT = (By.ID, "sorter")
PRODUCT_ITEM_PRICE = (By.XPATH, "//li[@class='item product product-item']//span[@class='price-wrapper ']")
SORT_ARROW_SELECT = (By.XPATH, "//a[@class='action sorter-action sort-asc']")
