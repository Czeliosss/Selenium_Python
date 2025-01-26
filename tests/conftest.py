from selenium import webdriver
from testSettings import *
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture(params=["chrome", "firefox", "edge"])
def driver(request):
    # Select and create driver
    browser = request.param
    print(f"Creating {browser} driver")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise TypeError("Incorrect browser settings")

    driver.implicitly_wait(10)

    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests"
    )