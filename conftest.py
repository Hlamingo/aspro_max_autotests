import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

@pytest.fixture(scope = 'session')
def browser():
    # ~ user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) \
    # ~ Gecko/20100101 Firefox/128.0'
    # ~ options = Options()
    # ~ options.set_preference("general.useragent.override", user_agent)
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()
