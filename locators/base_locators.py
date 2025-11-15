from selenium.webdriver.common.by import By


class BaseLocators:
    @staticmethod
    def get_modal_title_locator(modal_title):
        return (By.XPATH, f"//div[contains(@class,'ModalHeader') and text()='{modal_title}']")
    
    @staticmethod
    def get_modal_close_button_by_modal_title(modal_title):
        return (By.XPATH, f"""//h2[contains(@class,'Modal_modal__title') and text()='{modal_title}']
                //ancestor::div[contains(@class,'Modal_modal__container')]//button[contains(@class,'Modal_modal__close')]""")