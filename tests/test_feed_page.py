import allure
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from data import User



@allure.feature("Главная страница")
class TestFeedPage:
    @allure.title("Переход по клику на Конструктор")
    def test_navigation_to_feed_page(self, driver):
        feed_page = FeedPage(driver)
        feed_page.load_page()
        feed_page.click_constructor_btn_header()
        main_page = MainPage(driver)
        main_page.assert_page_is_loaded()
    
    @allure.title("Счетчики заказов увеличиваются после создания заказа")
    def test_counter_total_is_rise_on_order_creation(self, driver):
        login_page = LoginPage(driver)
        login_page.login(User.EMAIL, User.PASSWORD)
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        feed_page.load_page()
        order_count_before_create = feed_page.get_total_orders_count()
        main_page.load_page()
        main_page.create_order(['Краторная булка N-200i', 'Говяжий метеорит (отбивная)'])
        feed_page.load_page()
        assert order_count_before_create < feed_page.get_total_orders_count()
    
    @allure.title("Счетчики заказов за сегодня увеличиваются после создания заказа")    
    def test_counter_today_is_rise_on_order_creation(self, driver):
        login_page = LoginPage(driver)
        login_page.login(User.EMAIL, User.PASSWORD)
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        feed_page.load_page()
        order_count_before_create = feed_page.get_today_orders_count()
        main_page.load_page()
        main_page.create_order(['Краторная булка N-200i', 'Говяжий метеорит (отбивная)'])
        feed_page.load_page()
        assert order_count_before_create < feed_page.get_today_orders_count()
        
    @allure.title("Созданный заказ отображается в Ленте заказов со статусом 'В работе'")
    def test_order_id_is_present_in_work_status(self, driver):
        login_page = LoginPage(driver)
        login_page.login(User.EMAIL, User.PASSWORD)
        main_page = MainPage(driver)
        main_page.create_order(['Краторная булка N-200i', 'Говяжий метеорит (отбивная)'])
        order_id = main_page.get_order_id()
        feed_page = FeedPage(driver)
        feed_page.load_page()
        assert order_id in feed_page.get_orders_ids_by_status("В работе")
        
        
        
        