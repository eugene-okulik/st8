import  selenium
import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    my_driver = webdriver.Chrome()
    my_driver.maximize_window()
    yield my_driver
    my_driver.quit()
