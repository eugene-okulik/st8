import time
from playwright.sync_api import Page, Route
import re


def test_change_phone_name(page: Page):

    def change_resp(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['productName'] = 'яблокофон 16 про'
        route.fulfill(response=response, json=body)
    # route именно для приостанавливания запроса и подмены
    page.route(re.compile('/step0_iphone/digitalmat$'), change_resp)
    page.goto('https://www.apple.com/shop/buy-iphone')
    time.sleep(10)
    page.locator('.rf-hcard-content-title').first.click()
    time.sleep(10)
    title = page.locator('.rf-digitalmat-tabnav-button.current').text_content()
    assert title == 'яблокофон 16 про'
