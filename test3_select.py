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
    dropdown_button = driver.find_element(By.ID, "dropdownMenuButton")

    default_text = dropdown_button.text
    assert default_text == "Option 1", f"Expected default to be 'Option 1', but got '{default_text}'"
    print("Test 3 step 1 passed: Default value is Option 1.")

    dropdown_button.click()
    time.sleep(1)

    option_3 = driver.find_element(By.XPATH, '//div[@class="dropdown-menu show"]//a[text()="Option 3"]')
    option_3.click()
    print("Test 3 step 2 passed: Option 3 selected.")

except Exception as e:
    print("Test 3 failed:", e)

time.sleep(2)
driver.quit()
