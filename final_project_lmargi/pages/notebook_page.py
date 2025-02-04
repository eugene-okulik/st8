from final_project_lmargi.pages.base_page import BasePage
from final_project_lmargi.pages.card_page import CardPage
from final_project_lmargi.pages.locators import locator_notebook as locator
from final_project_lmargi.pages.const import const_notebook as const

from selenium.webdriver.common.by import By

class NotebookPage(BasePage):

    def open_page(self):
        self.open_by_url(const.URL_NOTEBOOK)

    def get_car_links(self):
        car_list = []
        results_element = self.find(locator.RESULTS_ITEM)
        all_product_elements = results_element.find_elements(*locator.PRODUCT_ITEM_FILTER)

        for product in all_product_elements:
            product_link = product.find_element(By.TAG_NAME, "a").get_attribute("href")
            product_link = product_link.removeprefix(const.URL_OBIAVA)
            car_list.append(product_link)

        return car_list

    def clean_notebook(self):
        all_car_links = self.get_car_links()
        for one_car_link in all_car_links:
            this_card_page = CardPage(self.driver)
            this_card_page.open_card(one_car_link)
            this_card_page.remove_car_from_notebook()

    def get_empty_message_text(self):
        self.find(locator.MESSAGE_EMPTY_CAR)



