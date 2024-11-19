from playwright.sync_api import sync_playwright

from playwright.sync_api import sync_playwright

from playwright.sync_api import sync_playwright


def test_wait_for_color_change():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://demoqa.com/dynamic-properties')
        button = page.locator("#colorChange")
        button.wait_for(state="attached")
        page.wait_for_function(
            "document.querySelector('#colorChange').style.color === 'rgb(220, 53, 69)' || window.getComputedStyle(document.querySelector('#colorChange')).color === 'rgb(220, 53, 69)'"
        )
        button.click()
        browser.close()
