from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"

service = Service(executable_path="C:/Users/23359/Downloads/geckodriver-v0.36.0-win32/geckodriver.exe")

driver = webdriver.Firefox(service=service, options=options)
driver.get("file:///C:/Users/23359/Desktop/QE-index.html")

try:
    wait = WebDriverWait(driver, 10)

    button = wait.until(EC.presence_of_element_located((By.ID, "test5-button")))
    print("Test 5 step 1 passed: Button appeared in DOM.")

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
    time.sleep(0.5)

    wait.until(EC.element_to_be_clickable((By.ID, "test5-button")))
    print("Test 5 step 2 passed: Button is clickable.")

    button.click()
    print("Test 5 step 3 passed: Button clicked.")

    success_msg = driver.find_element(By.ID, "test5-alert")
    assert success_msg.is_displayed()
    print("Test 5 step 4 passed: Success message displayed.")

    assert not button.is_enabled()
    print("Test 5 step 5 passed: Button is now disabled.")

except Exception as e:
    print("Test 5 failed:", e)

driver.quit()
