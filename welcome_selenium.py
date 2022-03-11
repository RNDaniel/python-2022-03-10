from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def go_to_page():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:5500/docs/index.html")
    return driver

def get_text_of_paragraph(driver):
    text=driver.find_element(By.CSS_SELECTOR, ".important-p").text
    return text

driver= go_to_page()
text=get_text_of_paragraph(driver)

assert "This is the second paragraph"==get_text_of_paragraph(driver)
#print(text)
print("End")

