import pytest
from playwright.sync_api import Page, BrowserContext, Route, Request, Response


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Page:
    page: Page = context.new_page()
    return page
