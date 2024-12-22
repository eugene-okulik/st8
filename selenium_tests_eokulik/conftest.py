from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

from selenium_tests_eokulik.pages.products_page import ProductsPage
from selenium_tests_eokulik.pages.home_page import HomePage


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
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
