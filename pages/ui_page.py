from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# создание класса
class MainPage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

# открыть главную страницу
    def open_main_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

# ввод фразы в строке поиска
    def search_by_phrase(self, phrase):
        search_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '[name="kp_query"]')))
        search_input.send_keys(phrase)
        self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

# получение результатов поиска
    def get_search_results(self) -> list:
        results_selector = 'js-serp-metrik'
        results = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, results_selector))
        )
        return results

# переход по разделам меню


# проверка заголовка главной страницы
