from playwright.sync_api import BrowserContext, Page, Route
import re
import pytest


@pytest.fixture
def page(context: BrowserContext) -> Page:
    page: Page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    return page


def test_login(page: Page):
    page.goto('https://www.demoblaze.com/index.html')
    page.locator("#login2").click()
    page.wait_for_selector("#logInModal", state="visible")
    username = page.locator('#loginusername')
    username.fill('FFFFF')
    password = page.locator('#loginpassword')
    password.fill('1q2we3e4r5t6y')

    with page.expect_response(re.compile('https://api.demoblaze.com/login')) as response_event:
        page.locator("button[onclick='logIn()']").click()

        response = response_event.value

    assert response.json().get("errorMessage") == "User does not exist.", "Invalid error message"


def test_iphone(page: Page):

    iphone_new_name = 'яблокофон 16 про'

    def change_resp(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['productName'] = iphone_new_name
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = iphone_new_name
        body['body']['digitalMat'][0]['familyTypes'][0]['tabTitle'] = iphone_new_name
        route.fulfill(response=response, json=body)

    page.route(re.compile('/step0_iphone/digitalmat$'), change_resp)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.locator("[data-relatedlink=':r5:_secondarybutton']").click()

    element = page.wait_for_selector(
        (
            "h2.rf-digitalmat-overlay-header#rf-digitalmat-overlay-label-0"
            "[data-autom='DigitalMat-overlay-header-0-0']"
        ),
        timeout=5000
    )
    this_iphone_name = element.inner_text()
    print(this_iphone_name)
    assert this_iphone_name == iphone_new_name

    element_2 = page.wait_for_selector('.rf-digitalmat-tabnav-button', timeout=5000)
    this_iphone_name_2 = element_2.inner_text()
    assert this_iphone_name_2 == iphone_new_name

    element_3 = page.wait_for_selector('.rf-digitalmat-inlinetabnav-button.current', timeout=5000)
    this_iphone_name_3 = element_3.inner_text()
    assert this_iphone_name_3 == iphone_new_name
