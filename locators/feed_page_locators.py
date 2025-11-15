from selenium.webdriver.common.by import By


class FeedPageLocators:
    HEADER = (By.XPATH, "//main//h1[text()='Лента заказов']")
    ORDERS_FEED_COMPONENT = (By.XPATH, "//main//ul[contains(@class,'OrderFeed_list')]")
    ORDERS_DATA_COMPONENT = (By.XPATH, "//main//div[contains(@class,'OrderFeed_ordersData')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//header//p[text()='Конструктор']")
    TOTAL_ORDERS_COUNT = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_ORDERS_COUNT = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    
    @staticmethod
    def get_orders_ids_by_status_locator(status):
        if status == 'Готовы':
            return (By.XPATH, "//ul[contains(@class,'OrderFeed_orderList__')]//li[contains(@class,'text_type_digits')]")
        elif status == 'В работе':
            return (By.XPATH, "//ul[contains(@class,'OrderFeed_orderListReady__')]//li[contains(@class,'text_type_digits')]")
        else:
            raise ValueError(f"Unknown status: {status}")
    