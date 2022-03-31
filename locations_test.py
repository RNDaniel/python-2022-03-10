from urllib import request
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locations_waits import table_became_empty
import uuid
import requests

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8080")
    requests.delete("http://127.0.0.1:8080/api/locations")
    return driver

def test_create(driver: webdriver.Chrome):
    #given
    
    #when
    driver.find_element(By.LINK_TEXT,"Create location").click()
    driver.find_element(By.ID, "location-name").send_keys("Home")
    driver.find_element(By.ID, "location-coords").send_keys("1,1")
    driver.find_element(By.CLASS_NAME,"btn-primary").click()
    #then
    wait = WebDriverWait(driver,3)
    wait.until(EC.text_to_be_present_in_element((By.ID,"message-div"),\
        "Location has been created"))

    message = driver.find_element(By.ID,"message-div").text
    assert message == "Location has been created"

    name_cell_text = driver.find_element(By.CSS_SELECTOR,\
        "#locations-table-tbody > tr > td:nth-child(2)").text

    assert name_cell_text == "Home"

    coord_cell_text = driver.find_element(By.CSS_SELECTOR,\
        "#locations-table-tbody > tr > td:nth-child(3)").text

    assert coord_cell_text == "1, 1"
    #locations-table-tbody > tr > td:nth-child(3)

def test_negativ(driver: webdriver.Chrome):
    #given
    
    #when
    driver.find_element(By.LINK_TEXT,"Create location").click()
    #driver.find_element(By.ID, "location-name").send_keys("")
    #driver.find_element(By.ID, "location-coords").send_keys("1,1")
    driver.find_element(By.CLASS_NAME,"btn-primary").click()
    #then
    wait = WebDriverWait(driver,3)
    wait.until(EC.text_to_be_present_in_element((By.ID,"location-name-feedback"),\
       "Can not be empty name!"))

    wait.until(EC.text_to_be_present_in_element((By.ID,"location-coords-feedback"),\
       "Invalid format!"))
    
    red = driver.find_element(By.ID,"location-name")
    assert 'is-invalid' in red.get_attribute('class').split()

    red2 = driver.find_element(By.ID,"location-coords")
    assert 'is-invalid' in red2.get_attribute('class').split()

    #rows = driver.find_elements(By.CSS_SELECTOR, "#locations-table-tbody > tr")
    #assert len(rows) == 0

    #driver.find_element(By.ID,"refresh-button").click()

    wait.until(table_became_empty())

def test_edit(driver: webdriver.Chrome):
    name= "Test" + str(uuid.uuid4())
    data = {"name": name, "coords":"5,5"}
    requests.post("http://127.0.0.1:8080/api/locations",json=data)

    driver.find_element(By.ID,"refresh-button").click()

    wait = WebDriverWait(driver,3)
    link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,\
        "#locations-table-tbody > tr > td:nth-child(6) > button.btn.btn-link")))

    link.click()

  


   
