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
    list_items = driver.find_elements(By.XPATH, '//div[@id="test-2-div"]//li')

    assert len(list_items) == 3, f"Expected 3 list items, but found {len(list_items)}"

    second_item_text = list_items[1].text.split()[0:3]
    assert " ".join(second_item_text) == "List Item 2", f"Second item text is incorrect: {' '.join(second_item_text)}"

    badge_value = driver.find_element(By.XPATH, '(//div[@id="test-2-div"]//li)[2]/span').text
    assert badge_value == "6", f"Expected badge value 6, but found {badge_value}"

    print("Test 2 passed successfully.")

except Exception as e:
    print("Test 2 failed:", e)

time.sleep(2)
driver.quit()
