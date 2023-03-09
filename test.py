from testconfig import driver
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_insert_text(driver):
    # Set explicit wait to 10 seconds
    wait = WebDriverWait(driver, 10)

    # Open Google Docs new document with login form
    driver.get("https://docs.new")

    # Maximize window
    driver.maximize_window()

    # Find sign in email field and enter email
    email_field = wait.until(EC.visibility_of_element_located((By.ID, "identifierId")))
    email_field.send_keys("test.goran.rosulj@gmail.com")

    # Find and click on Next button
    next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#identifierNext button")))
    next_button.click()

    # Find password field and enter password
    pwd_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#password input")))
    pwd_field.send_keys("thisis4learning")

     # Find and click on Next password button
    next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#passwordNext button")))
    next_button.click()

    # # Find the body element and insert the text
    canvas = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='kix-appview']//canvas")))
    ActionChains(driver).move_to_element(canvas).click(canvas).send_keys("Hello, world!").perform()
    

    # Find the "Heading 1" button and click it
    normal_text = wait.until(EC.visibility_of_element_located((By.ID, ":x"))).click()
    header1_text = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id=':fd']//span"))).click()


    # Verify that the text is now in the "Heading 1" style
    header_check = driver.find_element(By.CSS_SELECTOR, ".navigation-widget-content .navigation-item .navigation-item-content")
    assert "Hello, world!" in header_check.get_attribute('data-tooltip')
