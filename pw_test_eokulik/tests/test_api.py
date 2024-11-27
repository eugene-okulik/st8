from playwright.sync_api import Page, expect


def test_api(page: Page):
    response = page.request.get('https://jsonplaceholder.typicode.com/posts')
    expect(response).to_be_ok()
