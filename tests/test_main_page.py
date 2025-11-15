import allure
from pages.feed_page import FeedPage
from pages.main_page import MainPage


@allure.feature("Главная страница")
class TestMainPage:
    @allure.title("Переход по клику на Ленту заказов")
    def test_navigation_to_feed_page(self, driver):
        main_page = MainPage(driver)
        main_page.load_page()
        main_page.assert_page_is_loaded()
        main_page.click_feed_btn_header()
        feed_page = FeedPage(driver)
        feed_page.assert_page_is_loaded()
        
        
    @allure.title("При клике на ингредиент открывается попап с деталями ингредиента")
    def test_ingredient_popup(self, driver):
        main_page = MainPage(driver)
        main_page.load_page()
        main_page.click_ingredient("Говяжий метеорит (отбивная)")
        main_page.assert_ingredient_modal_is_displayed()
        
    @allure.title("Модальное окно с деталями ингредиента закрывается при клике на крестик")
    def test_ingredient_popup_close(self, driver):
        main_page = MainPage(driver)
        main_page.load_page()
        main_page.click_ingredient("Говяжий метеорит (отбивная)")
        main_page.assert_ingredient_modal_is_displayed()
        main_page.close_modal("Детали ингредиента")
        main_page.assert_modal_is_closed("Детали ингредиента")  
    
    @allure.title("Проверка счетчика ингредиента при добавлении ингредиента в корзину")
    def test_ingredient_counter(self, driver):
        main_page = MainPage(driver)
        main_page.load_page()
        main_page.assert_ingredient_counter("Говяжий метеорит (отбивная)", 0)
        main_page.add_ingredient_to_basket("Говяжий метеорит (отбивная)")
        main_page.assert_ingredient_counter("Говяжий метеорит (отбивная)", 1)
        