from playwright.sync_api import BrowserContext, Page, Request, Response

import pytest


def test_listen(page: Page):

    def handle_request(request: Request):
        print('REQUEST', request.url, request.post_data)

    page.on('request', handle_request)
    page.on('response', lambda response: print('RESPONSE', response.url, response.status))
    page.goto('https://www.qa-practice.com/')
