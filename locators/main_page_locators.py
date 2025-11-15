from selenium.webdriver.common.by import By


class MainPageLocators:
    HEADER = (By.XPATH, "//main//h1[text()='Соберите бургер']")
    FEED_BUTTON = (By.XPATH, "//header//p[text()='Лента Заказов']")
    INGREDIENT_COMPONENT = (By.XPATH, "//main//section[contains(@class,'BurgerIngredients_ingredients')]")
    BASKET_COMPONENT = (By.XPATH, "//main//section[contains(@class,'BurgerConstructor_basket')]")
    CONSTRUCTOR_ITEMS_LIST = (By.XPATH, "//ul[contains(@class,'BurgerConstructor_basket__list')]")
    INGREDIENT_DETAILS_HEADER = (By.XPATH, "//h2[contains(@class,'Modal_modal__title') and text()='Детали ингредиента']")
    INGREDIENT_COUNTER = (By.XPATH, "//p[contains(@class,'counter_counter__num')]")
    
    @staticmethod
    def get_ingredient_locator_by_name(ingredient_name):
        return (By.XPATH, f"//p[contains(@class,'BurgerIngredient_ingredient') and text()='{ingredient_name}']")
    
    @staticmethod
    def get_ingredient_count(ingredient_name):
        return (By.XPATH, f"//p[contains(@class,'BurgerIngredient_ingredient') and text()='{ingredient_name}']//ancestor::a//p[contains(@class,'counter_counter__num')]")
    
    @staticmethod
    def get_ingredient_draggable_locator_by_name(ingredient_name):
        return (By.XPATH, f"//p[contains(@class,'BurgerIngredient_ingredient') and text()='{ingredient_name}']//ancestor::a")
