from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from final_project_lmargi.pages.base_page import BasePage
from final_project_lmargi.pages.locators import  locator_my_offers as locator



class MyOfferPage(BasePage):

    def open_page(self):
        self.open_by_url('myadverts')

    def get_filtered_title(self):
        results = []
        all_product_elements = self.find_all_elements(locator.PRODUCT_ITEM_FILTER)

        for product in all_product_elements:
            title = product.find_element(By.TAG_NAME, "a").text.strip()
            results.append({'title': title})
            print(f"Found title: {title}")
        return results

    def delete_all_cars(self):
        all_product_elements = self.find_all_elements(locator.PRODUCT_ITEM_FILTER)

        for product in all_product_elements:
            delete_button = product.find_element(By.CLASS_NAME, "delete")
            delete_button.click()

        return True

    def wait_allert_for_delete(self):
        WebDriverWait(self.driver, 5).until(ec.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()