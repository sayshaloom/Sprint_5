import pytest
from selenium import webdriver
import constants

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(constants.url)
    yield driver
    driver.quit()