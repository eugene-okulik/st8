import re

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from final_project_lmargi.pages.base_page import BasePage
from final_project_lmargi.pages.locators import  locator_my_announcement as locator
from selenium.webdriver.support import expected_conditions as ec


class MyAnnouncementPage(BasePage):

    def open_page(self):
        self.open_by_url('newoffer')


    def select_option(self, value, select_locator):
        select_ui_element = Select(self.find(select_locator))
        select_ui_element.select_by_value(value)

    def field_section(self, value:int):
        self.select_option(str(value), locator.DROPDOWN_SECTION)

    def field_brand(self, value:int):
        self.select_option(str(value), locator.DROPDOWN_BRAND)

    def field_condithion_car_used(self, value:int):
        self.select_option(str(value), locator.INPUT_USED_CHECKBOX)

    def field_condithion_car_parts(self, value:int):
        self.select_option(str(value), locator.INPUT_PARTS_CHECKBOX)

    def field_type(self, value:int):
        self.select_option(str(value), locator.DROPDOWN_TYPE)

    def field_model(self, value:int):
        self.select_option(str(value), locator.DROPDOWN_MODEL)

    def field_currency(self, value:int):
        self.select_option(str(value), locator.DROPDOWN_CURRENCY)

    def field_price(self, value:int):
        price_element = self.select_option(str(value), locator.INPUT_PRICE)
        price_element.click()
        price_element.send_keys(value)

    def field_month(self, value: int):
        self.select_option(str(value), locator.DROPDOWN_YEAR_2)

    # поле без звездочки
    def field_year(self, value: int):
        self.select_option(str(value), locator.DROPDOWN_YEAR_2)

    def field_region(self, value: int):
        self.select_option(str(value), locator.DROPDOWN_YEAR_2)

    def field_plice(self, value:int):
        self.select_option(str(value), locator.DROPDOWN_YEAR_2)

    def field_mileage(self, value: int):
        self.select_option(str(value), locator.DROPDOWN_YEAR_2)

    def field_seats(self, value: int):
        self.select_option(str(value), locator.DROPDOWN_YEAR_2)












