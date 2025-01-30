import re
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from final_project_lmargi.pages.base_page import BasePage
from final_project_lmargi.pages.locators import locator_card as locator
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from final_project_lmargi.pages.login_page import LoginPage
from final_project_lmargi.pages.const import const_card as const


class CardPage(BasePage):

    def open_page(self):
        self.open_by_url('obiava')

    def open_card(self, card_url):
        self.open_by_url(f'obiava/{card_url}')

    # def by_search_check_next_and_prev_page(self):
    #     original_url = self.driver.current_url
    #     print(f'original_url = {original_url}')
    #     next_link = self.find(locator.NEXT_BUTTON)
    #     next_link.click()
    #     time.sleep(2)
    #     # не работает стабильно, хз почему
    #     #WebDriverWait(self.driver, 10).until(ec.url_changes(original_url))
    #
    #     this_url = self.driver.current_url
    #     print(f'url_after_next = {this_url}')
    #     assert this_url != original_url, "URL не изменился"
    #
    #     prev_link = self.find(locator.PREV_BUTTON)
    #     prev_link.click()
    #     time.sleep(2)
    #
    #
    #     this_url = self.driver.current_url
    #     clean_url = this_url.removeprefix(const.AUTO_BG_OBIAVA)
    #     clean_url = clean_url.split('?')[0]
    #
    #     clean_original_url = original_url.removeprefix(const.AUTO_BG_OBIAVA)
    #     clean_original_url = clean_original_url.split('?')[0]
    #
    #     print(f'url_after_prev = {clean_url}')
    #     print(f'clean_original_url = {clean_original_url}')
    #     assert clean_url == clean_original_url, "URL изменился"

    def get_card_info(self):
        self.find(locator.CARD_BASE_TABLE)
        th_ui_1_elements = self.find_all_elements(locator.CARD_TABLE_TH)
        td_ui_1_elements = self.find_all_elements(locator.CARD_TABLE_TD)

        model_attrs = []
        th_index = 0

        for one_th in th_ui_1_elements:
            if th_index < len(td_ui_1_elements):
                th_title = one_th.text
                td_title = td_ui_1_elements[th_index].text
                model_attrs.append({'title': th_title, 'value': td_title})
            th_index += 1

        return model_attrs

    def get_card_info_attr(self, attr_title):
        all_attrs = self.get_card_info()
        for one_attr in all_attrs:
            if one_attr['title'] == attr_title:
                return one_attr['value']

        return None


    def get_color(self):
        return self.get_card_info_attr(const.COLOR_CAR)

    def get_load(self):
        return self.get_card_info_attr(const.LOAD_CAR)

    def get_brand(self):
        return self.get_card_info_attr(const.BRAND_CAR)

    def get_price(self):
        return self.get_card_info_attr(const.PRICE_CAR)

    def get_year(self):
        year_text = self.get_card_info_attr(const.YEAR_CAR)
        year_stripped = year_text.strip().split()
        year = int(year_stripped[1])
        return year

    def press_dealer_button(self):
        button_element = self.find(locator.BUTTON_SEND_EMAIL_MESSAGE)
        ActionChains(self.driver).move_to_element(button_element).perform()
        button_element.click()

    def get_ignore_checkbox_error(self):
        button_element = self.find(locator.SEND_BUTTON_LOCATOR)
        ActionChains(self.driver).move_to_element(button_element)
        button_element.click()
        error_message = self.find(locator.MESSAGE_FAIL)
        return error_message.is_displayed()

    def check_invalid_send_request_message(self):
        invalid_message = self.find(locator.MESSAGE_FAIL)
        assert invalid_message.is_displayed(), "FAAAAIL"


    def check_phone_number_hidden(self):
        phone_element = self.find(locator.SHOW_PHONE_NUMBER)
        initial_text = phone_element.text

        button_element = self.find(locator.SHOW_PHONE_BUTTON)
        button_element.click()
        return initial_text

    def check_phone_number_visible(self, initial_text):
        updated_text = self.find(locator.SHOW_PHONE_NUMBER).text
        return updated_text

    def check_title_notebook(self):
        link_element = self.find(locator.WRITE_NOTEBOOK)
        text_before_click = link_element.text.strip()

        actions = ActionChains(self.driver)
        actions.move_to_element(link_element).perform()
        return  text_before_click

    def check_save_car_from_notebook(self):
        link_element = self.find(locator.WRITE_NOTEBOOK)
        text_before_click = link_element.text.strip()

        actions = ActionChains(self.driver)
        actions.move_to_element(link_element).click().perform()
        return text_before_click


    # def save_car_ad_notebook(self):
    #     link_element = self.find(locator.WRITE_NOTEBOOK)
    #     link_element.click()

    def remove_car_from_notebook(self):
        link_element = self.find(locator.WRITE_NOTEBOOK)
        link_element.click()

    def fill_send_request_field_message(self, text_message):
        select_input = self.find_clickable(locator.INPUT_REQUEST)
        ActionChains(self.driver).move_to_element(select_input).perform()
        select_input.click()
        select_input.send_keys(text_message)

    def fill_send_request_field_name(self, text_name):
        select_input = WebDriverWait(self.driver, 15).until(
            ec.element_to_be_clickable(locator.SEND_REQUEST_NAME)
        )

        ActionChains(self.driver).move_to_element(select_input).perform()
        select_input.click()
        select_input.send_keys(text_name)

    def press_send_request(self):
        button_element = self.find(locator.SEND_BUTTON_LOCATOR)
        ActionChains(self.driver).move_to_element(button_element).perform()
        button_element.click()

    def status_message_ignor_privacy_policy(self, value):
        message_element = self.find(locator.MESSAGE_STATUS)
        if message_element.is_displayed() and value in message_element.text:
            return True
        return False


