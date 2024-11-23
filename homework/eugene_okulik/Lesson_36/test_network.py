import time

from playwright.sync_api import BrowserContext, Page, Route
import re
import pytest


@pytest.fixture
def page(context: BrowserContext) -> Page:
    page: Page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    return page


def test_login(page: Page):
    page.goto('https://www.it-roast.com/auth')
    page.locator('#email').fill('username@mail.ru')
    passwrod = page.locator('#password')
    passwrod.fill('sakjdfgeri')
    # with page.expect_response('**auth/login')
    with page.expect_response(re.compile('auth/login$')) as response_event:
        passwrod.press('Enter')
        response = response_event.value

    assert response.json()['status'] == 'UNAUTHORIZED'


def test_change_request(page: Page):

    def change_req(route: Route):
        url = route.request.url
        if 'filter4' in url:
            url = url.replace('&filter4=09z01', '')
            time.sleep(3)
        route.continue_(url=url)

    page.route(re.compile('/product/finder'), change_req)
    page.goto('https://www.samsung.com/au/smartphones/galaxy-z/')
    time.sleep(3)
    page.locator('[for="checkbox-series09z01"]').click()
    time.sleep(10)


def test_change_response(page: Page):

    def change_resp(route: Route):
        response = route.fetch()
        body = response.json()
        body['temperature'] = '+28'
        body['icon'] = 'A2'
        # body = json.dumps(body).encode('ascii')
        route.fulfill(response=response, json=body)

    page.route(re.compile('/pogoda/'), change_resp)
    page.goto('https://www.onliner.by/')
    page.locator('[name="query"]').click()
    time.sleep(5)


def test_form(page: Page):
    page.goto("https://demoqa.com/automation-practice-form")
    page.get_by_text("Male", exact=True).click()
    page.locator(".subjects-auto-complete__value-container").click()
    page.locator("#subjectsInput").fill("en")
    suggest = page.locator("#react-select-2-option-0")
    suggest.click()
    time.sleep(3)
