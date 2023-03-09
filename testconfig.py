import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    # Initialize the ChromeDriver instance
    driver = webdriver.Chrome()

    # Wait for the page to load
    driver.implicitly_wait(10)

    yield driver
    
    # Quit the driver instance
    driver.quit()