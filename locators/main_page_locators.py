from selenium.webdriver.common.by import By


class MainPageLocators:
    HEADER = (By.XPATH, "//main//h1[text()='Соберите бургер']")
    FEED_BUTTON = (By.XPATH, "//header//p[text()='Лента Заказов']")
    INGREDIENT_COMPONENT = (By.XPATH, "//main//section[contains(@class,'BurgerIngredients_ingredients')]")
    BASKET_COMPONENT = (By.XPATH, "//main//section[contains(@class,'BurgerConstructor_basket')]")
    CONSTRUCTOR_ITEMS_LIST = (By.XPATH, "//ul[contains(@class,'BurgerConstructor_basket__list')]")
    INGREDIENT_DETAILS_HEADER = (By.XPATH, "//h2[contains(@class,'Modal_modal__title') and text()='Детали ингредиента']")
    ORDER_MODAL_HEADER = (By.XPATH, "//div[contains(@class,'Modal_modal__contentBox')]//p[text()='идентификатор заказа']")
    ORDER_MODAL_ID = (By.XPATH, "//h2[contains(@class,'Modal_modal__title')]")
    LOGIN_BTN = (By.XPATH, "//button[text()='Войти в аккаунт']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
        
    @staticmethod
    def get_ingredient_count(ingredient_name):
        return (By.XPATH, f"//p[contains(@class,'BurgerIngredient_ingredient') and text()='{ingredient_name}']//ancestor::a//p[contains(@class,'counter_counter__num')]")
    
    @staticmethod
    def get_ingredient_draggable_locator_by_name(ingredient_name):
        return (By.XPATH, f"//p[contains(@class,'BurgerIngredient_ingredient') and text()='{ingredient_name}']//ancestor::a")
