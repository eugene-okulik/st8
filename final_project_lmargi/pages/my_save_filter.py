import re
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from final_project_lmargi.pages.base_page import BasePage
from final_project_lmargi.pages.locators import locator_my_save_filter as locator
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains



class MysaveFilterPage(BasePage):

    def open_page(self):
        self.open_by_url('myfilters')




