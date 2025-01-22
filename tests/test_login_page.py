#Import selenium
from selenium import webdriver
from tests.testSettings import *
import time
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def driver():
    #Open browser
    driver = webdriver.Chrome()

    #Open the website
    driver.get(TARGET_URL)

    #Click on the Practice link
    practiceButtonLocator = driver.find_element(By.ID, "menu-item-20")
    practiceButtonLocator.click()

    #Select the Test Login Page
    testLoginPageLocator = driver.find_element(By.XPATH, "//*[@id='loop-container']/div/article/div[2]/div[1]/div[1]/p/a")
    testLoginPageLocator.click()
    
    yield driver
    driver.quit()
    
@pytest.mark.positive
def test_login_page_url(driver):
    assert LOGIN_PAGE_URL in driver.current_url    

@pytest.mark.positive
@pytest.mark.login
def test_positive_login(driver):
    #Login locators
    loginLocator = driver.find_element(By.ID, "username")
    passwordLocator = driver.find_element(By.ID, "password")
    loginButtonLocator = driver.find_element(By.ID, "submit")
    
    #Enter login & password
    loginLocator.send_keys(CORRECT_USERNAME)
    passwordLocator.send_keys(CORRECT_PASSWORD)
    loginButtonLocator.click()

    #Check if the login was successful
    textLocator = driver.find_element(By.TAG_NAME, "h1")
    logoutLocator = driver.find_element(By.LINK_TEXT, "Log out")

    assert SUCESSFUL_URL_PART in driver.current_url 

    assert textLocator.text == SUCCESSFUL_TEXT

    assert logoutLocator.is_displayed()

@pytest.mark.negative
@pytest.mark.login
def test_invalid_login(driver):
    #Login locators
    loginLocator = driver.find_element(By.ID, "username")
    passwordLocator = driver.find_element(By.ID, "password")
    loginButtonLocator = driver.find_element(By.ID, "submit")
    
    #Enter invalid login
    loginLocator.send_keys(INCORRECT_USERNAME)
    passwordLocator.send_keys(CORRECT_PASSWORD)
    loginButtonLocator.click()

    #Check if the error message is displayed
    time.sleep(2)
    errorLocator = driver.find_element(By.ID, "error")

    assert INVALID_LOGIN_TEXT in errorLocator.text
    assert errorLocator.is_displayed()

@pytest.mark.negative
@pytest.mark.login
def test_invalid_password(driver):
    
    #Login locators
    loginLocator = driver.find_element(By.ID, "username")
    passwordLocator = driver.find_element(By.ID, "password")
    loginButtonLocator = driver.find_element(By.ID, "submit")
    
    #Enter invalid login
    loginLocator.send_keys(CORRECT_USERNAME)
    passwordLocator.send_keys(INCORRECT_PASSWORD)
    loginButtonLocator.click()

    #Check if the error message is displayed
    time.sleep(2)
    errorLocator = driver.find_element(By.ID, "error")

    assert INVALID_PASSWORD_TEXT in errorLocator.text
    assert errorLocator.is_displayed()