from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from tests.testSettings import *


@pytest.fixture()
def driver(driver):
    driver.get(EXCEPTION_PAGE_URL)
    yield driver

@pytest.mark.redirect
@pytest.mark.positive
def test_exception_page(driver):
    assert EXCEPTION_PAGE_URL == driver.current_url


@pytest.mark.exception
@pytest.mark.negative
def test_new_row(driver):
    #Locators
    addButtonLocator = driver.find_element(By.NAME, "Add")
    addButtonLocator.click()
    secondRowLocator = driver.find_element(By.XPATH, "//div[@id='row2']/input[@type='text']")

    assert secondRowLocator.is_displayed(), "Row 2 input is not displayed"