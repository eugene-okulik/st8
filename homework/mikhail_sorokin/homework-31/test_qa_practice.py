from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class TestHomeWorkOne:
    POPUP = (By.XPATH, "//button[@class='btn btn-primary' and @data-bs-toggle='modal']")
    IFRAME = (By.XPATH, "//iframe[@class='embed-responsive-item']")
    TEXT_TO_COPY = (By.XPATH, "//p[@id='text-to-copy']")
    CHECK_BUTTON = (By.XPATH, "//button[text()='Check']")
    TEXT_INPUT = (By.XPATH, "//input[@name='text_from_iframe']")
    SUBMIT_BUTTON = (By.XPATH, "//input[@id='submit-id-submit']")
    CHECK_RESULT = (By.XPATH, "//div[@id='check-result']")

    def test_qa_practice_homework(self, driver):
        driver.get('https://www.qa-practice.com/elements/popup/iframe_popup')
        wait = WebDriverWait(driver, 10)
        actions = ActionChains(driver)
        popup = wait.until(EC.element_to_be_clickable(self.POPUP))
        actions.move_to_element(popup).click().perform()
        iframe = wait.until(EC.presence_of_element_located(self.IFRAME))
        driver.switch_to.frame(iframe)
        popup_modal_window_text = wait.until(EC.presence_of_element_located(self.TEXT_TO_COPY))
        text_from_popup = popup_modal_window_text.get_attribute("textContent")
        driver.switch_to.default_content()
        check = wait.until(EC.element_to_be_clickable(self.CHECK_BUTTON))
        check.click()
        text_input = wait.until(EC.visibility_of_element_located(self.TEXT_INPUT))
        text_input.send_keys(text_from_popup)
        submit = wait.until(EC.visibility_of_element_located(self.SUBMIT_BUTTON))
        submit.click()
        result = wait.until(EC.visibility_of_element_located(self.CHECK_RESULT))
        assert "Correct!" in result.text
