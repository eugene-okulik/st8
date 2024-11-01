import  selenium
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()