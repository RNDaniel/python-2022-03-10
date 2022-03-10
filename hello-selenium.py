from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://python.org")
driver.find_element(By.ID, "id-search-field").send_keys("precedence")
driver.find_element(By.ID, "submit").click()
print("End")