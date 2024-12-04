from playwright.sync_api import Page, BrowserContext, Route
import re
import pytest
from playwright.sync_api import expect


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Page:
    page: Page = context.new_page()
    return page


def test_mock_homework(page):
    def change_response(route: Route):
        response = route.fetch()
        resp_body = response.json()
        resp_body['body']['digitalMat'][0]['productName'] = "яблокофон 16 про"
        resp_body['body']['digitalMat'][0]['familyTypes'][0]['tabTitle'] = "яблокофон 16 про"
        resp_body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = "яблокофон 16 про"
        route.fulfill(response=response, json=resp_body)

    page.route(re.compile('/digital-mat'), change_response)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.locator("(//div[@class='rf-hcard-content tile as-util-relatedlink'])[1]").click()
    expect("//div//h2[@id='rf-digitalmat-overlay-label-0'])[1]").to_have_text("яблокофон 16 про")
