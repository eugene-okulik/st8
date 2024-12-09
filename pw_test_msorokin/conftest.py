from playwright.sync_api import Page, BrowserContext

import pytest

from pw_test_msorokin.pages.woman_page import WomenCatalogPage
from pw_test_msorokin.pages.home_page import HomePage


@pytest.fixture
def page(context: BrowserContext) -> Page:
    page: Page = context.new_page()
    return page


@pytest.fixture()
def women_catalog_page(page):
    return WomenCatalogPage(page)


@pytest.fixture()
def home_page(page):
    return HomePage(page)
