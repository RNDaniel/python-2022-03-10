import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locations_po import LocationsPage
#from locations_rest_api import create_location, delete_all_locations
from locations_db import create_location, delete_all_locations
from read_locations import read_locations


@pytest.fixture
def driver():
    # feldobja a böngészőt
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    delete_all_locations()
    return driver
# asd


def test_create(driver: webdriver.Chrome):
    """Teszteset létrehozása"""
    page = LocationsPage(driver)

    # when
    page.click_on_create_location()
    page.fill_create_form("Home", "1,1")
    page.click_on_create_location_submit()

    # then
    page.wait_for_message("Location has been created")

    name, coords = page.get_first_location()
    assert name == "Home"
    assert coords == "1, 1"


def test_negativ(driver: webdriver.Chrome):
    page = LocationsPage(driver)
    page.click_on_create_location()
    page.click_on_create_location_submit()
    page.wait_for_name_message("Can not be empty name!")

    # given

    assert page.has_name_red_border()
    page.wait_for_table_has_rows(0)


def test_edit(driver: webdriver.Chrome):
    # Given: legyen az adatbázisban egy test ... nevű location
    create_location("Test", "5,5")

    page = LocationsPage(driver)
    page.wait_for_table_has_rows(1)

    page.click_on_first_edit_button()
    page.fill_update_form("Test2", "8,8")
    page.click_on_update_location_submit()

    page.wait_for_message("Location has been modified")
    page.wait_for_table_has_rows(1)

    name, coords = page.get_first_location()
    assert name == "Test2"
    assert coords == "8, 8"


def test_delete(driver: webdriver.Chrome):
    create_location("Test", "5,5")

    page = LocationsPage(driver)
    page.wait_for_table_has_rows(1)
    page.click_on_first_delete_button()
    page.click_on_delete_submit()
    page.wait_for_message("Location has been deleted")
    page.wait_for_table_has_rows(0)


def test_with_data_driven(driver):
    page = LocationsPage(driver)

    for name, coords in read_locations():
        page.click_on_create_location()
        page.fill_create_form(name, coords)
        page.click_on_create_location_submit()
        page.wait_for_message("Location has been created")

    page.wait_for_table_has_rows(10)
