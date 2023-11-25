# Practice site
# https://practice.expandtesting.com/login
# validate the login with the login credentials
# use pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
# Define a list of browser configuration
browsers = ['chrome', 'firefox']

# parametrize test using pytest


@pytest.mark.parametrize("browser", browsers)
def test_open_website(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise Exception(f"Unsupported browser: {browser}")

    try:
        driver.get("https://practice.expandtesting.com/login")
        # Perform actions on website using driver
    finally:
        driver.close()