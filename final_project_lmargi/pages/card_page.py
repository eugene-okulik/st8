from selenium.webdriver.support.wait import WebDriverWait

from final_project_lmargi.pages.base_page import BasePage
from final_project_lmargi.pages.locators import locator_card as locator
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from final_project_lmargi.pages.const import const_card as const


class CardPage(BasePage):

    def open_page(self):
        self.open_by_url(const.URI_OBIAVA)

    def open_card(self, card_url):
        self.open_by_url(f'obiava/{card_url}')


    def get_current_url(self):
        return self.driver.current_url

    def get_current_pure_url(self):
        current_link = self.get_current_url()
        current_link = current_link.split('?')[0]
        return current_link

    def get_current_relative_url(self):
        current_link = self.get_current_pure_url()
        current_link = current_link.removeprefix(const.AUTO_BG_OBIAVA)
        return current_link

    def click_next_page(self):
        next_link_ui = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(locator.NEXT_BUTTON)
        )
        next_link_ui.click()

    def click_prev_page(self):

        prev_link_ui = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(locator.PREV_BUTTON)
        )
        prev_link_ui.click()

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

    # def get_load(self):
    #     return self.get_card_info_attr(const.LOAD_CAR)
    #
    # def get_brand(self):
    #     return self.get_card_info_attr(const.BRAND_CAR)
    #
    # def get_price(self):
    #     return self.get_card_info_attr(const.PRICE_CAR)
    #
    # def get_year(self):
    #     year_text = self.get_card_info_attr(const.YEAR_CAR)
    #     year_stripped = year_text.strip().split()
    #     year = int(year_stripped[1])
    #     return year

    def press_dealer_button(self):
        button_element = self.find(locator.BUTTON_SEND_EMAIL_MESSAGE)
        ActionChains(self.driver).move_to_element(button_element).perform()
        button_element.click()

    def get_ignore_checkbox_error(self):
        button_element = self.find(locator.SEND_BUTTON_LOCATOR)
        ActionChains(self.driver).move_to_element(button_element)
        button_element.click()
        error_message = self.find(locator.MESSAGE_FAIL)
        print(error_message.text)
        return error_message.is_displayed()


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


    def remove_car_from_notebook(self):
        link_element = self.find(locator.WRITE_NOTEBOOK)
        link_element.click()


    def press_send_request(self):
        button_element = self.find(locator.SEND_BUTTON_LOCATOR)
        ActionChains(self.driver).move_to_element(button_element).perform()
        button_element.click()

    def status_message_ignor_privacy_policy(self, value):
        message_element = self.find(locator.MESSAGE_STATUS)
        if message_element.is_displayed() and value in message_element.text:
            return True

        return False

    def save_card_ad_notebook(self):
        link_element = self.find(locator.WRITE_NOTEBOOK)
        link_element.click()
