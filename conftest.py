import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

@pytest.fixture(params=["firefox", "chrome"], scope="function")
def driver(request):
    """
    Parametrized fixture that yields both Firefox and Chrome drivers.
    Each test runs twice - once with Firefox, once with Chrome.
    """
    browser = request.param
    
    if browser == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    else:  # chrome
        options = ChromeOptions()
        driver = webdriver.Chrome(options=options)
    
    yield driver
    driver.quit()