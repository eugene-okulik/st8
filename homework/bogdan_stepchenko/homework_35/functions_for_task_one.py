from playwright.sync_api import Page, expect


class Alert:
    URL = 'https://www.qa-practice.com/elements/alert/confirm'

    def __init__(self, page: Page, base_url=URL):
        self.page = page
        self.base_url = base_url

    def open_web_page(self):
        self.page.goto(self.base_url)

    def click_on_button(self):
        self.page.on('dialog', lambda dialog: dialog.accept())
        button = self.page.get_by_role('link', name='Click')
        button.click()

    def check_if_text_correct(self):
        result_block = self.page.locator('#result-text')
        expect(result_block).to_be_visible(timeout=5000)
        result_text = result_block.text_content()
        assert result_text == 'Ok', 'Result text is incorrect! should be "Ok"'
