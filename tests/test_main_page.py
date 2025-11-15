import allure
from pages.feed_page import FeedPage
from pages.main_page import MainPage


@allure.feature("Главная страница")
class TestMainPAge:
    @allure.title("Переход по клику на Ленту заказов")
    def test_navigation_to_feed_page(self, driver):
        main_page = MainPage(driver)
        main_page.load_page()
        main_page.click_feed_btn_header()
        feed_page = FeedPage(driver)
        feed_page.assert_page_is_loaded()
    