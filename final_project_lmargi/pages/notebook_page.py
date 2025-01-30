from final_project_lmargi.pages.base_page import BasePage
from final_project_lmargi.pages.card_page import CardPage
from final_project_lmargi.pages.locators import locator_notebook as locator

from selenium.webdriver.common.by import By

class NotebookPage(BasePage):

    def open_page(self):
        self.open_by_url('mynotepad')

    def get_car_links(self):
        car_list = []
        results_element = self.find(locator.RESULTS_ITEM)
        all_product_elements = results_element.find_elements(*locator.PRODUCT_ITEM_FILTER)

        for product in all_product_elements:
            product_link = product.find_element(By.TAG_NAME, "a").get_attribute("href")
            product_link = product_link.removeprefix('https://www.auto.bg/obiava/')
            car_list.append(product_link)

        return car_list

    def clean_notebook(self):
        all_car_elements = self.find_all_elements(locator.PRODUCT_ITEM_FILTER)
        for one_car in all_car_elements:
            product_link = one_car.find_element(By.TAG_NAME, "a").get_attribute("href")
            product_link = product_link.removeprefix('https://www.auto.bg/obiava/')
            this_card_page = CardPage(self.driver)
            this_card_page.open_card(product_link)
            this_card_page.remove_car_from_notebook()











