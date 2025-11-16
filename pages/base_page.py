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
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

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
    
    @allure.step('Находим элементы')
    def _find_elements(self, locator):
        return self._wait.until(EC.presence_of_all_elements_located(locator))
    
    @allure.step('Проверяем что элемент кликабелен и не перекрыт')
    def check_element_clickable_not_overlay(self, driver, locator):
        element = EC.element_to_be_clickable(locator)(driver)

        if not element:
            return False

        is_obstructed = driver.execute_script("""
                const element = arguments[0];
                const rect = element.getBoundingClientRect();
                const x = rect.left + rect.width / 2;
                const y = rect.top + rect.height / 2;
                const topElement = document.elementFromPoint(x, y);
                return !element.isSameNode(topElement);
            """, element)

        return element if not is_obstructed else False
        
    @allure.step('Находим кликабельный элемент')
    def _find_clickable_element(self, locator):
        """
        Вспомогательный метод поиска кликабельного элемента
        """
        return self._wait.until(EC.element_to_be_clickable(locator))
        
    @allure.step('Кликаем по элементу с проверкой overlay')
    def click_on_element(self, locator):
        element = self._wait.until(
            lambda driver: self.check_element_clickable_not_overlay(driver, locator)
        )
        element.click()
        return self
    
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
        
    @allure.step('Элемент не присутсвует на странице')
    def _is_element_not_present(self, locator, timeout=3):
        """
        Проверка отсутствия элемента
        """
        try:
            wait = WebDriverWait(self._driver, timeout)
            wait.until(EC.invisibility_of_element_located(locator))
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
    
    @allure.step('Закрываем модальное окно')
    def close_modal(self, modal_title):
        self._find_clickable_element(BaseLocators.get_modal_close_button_by_modal_title(modal_title)).click()
        
    @allure.step('Проверяем что модального окна нет')
    def assert_modal_is_closed(self, name):
        assert self._is_element_not_present(BaseLocators.get_modal_title_locator(name)) == True
        
    @allure.step('Перетаскиваем элемент')
    def _drag_and_drop(self, source_locator, target_locator):
        actions = ActionChains(self._driver)
        self._scroll_to_element(source_locator)
        source_element = self._find_element(source_locator)
        target_element = self._find_element(target_locator)
        self._driver.execute_script(
            """
            var source = arguments[0];
            var target = arguments[1];
            var evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
            """,
            source_element,
            target_element
        )
        