import pytest
from playwright.sync_api import BrowserContext, Page
from pw_test_mliaushkina.pages.customer_create_page import CustomerCreatePage
from pw_test_mliaushkina.pages.eco_friendly_page import EcoFriendlyPage
from pw_test_mliaushkina.pages.sale_page import SalePage


@pytest.fixture()
def page(context: BrowserContext) -> Page:
    page: Page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    return page


@pytest.fixture()
def customer_create_page(page):
    return CustomerCreatePage(page)


@pytest.fixture()
def eco_friendly_page(page):
    return EcoFriendlyPage(page)


@pytest.fixture()
def sale_page(page):
    return SalePage(page)
