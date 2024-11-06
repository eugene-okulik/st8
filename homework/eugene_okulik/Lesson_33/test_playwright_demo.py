import time

from playwright.sync_api import Page, expect
import re


def test_google(page: Page):
    page.goto('https://www.google.com/')
    search_field = page.get_by_role('combobox')
    search_field.fill('cat')
    # search_field.type('cat')
    # search_field.press_sequentially('cat', delay=1000)
    search_field.press('Enter')
    # assert 'cat' in page.title()
    # assert page.title().startswith('cat')
    expect(page).to_have_title(re.compile('cat'))
    expect(page).to_have_title(re.compile('^cat'))
    # expect(page).to_have_title(re.compile('cat$'))


def test_by_role(page: Page):
    page.goto('https://demoblaze.com/')
    # phone = page.get_by_role('link', name='Phone')
    laptops = page.get_by_role('link', name='Laptops')
    laptops.click()
    time.sleep(3)
