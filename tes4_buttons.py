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
    buttons = driver.find_elements(By.XPATH, '//div[@id="test-4-div"]//button')

    assert len(buttons) == 2, "Did not find exactly 2 buttons"

    assert buttons[0].is_enabled(), "First button is not enabled"
    print("Test 4 step 1 passed: First button is enabled.")

    assert not buttons[1].is_enabled(), "Second button is not disabled"
    print("Test 4 step 2 passed: Second button is disabled.")

except Exception as e:
    print("Test 4 failed:", e)

time.sleep(2)
driver.quit()
