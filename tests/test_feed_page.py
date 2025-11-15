import allure
from pages.feed_page import FeedPage
from pages.main_page import MainPage


@allure.feature("Главная страница")
class TestFeedPage:
    @allure.title("Переход по клику на Конструктор")
    def test_navigation_to_feed_page(self, driver):
        feed_page = FeedPage(driver)
        feed_page.load_page()
        feed_page.click_constructor_btn_header()
        main_page = MainPage(driver)
        main_page.assert_page_is_loaded()
    