import re
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from final_project_lmargi.pages.base_page import BasePage
from final_project_lmargi.pages.locators import locator_ad_list as locator
from final_project_lmargi.pages.const import const_adlist as const


class AdlistPage(BasePage):

    def open_page(self):
        self.open_by_url(const.OBIAVA_URL)

    def open_page_bus(self):
        self.open_by_url('obiavi/busove')

    def open_one_card(self, card_index):
        index = 0
        all_product_elements = self.find_all_elements(locator.PRODUCT_ITEM_FILTER)
        for product in all_product_elements:
            product_link = product.find_element(By.TAG_NAME, "a")
            if index == card_index:
                product_link.click()
                return True

            index = index + 1

        return False

    def open_first_card(self):
        all_product_elements = self.find_all_elements(locator.PRODUCT_ITEM_FILTER)
        for product in all_product_elements:
            product_url = product.find_element(By.TAG_NAME, "a")
            product_href = product_url.get_attribute("href")
            product_url.click()
            return product_href

        return ""

    def select_option(self, value, select_locator):
        select_ui_element = Select(self.find(select_locator))
        select_ui_element.select_by_value(value)

    def change_sort_by_price_asc(self):
        self.select_option(const.SORT_BY_PRICE_ASC_VALUE, locator.SELECT_SORT_BY)

    def change_sort_by_price_desc(self):
        self.select_option(const.SORT_BY_PRICE_DESC_VALUE, locator.SELECT_SORT_BY)

    def change_sort_by_year(self):
        self.select_option(const.SORT_BY_PRICE_YEAR_VALUE, locator.SELECT_SORT_BY)

    def set_filter_by_color(self, color_value):
        self.select_option(color_value, locator.SELECT_COLOR)

    def set_filter_by_gearbox(self, gearbox_value):
        self.select_option(gearbox_value, locator.SELECT_GEARBOX)

    def set_filter_by_prices(self, price_min: int, price_max: int):
        self.select_option(str(price_min), locator.PRICE_MIN)
        self.select_option(str(price_max), locator.PRICE_MAX)

    def set_filter_by_years(self, year_min: int, year_max: int):
        self.select_option(str(year_min), locator.YEAR_MIN)
        self.select_option(str(year_max), locator.YEAR_MAX)

    def set_filter_by_power(self, power_min: int, power_max: int):
        power_min_ui = self.find(locator.POWER_MIN)
        power_max_ui = self.find(locator.POWER_MAX)
        power_min_ui.click()
        power_min_ui.send_keys(str(power_min))
        power_max_ui.click()
        power_max_ui.send_keys(str(power_max))

    def set_filter_by_region(self, region_value):
        self.select_option(region_value, locator.SELECT_REGION)

    def press_button_refresh(self):
        button_update = self.find_clickable(locator.BUTTON_REFRESH)
        actions = ActionChains(self.driver)
        actions.move_to_element(button_update).perform()
        button_update.click()

    def get_filtered_cars(self):
        results = []
        all_product_elements = self.find_all_elements(locator.PRODUCT_ITEM_FILTER)
        car_index = 0
        maximum_cars = 3
        for product in all_product_elements:
            one_car_info = {
                'link': "",
                'title': "",
                'price': 0,
                'year': 0,
                'gearbox': "",
                'power': 0,
                'region': ""
            }

            # link
            product_link = product.find_element(By.TAG_NAME, "a").get_attribute("href")
            product_link = product_link.removeprefix(const.AUTO_BG_OBIAVA)

            one_car_info['link'] = product_link

            # title
            product_title = product.find_element(By.TAG_NAME, "a").text
            one_car_info['title'] = product_title

            # price
            price_element = product.find_element(*locator.PRICE_PRODUCT)
            price_text = price_element.text.strip()
            if price_text == "Цена по договаряне":
                one_car_info['price'] = 100500
            else:
                match = re.match(r'(\d[\d\s]*)', price_text)
                one_car_info['price'] = int(match.group(1).strip().replace(' ', ''))

            # region
            region_element = product.find_element(*locator.REGION_PRODUCT)
            region_text = region_element.text.strip()
            one_car_info['region'] = region_text.split()[-1]

            info_element = product.find_element(*locator.INFO_PRODUCT)
            info_text_splitted = info_element.text.strip().split()

            year_string = info_text_splitted[1]
            if year_string.isnumeric():
                one_car_info['year'] = int(year_string)

            one_car_info['gearbox'] = info_text_splitted[7]

            power_string = info_text_splitted[11]
            if power_string.isnumeric():
                one_car_info['power'] = int(power_string)

            results.append(one_car_info)

            car_index = car_index + 1
            if car_index >= maximum_cars:
                break

        return results
