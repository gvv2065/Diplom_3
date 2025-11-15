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
        self.click_on_element(FeedPageLocators.CONSTRUCTOR_BUTTON)
        return self
            
    @allure.step('Проверяем что открыта страница Лента заказов')
    def assert_page_is_loaded(self):
        self.assert_current_page_url(Url.FEED_PAGE)
        assert self._is_element_present(FeedPageLocators.ORDERS_FEED_COMPONENT) == True
        assert self._is_element_present(FeedPageLocators.ORDERS_DATA_COMPONENT) == True
       
    @allure.step('Получаем общее количество заказов') 
    def get_total_orders_count(self):
        return int(self._find_element(FeedPageLocators.TOTAL_ORDERS_COUNT).text)
    
    @allure.step('Получаем количество заказов за сегодня')
    def get_today_orders_count(self):
        return int(self._find_element(FeedPageLocators.TODAY_ORDERS_COUNT).text)
    
    @allure.step('Получаем ID заказов по статусу')
    def get_orders_ids_by_status(self, status):
        order_elements = self._find_elements(FeedPageLocators.get_orders_ids_by_status_locator(status))
        return [element.text for element in order_elements]