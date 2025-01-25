from selenium import webdriver
from testSettings import *
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def driver(request):
    # Select and open browser
    browser = request.config.getoption("--browser")
    print(f"Creating {browser} driver")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise TypeError("Incorrect browser settings")

    # Open the website
    driver.get(TARGET_URL)

    # Click on the Practice link
    practiceButtonLocator = driver.find_element(By.ID, "menu-item-20")
    practiceButtonLocator.click()

    # Select the Test Login Page
    testLoginPageLocator = driver.find_element(By.XPATH,"//*[@id='loop-container']/div/article/div[2]/div[1]/div[1]/p/a")
    testLoginPageLocator.click()

    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests"
    )