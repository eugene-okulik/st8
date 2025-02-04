from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

from final_project_lmargi.pages.base_page import BasePage
from final_project_lmargi.pages.locators import  locator_search as locator


class SearchPage(BasePage):

    def open_page(self):
        self.open_by_url('search')

    def select_option(self, value, select_locator):
        select_ui_element = Select(self.find(select_locator))
        select_ui_element.select_by_value(value)

    def field_price_from(self, value:int):
        self.select_option(str(value), locator.DROPDOWN_PRICE_1)

    def field_price_to(self, value:int):
        self.select_option(str(value), locator.DROPDOWN_PRICE_2)

    def field_year_from(self, value:int):
        self.select_option(str(value), locator.DROPDOWN_YEAR_1)

    def field_year_to(self, value:int):
        self.select_option(str(value), locator.DROPDOWN_YEAR_2)

    def field_power_from(self, value):
         power_field_1 = self.find(locator.POWER_FROM)
         power_field_1.click()
         power_field_1.send_keys(value)

    def field_power_to(self, value):
         power_field_1 = self.find(locator.POWER_TO)
         power_field_1.click()
         power_field_1.send_keys(value)

    def field_gearbox(self, gearbox_value):
        self.select_option(gearbox_value, locator.SELECT_GEARBOX)


    def field_brand(self, value):
        self.select_option(value, locator.DROPDOWN_BRAND)


    def field_region(self, value):
        self.select_option(value, locator.DROPDOWN_REGION)

    def field_section(self, value):
        self.select_option(value, locator.DROPDOWN_SECTION)

    def field_load_from(self, value):
        power_field_1 = self.find(locator.DROPDOWN_LOAD_FROM)
        power_field_1.click()
        power_field_1.send_keys(value)

    def field_load_to(self, value):
        power_field_1 = self.find(locator.DROPDOWN_LOAD_TO)
        power_field_1.click()
        power_field_1.send_keys(value)

    def title_h1(self, value):
        title_filter = self.find(locator.TITLE_SEARCH)
        if title_filter.is_displayed() and value in title_filter.text:
            return True
        return False


    def press_button_search(self):
        select_ui_element = self.find(locator.BUTTON_SUBMIT_SEARCH)
        select_ui_element.click()


    def reset_checkboxes_on_page(self):
         checkbox_locators = [
             locator.INPUT_NEW_CHECKBOX,
             locator.INPUT_USED_CHECKBOX,
             locator.INPUT_PARTS_CHECKBOX
         ]
         for checkbox_locator in checkbox_locators:
             checkbox = self.find(checkbox_locator)
             if checkbox.is_selected():
                 checkbox.click()


    def check_condithion_input_used(self, expected_value):
        select_ui_element = self.find(locator.INPUT_USED_CHECKBOX)
        actions = ActionChains(self.driver)
        actions.move_to_element(select_ui_element).perform()
        select_ui_element.click()

        used_input = self.find(locator.SELECT_USED)
        used_input.get_attribute("value")


    def search_result(self):
        text_div = self.find(locator.TEXT_FILTER)
        text_content = text_div.text
        return text_content.split(":")[-1].strip()


    def check_condithion_input_new(self, value):
        select_ui_element = self.find(locator.INPUT_NEW_CHECKBOX)
        actions = ActionChains(self.driver)
        actions.move_to_element(select_ui_element).perform()
        select_ui_element.click()

        new_input = self.find(locator.SELECT_USED)
        new_input.get_attribute("value")



    def select_all_checkboxes_on_page(self, value):
        checkbox_locators = [
            locator.INPUT_NEW_CHECKBOX,
            locator.INPUT_USED_CHECKBOX,
            locator.INPUT_PARTS_CHECKBOX
        ]
        for checkbox_locator in checkbox_locators:
            checkbox = self.find(checkbox_locator)
            if not checkbox.is_selected():
                checkbox.click()





