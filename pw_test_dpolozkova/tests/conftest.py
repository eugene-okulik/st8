from playwright.sync_api import Page, BrowserContext

import pytest

from pw_test_dpolozkova.pages.create_account_page import AccountPage
from pw_test_dpolozkova.pages.sale_page import SalePage
from pw_test_dpolozkova.pages.eco_friendly_products_page import EcoPage


def page(context: BrowserContext) -> Page:
    page: Page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    return page


@pytest.fixture()
def account_page(page):
    return AccountPage(page)


@pytest.fixture()
def sale_page(page):
    return SalePage(page)


@pytest.fixture()
def eco_products_page(page):
    return EcoPage(page)
