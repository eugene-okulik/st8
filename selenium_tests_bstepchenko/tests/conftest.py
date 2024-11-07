import pytest
from selenium import webdriver
from selenium_tests_bstepchenko.pages.sign_in_page import SignInPage
from selenium_tests_bstepchenko.pages.account_page import AccountPage
from selenium_tests_bstepchenko.pages.collections_eco_friendly_page import EcoFriendly
from selenium_tests_bstepchenko.pages.sale_page import SalePage
from selenium_tests_bstepchenko.pages.women_sale_page import WomenSale


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def sign_in_page(driver):
    return SignInPage(driver)


@pytest.fixture()
def account_page(driver):
    return AccountPage(driver)


@pytest.fixture()
def eco_friendly(driver):
    return EcoFriendly(driver)


@pytest.fixture()
def sales_page(driver):
    return SalePage(driver)


@pytest.fixture()
def women_sale_page(driver):
    return WomenSale(driver)
