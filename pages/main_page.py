from selenium.webdriver.common.by import By
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import Url
import allure


class MainPage(BasePage):
    @allure.step('Открываем главную страницу')
    def load_page(self):
        self.open_page(Url.MAIN_PAGE)
        return self
    
    @allure.step('Нажимаем в заголовке Лента Заказов')
    def click_feed_btn_header(self):
        self._find_clickable_element(MainPageLocators.FEED_BUTTON).click()
        return self
    
    @allure.step('Проверяем что открыта Главная страница')
    def assert_page_is_loaded(self):
        self.assert_current_page_url(Url.MAIN_PAGE)
        self._is_element_present(MainPageLocators.HEADER)
        self._is_element_present(MainPageLocators.INGREDIENT_COMPONENT)
        self._is_element_present(MainPageLocators.BASKET_COMPONENT)
        

    
