import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
    """Фикстура для создания WebDriver"""
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()

    yield driver
    driver.quit()