import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

@pytest.fixture
def setup():
    chrome_options = Options()

    if os.getenv("CI"):
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://magento.softwaretestingboard.com")
    yield driver
    driver.quit()
