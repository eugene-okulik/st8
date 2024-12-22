from playwright.sync_api import Page
import re


def test_receive_error_message(page: Page):
    page.goto('https://www.demoblaze.com/index.html')
    page.locator('#login2').click()
    page.locator('#loginusername').fill('Bubik')
    page.locator('#loginpassword').fill('Mumik')
    # указываем до действия после которого ожидаем
    with page.expect_response(re.compile('login$')) as response_event:
        page.get_by_role("button", name="Log in").click()
        response = response_event.value.json()
        assert response['errorMessage'] == 'User does not exist.'
