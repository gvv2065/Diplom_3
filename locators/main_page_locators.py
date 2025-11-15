from selenium.webdriver.common.by import By


class MainPageLocators:
    HEADER = (By.XPATH, "//main//h1[text()='Соберите бургер']")
    FEED_BUTTON = (By.XPATH, "//header//p[text()='Лента Заказов']")
    INGREDIENT_COMPONENT = (By.XPATH, "//main/section[contains(@class,'BurgerIngredients_ingredients')]")
    BASKET_COMPONENT = (By.XPATH, "//main/section[contains(@class,'BurgerIngredients_basket')]")