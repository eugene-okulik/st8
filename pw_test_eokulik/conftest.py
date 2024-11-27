from playwright.sync_api import Page, BrowserContext

import pytest

from pw_test_eokulik.pages.products_page import ProductsPage
from pw_test_eokulik.pages.home_page import HomePage
from pw_test_eokulik.pages.sale_page import SalePage


@pytest.fixture
def page(context: BrowserContext) -> Page:
    page: Page = context.new_page()
    # page.set_viewport_size({'width': 1920, 'height': 1080})
    return page


@pytest.fixture()
def products_page(page):
    return ProductsPage(page)


@pytest.fixture()
def home_page(page):
    return HomePage(page)


@pytest.fixture()
def sale_page(page):
    return SalePage(page)
