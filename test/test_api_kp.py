import os

import allure
from dotenv import load_dotenv

load_dotenv()
import requests
import pytest


@pytest.mark.api
@allure.title("Поиск фильма на русском языке")
@allure.story("Поиск")
# поиск по названию, проверить что в теле ответа есть
def test_search_film_name():
    name = 'Мачеха'
    url = f"https://kinopoiskapiunofficial.tech/api/v2.1/films/search-by-keyword?keyword={name}&page=1"
    key = os.getenv('API_KEY')
    payload = {}
    headers = {
        'accept': 'application/json',
        'X-API-KEY': key
    }
    with allure.step("Отправляем запрос"):
        response = requests.request("GET", url, headers=headers, data=payload)
        status_code = response.status_code
        resp = response.json()
    with allure.step("Проверяем статус-код"):
        assert status_code == 200
        assert isinstance(resp, dict)
    keyword = resp["keyword"]
    pages_count = resp["pagesCount"]
    film = resp['films']
    with allure.step("Проверяем, что фильм нашёлся"):
        assert keyword == name
        assert pages_count > 0
        assert isinstance(film, list)


@pytest.mark.api
@allure.title("Поиск фильма на русском языке")
@allure.story("Поиск")
# запрос с неправильным токеном, ожидаемая ошибка
def test_search_no_token():
    name = 'Мачеха'
    url = f"https://kinopoiskapiunofficial.tech/api/v2.1/films/search-by-keyword?keyword={name}&page=1"
    payload = {}
    headers = {
        'accept': 'application/json',
        'X-API-KEY': ""
    }
    with allure.step("Отправляем запрос"):
        response = requests.request("GET", url, headers=headers, data=payload)
    with allure.step("Проверяем статус-код"):
        status_code = response.status_code
        assert status_code == 401


# поиск фильма на английском языке

@pytest.mark.api
@allure.title("Поиск фильма на русском языке")
@allure.story("Поиск")
def test_search_film_name_eng():
    name = 'Star wars'
    url = f"https://kinopoiskapiunofficial.tech/api/v2.1/films/search-by-keyword?keyword={name}&page=1"
    key = os.getenv('API_KEY')
    payload = {}
    headers = {
        'accept': 'application/json',
        'X-API-KEY': key
    }
    with allure.step("Отправляем запрос"):
        response = requests.request("GET", url, headers=headers, data=payload)
        status_code = response.status_code
        resp = response.json()
    with allure.step("Проверяем статус-код"):
        assert status_code == 200
    with allure.step("Проверяем, что фильм нашёлся"):
        assert isinstance(resp, dict)
        keyword = resp["keyword"]
        pages_count = resp["pagesCount"]
        film = resp['films']
        assert keyword == name
        assert pages_count > 0
        assert isinstance(film, list)


@pytest.mark.api
@allure.title("Поиск фильма на русском языке")
@allure.story("Поиск")
# поиск фильма без названия
def test_search_film_no_name():
    name = ''
    url = f"https://kinopoiskapiunofficial.tech/api/v2.1/films/search-by-keyword?keyword={name}&page=1"
    key = os.getenv('API_KEY')
    payload = {}
    headers = {
        'accept': 'application/json',
        'X-API-KEY': key
    }
    with allure.step("Отправляем запрос"):
        response = requests.request("GET", url, headers=headers, data=payload)
    status_code = response.status_code
    resp = response.json()
    with allure.step("Проверяем статус-код"):
        assert status_code == 200
    with allure.step("Проверяем, что фильм НЕ нашёлся"):
        assert isinstance(resp, dict)
        keyword = resp["keyword"]
        pages_count = resp["pagesCount"]
        assert keyword == name
        assert pages_count == 0


@pytest.mark.api
@allure.title("Поиск фильма на русском языке")
@allure.story("Поиск")
# поиск фильма в названии номер
def test_search_film_number():
    name = '911'
    url = f"https://kinopoiskapiunofficial.tech/api/v2.1/films/search-by-keyword?keyword={name}&page=1"
    key = os.getenv('API_KEY')
    payload = {}
    headers = {
        'accept': 'application/json',
        'X-API-KEY': key
    }
    with allure.step("Отправляем запрос"):
        response = requests.request("GET", url, headers=headers, data=payload)
    status_code = response.status_code
    resp = response.json()
    with allure.step("Проверяем статус-код"):
        assert status_code == 200
    with allure.step("Проверяем, что фильм нашёлся"):
        assert isinstance(resp, dict)
        keyword = resp["keyword"]
        pages_count = resp["pagesCount"]
        assert keyword == name
        assert pages_count > 0
