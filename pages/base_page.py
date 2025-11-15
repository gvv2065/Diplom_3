"""
Базовый класс для всех Page Object классов
Общая функциональность для работы со страницами
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.base_locators import BaseLocators
from selenium.webdriver.common.keys import Keys
import allure

class BasePage:
    """
    Базовый класс для всех страниц
    Содержит общие вспомогательные методы
    """
    
    def __init__(self, driver):
        """
        Хранит WebDriver внутри класса
        Внешний код не работает с драйвером напрямую
        """
        self._driver = driver
        self._wait = WebDriverWait(driver, 10)
        
    @allure.step('Находим элемент')
    def _find_element(self, locator):
        """
        Вспомогательный метод поиска элемента
        Скрывает детали работы с WebDriver
        """
        return self._wait.until(EC.presence_of_element_located(locator))
    
    @allure.step('Находим кликабельный элемент')
    def _find_clickable_element(self, locator):
        """
        Вспомогательный метод поиска кликабельного элемента
        """
        return self._wait.until(EC.element_to_be_clickable(locator))
    
    @allure.step('Элемент присутсвует на странице')
    def _is_element_present(self, locator, timeout=3):
        """
        Проверка наличия элемента
        """
        try:
            wait = WebDriverWait(self._driver, timeout)
            wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False
        
    @allure.step('Открываем страницу')
    def open_page(self, url):
        """
        Публичный метод открытия страницы
        Открывает указанный URL
        """
        self._driver.get(url)
    
    @allure.step('Получаем текущую страницу')
    def get_current_url(self):
        return self._driver.current_url
    
    @allure.step('Переходим на вкладку')
    def switch_to_tab(self, tab_index):
        self._driver.switch_to.window(self._driver.window_handles[tab_index])
    
    @allure.step('Пороверяем текущий урл')
    def assert_current_page_url(self, expected_url):
        WebDriverWait(self._driver, 3).until(
            lambda driver: driver.current_url == expected_url
        )

    @allure.step('Скроллим до элемента')
    def _scroll_to_element(self, locator):
        element = self._find_element(locator)
        self._driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self._driver, 10000).until(
            EC.visibility_of(element)
        )
        return element
    
    @allure.step('Заполняем поле')
    def _fill_input(self, locator, value):
        element = self._find_element(locator)
        element.send_keys(value)
        return self
    
    @allure.step('Заполняем дату')
    def _fill_input_date(self, locator, value):
        element = self._find_element(locator)
        element.send_keys(value)
        element.send_keys(Keys.ESCAPE)
        return self
    
    @allure.step('Заполняем поисковое поле и выбираем из списка')
    def _fill_search(self, locator, value):
        self._find_element(locator).send_keys(value)
        self._find_element(BaseLocators.get_search_locator(value)).click()
        return self
    
    @allure.step('Выбираем из списка')
    def _fill_select(self, locator, value):
        self._find_element(locator).click()
        self._find_element(BaseLocators.get_option_locator(value)).click()
        return self
    
    @allure.step('Заполняем чекбокс')
    def _fill_checkbox(self, checkbox_group_name, value):
        self._find_element(BaseLocators.get_checkbox_locator(checkbox_group_name, value)).click()
        return self
    
    @allure.step('Проверяем что появилось модальное окно с текстом и кнопками')
    def _assert_modal(self, modal_text, buttons_text):
        self._find_element(BaseLocators.get_modal_locator(modal_text))
        for button in buttons_text:
            self._find_clickable_element(BaseLocators.get_modal_button(button))
