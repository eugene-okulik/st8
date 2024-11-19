import time

import pytest
from playwright.sync_api import Page, expect, BrowserContext


def test_authentication(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    link_form_auth = page.get_by_role('link', name = 'Form Authentication')
    link_form_auth.click()
    username = page.get_by_role('textbox', name = 'username' )
    username.fill('Veniamin')

    expect(username).to_have_value('Veniamin')
    password = page.get_by_role('textbox', name = 'password')
    password.fill('1q2we3e4r5t')
    expect(password).to_have_value('1q2we3e4r5t')

    login_button = page.get_by_role('button', name= "Login")
    login_button.click()
    expect(login_button).to_be_visible()


