from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def go_to_page():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:5500/docs/index.html")
    return driver

def submit(driver,name):
    driver.find_element(By.CSS_SELECTOR, "#name-input").send_keys(name)
    driver.find_element(By.ID, "submit-button").click()
    text=driver.find_element(By.ID, "message-p").text
    return text

def ass(text):
    assert "Hello John Doe!"==text

goto= go_to_page()
text=submit(goto,"John Doe")
ass(text)
text=submit(goto,"Jack Doe")
ass(text)


print("End")