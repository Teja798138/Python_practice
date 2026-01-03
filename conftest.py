import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from Utilities.Readproperties import ReadConfig

@pytest.fixture(scope="session")
def setup_browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(ReadConfig.getBaseurl())
    yield driver
    driver.quit()