#Import selenium
from selenium import webdriver
from testSettings import *
import time
from selenium.webdriver.common.by import By

#Open browser
driver = webdriver.Chrome()

#Open the website

driver.get(TARGET_URL)
time.sleep(1)

#Click on the Practice link
practiceButtonLocator = driver.find_element(By.ID, "menu-item-20")
practiceButtonLocator.click()
time.sleep(1)

#Select the Test Login Page
testLoginPageLocator = driver.find_element(By.XPATH, "//*[@id='loop-container']/div/article/div[2]/div[1]/div[1]/p/a")
testLoginPageLocator.click()
time.sleep(2)

#Login & password locators
loginLocator = driver.find_element(By.ID, "username")
passwordLocator = driver.find_element(By.ID, "password")
loginButtonLocator = driver.find_element(By.ID, "submit")

#Enter login & password
loginLocator.send_keys(CORRECT_USERNAME)
passwordLocator.send_keys(CORRECT_PASSWORD)
time.sleep(1)
loginButtonLocator.click()

#Check if the login was successful
textLocator = driver.find_element(By.TAG_NAME, "h1")
logoutLocator = driver.find_element(By.LINK_TEXT, "Log out")

assert SUCESSFUL_URL_PART in driver.current_url 

assert textLocator.text == SUCCESSFUL_TEXT

assert logoutLocator.is_displayed()


time.sleep(5)
