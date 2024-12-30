from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

from selenium_ui_tests_dpolozkova.pages.create_account_page import AccountPage
from selenium_ui_tests_dpolozkova.pages.sale_page import SalePage
from selenium_ui_tests_dpolozkova.pages.eco_friendly_products_page import EcoPage


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def account_page(driver):
    return AccountPage(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture()
def eco_products_page(driver):
    return EcoPage(driver)
