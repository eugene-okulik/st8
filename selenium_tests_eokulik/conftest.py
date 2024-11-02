from selenium import webdriver
import pytest

from selenium_tests_eokulik.pages.products_page import ProductsPage
from selenium_tests_eokulik.pages.home_page import HomePage


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    # driver.implicitly_wait(3)
    yield driver
    driver.quit()


@pytest.fixture()
def products_page(driver):
    return ProductsPage(driver)


@pytest.fixture()
def home_page(driver):
    return HomePage(driver)
