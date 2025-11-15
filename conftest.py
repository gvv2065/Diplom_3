import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(params=["firefox", "chrome"], scope="function")
def driver(request):
    """
    Parametrized fixture that yields both Firefox and Chrome drivers.
    Each test runs twice - once with Firefox, once with Chrome.
    """
    browser = request.param
    
    if browser == "firefox":
        options = FirefoxOptions()
        # options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    else:  # chrome
        options = ChromeOptions()
        # options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    
    yield driver
    driver.quit()
    
    
# @pytest.fixture(scope="function")
# def driver():
#     # driver = webdriver.Chrome(ChromeDriverManager().install())
#     options = ChromeOptions()
    
#     # options.add_argument("--headless")
#     driver = webdriver.Chrome(options)
#     yield driver
#     driver.quit()