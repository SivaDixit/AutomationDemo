import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def setup(request):
    options = Options()
    options.add_argument("--start-maximized")
    chrome_driver = webdriver.Chrome("C:/Users/dixit/PycharmProjects/PytestFramework/Pytest-Selenium-Framework/drivers/chromedriver.exe",options=options)
    chrome_driver.implicitly_wait(10)
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()
