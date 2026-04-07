import pytest
import allure
from pages.ui_page import MainPage
from selenium import webdriver
from time import sleep


def test_search_film():
    driver = webdriver.Chrome()
    main_page = MainPage(driver, "https://www.kinopoisk.ru/")
    main_page.open_main_page()
    main_page.search_by_phrase("Мачеха")

    sleep(5)
def