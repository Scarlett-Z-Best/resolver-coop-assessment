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

def get_cell(row, col):
    path = f'//div[@id="test-6-div"]//table//tbody/tr[{row + 1}]/td[{col + 1}]'
    return driver.find_element(By.XPATH, path).text

try:
    result = get_cell(2, 2)
    assert result == "Ventosanzap"
    print("Test 6 passed.")
except Exception as e:
    print("Test 6 failed:", e)

time.sleep(2)
driver.quit()
