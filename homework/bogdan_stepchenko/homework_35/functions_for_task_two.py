from playwright.sync_api import Page, expect, BrowserContext


class ChangingPage:
    URL = 'https://www.qa-practice.com/elements/new_tab/button'

    def __init__(self, page: Page, base_url=URL):
        self.page = page
        self.base_url = base_url

    def open_web_page(self):
        self.page.goto(self.base_url)

    def click_on_new_tab_button(self):
        button = self.page.get_by_role('link', name='Click')
        expect(button).to_be_enabled(timeout=5000)
        button.click()

    def check_if_new_tab_contain_correct_text(self, context: BrowserContext):
        with context.expect_page() as new_tab:
            page_2 = new_tab.value
        result_text_block = page_2.locator('#result-text')
        result_text = result_text_block.text_content()
        assert result_text == 'I am a new page in a new tab', 'Text in block is incorrect!'

    def check_if_new_tab_button_is_active(self):
        button = self.page.get_by_role('link', name='Click')
        expect(button).to_be_enabled(timeout=5000)
