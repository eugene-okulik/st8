import pytest
from selenium import webdriver
from selenium_tests_mliaushkina.pages.customer_create_page import CustomerCreatePage
from selenium_tests_mliaushkina.pages.eco_friendly_page import EcoFriendlyPage
from selenium_tests_mliaushkina.pages.sale_page import SalePage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def customer_create_page(driver):
    return CustomerCreatePage(driver)


@pytest.fixture()
def eco_friendly_page(driver):
    return EcoFriendlyPage(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)
