from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"

service = Service(executable_path="C:/Users/23359/Downloads/geckodriver-v0.36.0-win32/geckodriver.exe")

driver = webdriver.Firefox(service=service, options=options)

driver.get("file:///C:/Users/23359/Desktop/QE-index.html")
time.sleep(1)

try:
    email_input = driver.find_element(By.XPATH, '//input[@type="email"]')
    password_input = driver.find_element(By.XPATH, '//input[@type="password"]')
    login_button = driver.find_element(By.XPATH, '//button[text()="Sign in"]')

    email_input.send_keys("test@example.com")
    password_input.send_keys("password123")
    login_button.click()

    print("Test 1 passed: Login button clicked.")
except Exception as e:
    print("Test 1 failed:", e)

time.sleep(3)
driver.quit()
