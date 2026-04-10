### Дипломный проект по Автоматизации UI- и API финального проекта  по ручному тестированию
 [ссылка на проект](https://vera116.yonote.ru/share/a187b917-90c6-466d-8811-4698616e5a2c)
## Шаги работы
 1. Склонировать проект 'git clone https://github.com/ZVApro/Diploma.git
 2. Установить зависимости
 3. Запустить тесты 
## Команды для запуска тестов
Все тесты (UI + API):
bash
pytest 

Только API тесты
bash
pytest -m api -v

Только UI тесты
bash
pytest -m ui -v

Запуск с Allure отчетом
bash
pytest --alluredir=allure-results -v
allure serve allure-results

Запуск конкретного тестового файла
bash
pytest tests/test_api_kp.py -v
pytest tests/test_ui.py -v


## Стек:
-selenium,
-requests,
-pytest,
-allure.
 
## Настройка переменных окружения
Создание файла .env и заполнить необходимые значения:
    API_KEY="ВАШ КЛЮЧ"
    BASE_URL=https://poiskkino.dev/

## Библиотеки 
- pip install pytest
- pip install selenium
- pip install webdriver-manager
- pip install allure-pytest
- pip install requests
- 
