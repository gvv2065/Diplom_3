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
        self.click_on_element(MainPageLocators.FEED_BUTTON)
        return self
    
    @allure.step('Нажимаем на ингредиент')
    def click_ingredient(self, ingredient_name):
        locator = MainPageLocators.get_ingredient_draggable_locator_by_name(ingredient_name)
        self._scroll_to_element(locator)
        self._find_clickable_element(locator).click()
        return self
    
    @allure.step('Проверяем что открыта Главная страница')
    def assert_page_is_loaded(self):
        self.assert_current_page_url(Url.MAIN_PAGE)
        assert self._is_element_present(MainPageLocators.HEADER) == True
        assert self._is_element_present(MainPageLocators.INGREDIENT_COMPONENT) == True
        assert self._is_element_present(MainPageLocators.BASKET_COMPONENT) == True
    
    @allure.step('Проверяем что отображается попап Детали ингредиента')    
    def assert_ingredient_modal_is_displayed(self):
        assert self._is_element_present(MainPageLocators.INGREDIENT_DETAILS_HEADER) == True
        

    @allure.step('Добавляем ингредиент в корзину перетаскиванием')
    def add_ingredient_to_basket(self, ingredient_name):
        self._drag_and_drop(
            MainPageLocators.get_ingredient_draggable_locator_by_name(ingredient_name),
            MainPageLocators.CONSTRUCTOR_ITEMS_LIST
        )

    @allure.step('Создаем заказ из списка ингредиентов')
    def create_order(self, ingredients: list[str]):
        for ingredient in ingredients:
            self.add_ingredient_to_basket(ingredient)
        self.click_on_element(MainPageLocators.ORDER_BUTTON)
    
    @allure.step('Получаем ID созданного заказа')
    def get_order_id(self):
        self._is_element_present(MainPageLocators.ORDER_MODAL_HEADER)
        self.click_on_element(MainPageLocators.ORDER_MODAL_HEADER)
        return self._find_element(MainPageLocators.ORDER_MODAL_ID).text
    
    @allure.step('Получаем количество ингредиента в счётчике')    
    def _get_ingredient_count(self, ingredient_name):
        return int(self._find_element(MainPageLocators.get_ingredient_count(ingredient_name)).text)
    
    @allure.step('Проверяем количество ингредиента в счётчике')
    def assert_ingredient_counter(self, ingredient_name, expected_count):
        actual_count = self._get_ingredient_count(ingredient_name)
        assert expected_count == actual_count
        
    
