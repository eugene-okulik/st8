import pytest
from selenium import webdriver
from final_project_lmargi.pages.login_page import LoginPage
from  final_project_lmargi.pages.search_page import SearchPage
from  final_project_lmargi.pages.card_page import CardPage
from  final_project_lmargi.pages.notebook_page import NotebookPage
from  final_project_lmargi.pages.adlist_page import AdlistPage
from  final_project_lmargi.pages.my_save_filter import MysaveFilterPage
from  final_project_lmargi.pages.my_announcement import MyAnnouncementPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture()
def search_page(driver):
    return SearchPage(driver)

@pytest.fixture()
def card_page(driver):
    return CardPage(driver)

@pytest.fixture()
def notebook_page(driver):
    return NotebookPage(driver)

@pytest.fixture()
def adlist_page(driver):
    return AdlistPage(driver)


@pytest.fixture()
def my_save_filter(driver):
    return MysaveFilterPage(driver)

@pytest.fixture()
def my_announcement(driver):
    return MyAnnouncementPage(driver)




