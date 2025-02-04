from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from final_project_lmargi.pages.base_page import BasePage
from final_project_lmargi.pages.locators import  locator_add_announcement as locator
from final_project_lmargi.pages.const import const_add_announc as const


class Add_AnnouncementPage(BasePage):

    def open_page(self):
        self.open_by_url(const.LINK_PAGE)


    def select_option(self, value, select_locator):
        select_ui_element = Select(self.find(select_locator))
        select_ui_element.select_by_value(value)

    def field_section(self, value: int):
        self.select_option(str(value), locator.DROPDOWN_SECTION)

    def field_brand(self, value):
        self.select_option(str(value), locator.DROPDOWN_BRAND)


    def field_type(self, value):
        self.select_option(str(value), locator.DROPDOWN_TYPE)

    def field_model(self, value):
        self.select_option(str(value), locator.DROPDOWN_MODEL)

    def get_field_model_option_count(self):
        select_ui_element = Select(self.find(locator.DROPDOWN_MODEL))
        opt_list = select_ui_element.options
        return len(opt_list)

    def field_currency(self, value):
        self.select_option(str(value), locator.DROPDOWN_CURRENCY)

    def field_month(self, value):
        self.select_option(str(value), locator.DROPDOWN_MONTH)

    def field_year(self, value: int):
        self.select_option(str(value), locator.DROPDOWN_YEAR)

    def field_color(self, value):
        self.select_option(str(value), locator.DROPDOWN_YEAR)

    def field_region(self, value):
        self.select_option(str(value), locator.DROPDOWN_REGION)

    def field_place(self, value):
        self.select_option(str(value), locator.DROPDOWN_PLACE)

    def field_engine_type(self, value):
        self.select_option(str(value), locator.DROPDOWN_ENGINE_TYPE)

    def field_gearbox(self, value):
        self.select_option(str(value), locator.DROPDOWN_GEARBOX)


    def field_mileage(self, value: int):
        mileage_field = self.find(locator.INPUT_MILEAGE)
        mileage_field.click()
        mileage_field.send_keys(value)


    def field_price(self, value: int):
        price_element = self.find(locator.INPUT_PRICE)
        price_element.click()
        price_element.send_keys(value)

    def press_button_create_ad(self):
        button_pub = self.find(locator.BUTTON_PUBLICATION)
        button_pub.click()


    def upload_photo_to_placeholder(self, file_path, placeholder_locator):
        placeholders = self.find_all_elements(placeholder_locator)
        for placeholder in placeholders:
            placeholder.click()

            file_input = placeholder.find_element(By.CSS_SELECTOR, "input[type='file']")
            file_input.send_keys(file_path)
            break

    def check_checkbox_price(self):
        checkbox_price = self.find(locator.INPUT_CHECKBOX_PRICE)
        checkbox_price.click()


    def wait_allert(self):
        WebDriverWait(self.driver, 5).until(ec.alert_is_present())
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text

    def wait_message_invalid_check(self):
        element = self.find(locator.MESSAGE_ERROR)
        message_text = element.text.strip()
        return message_text.strip()


    def check_title_big(self, value):
        title_announcement = self.find(locator.TITLE_BIG)
        title = title_announcement.text.strip()
        return title.strip()

    def field_text_add_info(self, value):
        select_input = WebDriverWait(self.driver, 15).until(
            ec.element_to_be_clickable(locator.ADD_INFO)
        )

        ActionChains(self.driver).move_to_element(select_input).perform()
        select_input.click()
        select_input.send_keys(value)

    def check_change_url(self, part_url):
        WebDriverWait(self.driver, 10).until(ec.url_contains(part_url))


    def press_button_create_ad_2(self):
        button_pub = self.find(locator.BUTTON_PUBLICATION_2)
        button_pub.click()

    def check_condithion_input_used(self, expected_value):
        select_ui_element = self.find(locator.INPUT_USED_CHECKBOX)
        actions = ActionChains(self.driver)
        actions.move_to_element(select_ui_element).perform()
        select_ui_element.click()









