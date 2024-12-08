from pw_test_msorokin.pages.base_page import BasePage


class HomePage(BasePage):
    def open_by_url(self, postfix=None):
        self.page.goto(self.base_url)
