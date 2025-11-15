from selenium.webdriver.common.by import By


class FeedPageLocators:
    HEADER = (By.XPATH, "//main//h1[text()='Лента заказов']")
    ORDERS_FEED_COMPONENT = (By.XPATH, "//main//ul[contains(@class,'OrderFeed_list')]")
    ORDERS_DATA_COMPONENT = (By.XPATH, "//main//div[contains(@class,'OrderFeed_ordersData')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//header//p[text()='Конструктор']")
    