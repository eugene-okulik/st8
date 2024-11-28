import re
from playwright.sync_api import Page, Route


class CheckChangedTitle:
    URL = 'https://www.apple.com/shop/buy-iphone'
    REQ_URL = 'https://www.apple.com/shop/api/digital-mat?path=library/step0_iphone/digitalmat'
    NAME_FOR_CHANGE = 'яблокофон 16 Про'

    def __init__(self, page: Page, base_url=URL, req_url=REQ_URL):
        self.base_url = base_url
        self.page = page
        self.req_url = req_url

    def change_phone_name_in_request(self):
        def change_response(route: Route):
            response = route.fetch()
            body = response.json()
            body['body']['digitalMat'][0]['productName'] = self.NAME_FOR_CHANGE
            route.fulfill(response=response, json=body)

        self.page.route(re.compile('/step0_iphone/digitalmat$'), change_response)
        self.page.goto(self.base_url)

    def click_on_first_card(self):
        first_card = self.page.locator('.rf-hcard-content-title').first
        first_card.click()

    def check_if_title_in_popup_is_correct(self):
        card_title = self.page.locator('#rf-digitalmat-overlay-label-0').first
        card_title_name = card_title.text_content()
        assert card_title_name == 'iPhone 16 Pro'

    def check_if_button_name_contains_changed_phone_name(self):
        button_with_phone_name = self.page.locator(".rf-digitalmat-tabnav-button.current")
        button_with_phone_name.wait_for(state="visible")
        phone_name_on_button = button_with_phone_name.text_content()
        assert phone_name_on_button == self.NAME_FOR_CHANGE
