# поиск по названию, проверить что в теле ответа есть
import os

from dotenv import load_dotenv
load_dotenv()
import requests
import pytest


def test_search_film_name():
    name = os.getenv('FILM_NAME')
    url = f"https://kinopoiskapiunofficial.tech/api/v2.1/films/search-by-keyword?keyword={name}&page=1"
    key = os.getenv('API_KEY')
    payload = {}
    headers = {
        'accept': 'application/json',
        'X-API-KEY': key
    }


    response = requests.request("GET", url, headers=headers, data=payload)
    status_code = response.status_code
    resp = response.json()
    assert status_code == 200
    assert isinstance(resp, dict)
    keyword = resp["keyword"]
    pages_count = resp["pagesCount"]
    film = resp['films']
    assert keyword == "Мачеха"
    assert pages_count > 0
    assert isinstance(film, list)

    print(response.text)


# переход на раздел "фильмы", список фильмов

def test





# поиск персоны (режиссера) и список его фильмов
# запрос с неправильным токеном, ожидаемая ошибка
#
