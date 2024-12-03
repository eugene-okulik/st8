import re


def test_first_homework(page):
    page.goto('https://www.demoblaze.com/index.html')
    login = page.locator("//a[@id='login2']")
    login.click()
    login_username = page.locator("//input[@id='loginusername']")
    login_password = page.locator("//input[@id='loginpassword']")
    login_button = page.locator("//button[@onclick='logIn()']")
    with page.expect_response(re.compile('/login$')) as response_event:
        login_username.fill("r3www")
        login_password.fill("errerr")
        login_button.click()
        resp = response_event.value
        err_message = resp.json()['errorMessage']
    assert err_message == "User does not exist."
