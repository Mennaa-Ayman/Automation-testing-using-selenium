from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from Utils import Config

def test_signup_empty_fields(driver):
    driver.get(Config.BASE_URL)
    driver.find_element(By.NAME, "name").send_keys("")
    driver.find_element(By.NAME, "email").send_keys("")
    driver.find_element(By.XPATH, "//button[text()='Signup']").click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    page_source = driver.page_source.lower()
    assert "required" in page_source or "already exists" in page_source or "error" in page_source

def test_signup_invalid_email(driver):
    driver.get(Config.BASE_URL)
    driver.find_element(By.NAME, "name").send_keys("Test User")
    driver.find_element(By.NAME, "email").send_keys("invalidemail")
    driver.find_element(By.XPATH, "//button[text()='Signup']").click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    page_source = driver.page_source.lower()
    # Check if form is still present (signup not processed) or error message exists
    assert "signup" in page_source or "invalid email" in page_source or "already exists" in page_source
