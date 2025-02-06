from selenium.webdriver.common.by import By


CARD_BASE_TABLE = (By.CLASS_NAME, 'dowble')
CARD_TABLE_TR = (By.TAG_NAME, 'tr')
CARD_TABLE_TH = (By.TAG_NAME, 'th')
CARD_TABLE_TD = (By.TAG_NAME, 'td')
CARD_TABLE_TH_2 = (By.XPATH, '//tr//th[@class="secColumn"]')
CARD_TABLE_TD_2 = (By.XPATH, "//tr//td[@class='secColumn']")
BUTTON_SEND_EMAIL_MESSAGE = (By.ID, "callDealerBtn")
AGREE_CHECKBOX =(By.NAME, "f4")
MESSAGE_FAIL = (By.ID, "messageFail")
SEND_BUTTON_LOCATOR = (By.XPATH, "//ul[@id='callDealerForms']//button[@class='btBlue']")
INPUT_REQUEST = (By.XPATH, "//li[./text()[normalize-space()]]/textarea")
SEND_REQUEST_NAME =(By.XPATH, "//input[@name='f0']")
NEXT_BUTTON = (By.ID, "next")
PREV_BUTTON = (By.ID, "prev")
SHOW_PHONE_NUMBER = (By.CLASS_NAME, "phoneNumber")
SHOW_PHONE_BUTTON = (By.CLASS_NAME, "callBTN")
WRITE_NOTEBOOK = (By.ID, "saveLink")
CARD_TABLE_OTHER = (By.CLASS_NAME, "options")
WRITE_FILTER = (By.CLASS_NAME, "btBlue")
MESSAGE_STATUS = (By.ID, "messageFail")
