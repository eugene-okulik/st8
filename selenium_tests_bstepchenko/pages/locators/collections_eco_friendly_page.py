from selenium.webdriver.common.by import By


PRODUCT_CARD = (By.XPATH, './/li[@class="item product product-item"]')
WHITE_COLOR_INSIDE_PRODUCT_CARD = (By.CSS_SELECTOR, "div.swatch-option.color[aria-label='White']")

DEFAULT_PRODUCT_QUANTITY = (By.XPATH, './/p[@class="toolbar-amount"]/span[@class="toolbar-number"][2]')
ALL_PRODUCTS_QUANTITY = (By.XPATH, './/p[@class="toolbar-amount"]/span[@class="toolbar-number"][1]')

LIST_VIEW_BUTTON = (By.XPATH, '//a[@class="modes-mode mode-list"]')

COLOR_DROPDOWN = (By.XPATH, '//div[@data-role="title" and text()="Color"]')
LIST_OF_COLORS_IN_DROPDOWN = (By.CLASS_NAME, "swatch-attribute-options")
WHITE_COLOR_IN_DROPDOWN = (By.XPATH, '//a[div[@option-id="59"]]')


SELECTOR = (By.XPATH, "(//div[@class='control']//select[@id='limiter'])[2]")
