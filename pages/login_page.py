from selenium.webdriver.common.by import By

from locators.main_page_locators import MainPageLocators
from .base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from data import Url
import allure


class LoginPage(BasePage):
    @allure.step('Логинимся')
    def login(self, email, password):
        self._driver.get(Url.LOGIN_PAGE)
        self._find_element(LoginPageLocators.EMAIL_FIELD).send_keys(email)
        self._find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.click_on_element(LoginPageLocators.LOGIN_BUTTON)
        # считаем что мы успешно залогинились если есть кнопка "Оформить заказ"
        assert self._is_element_present(MainPageLocators.ORDER_BUTTON) == True
        return self
