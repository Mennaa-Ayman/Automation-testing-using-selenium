from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from Utils import Config

def test_login_valid(driver):
    driver.get(Config.BASE_URL)
    driver.find_element(By.NAME, "email").send_keys(Config.VALID_EMAIL)
    driver.find_element(By.NAME, "password").send_keys(Config.VALID_PASSWORD)
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    page_source = driver.page_source.lower()
    assert "logged in" in page_source or "home" in page_source or "dashboard" in page_source

def test_login_invalid(driver):
    driver.get(Config.BASE_URL)
    driver.find_element(By.NAME, "email").send_keys(Config.INVALID_EMAIL)
    driver.find_element(By.NAME, "password").send_keys(Config.INVALID_PASSWORD)
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    page_source = driver.page_source.lower()
    assert "incorrect" in page_source or "invalid" in page_source or "error" in page_source

