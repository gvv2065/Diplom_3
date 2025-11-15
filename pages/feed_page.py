from .base_page import BasePage
from locators.feed_page_locators import FeedPageLocators
from data import Url
import allure


class FeedPage(BasePage):
    @allure.step('Открываем страницу лента заказов')
    def load_page(self):
        self.open_page(Url.FEED_PAGE)
        return self
    
    @allure.step('Нажимаем в заголовке Конструктор')
    def click_constructor_btn_header(self):
        self._find_clickable_element(FeedPageLocators.CONSTRUCTOR_BUTTON).click()
        return self
            
    @allure.step('Проверяем что открыта страница Лента заказов')
    def assert_page_is_loaded(self):
        self.assert_current_page_url(Url.FEED_PAGE)
        assert self._is_element_present(FeedPageLocators.ORDERS_FEED_COMPONENT) == True
        assert self._is_element_present(FeedPageLocators.ORDERS_DATA_COMPONENT) == True