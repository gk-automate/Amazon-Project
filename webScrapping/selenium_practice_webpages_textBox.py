import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
"""import pytest

browsers = ['chrome', 'firefox', 'edge']


@pytest.mark.parametrize('browser', browsers)
def test_open(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()
    else:
        raise Exception(f"Unsupported Browser {browser}")

    try:
        driver.get("https://demoqa.com/")
    finally:
        driver.close()"""

driver = webdriver.Chrome()
driver.get("https://demoqa.com")
# Test the Entire Webelements(Through Widget) from this webpage
driver.maximize_window()
Element = driver.find_element(By.CLASS_NAME, 'card-up')
Element.click()
actual_element_page = driver.title
expected_element_page = "DEMOQA"
time.sleep(5)

print(driver.current_url)
# Compare the Actual Page and Expected Page you can use assert or if_else here
assert actual_element_page == expected_element_page, (f'Test Failed: Page Title is not as Expected. Actual:'
                                                      f' {actual_element_page}, Expected: {expected_element_page}')

text_box_clickable = driver.find_element(By.CLASS_NAME, "text")
text_box_clickable.click()

text_box_fullname = driver.find_element(By.ID, "userName")
print(text_box_fullname.get_attribute('placeholder'))

text_box_fullname.send_keys("Lalit Chandani")

email_element = driver.find_element(By.ID, "userEmail")
print(email_element.get_attribute('placeholder'))
email_element.send_keys("lalitchand@gmail.com")

Current_address_element = driver.find_element(By.ID, 'currentAddress')
current_address = "KL-2/567, Thakur Singh nagar, Rajasthan"
Current_address_element.send_keys(current_address)
print(Current_address_element.get_attribute('placeholder'))

Permanent_add_ele = driver.find_element(By.ID, 'permanentAddress')
Permanent_add_ele.send_keys(current_address)
time.sleep(5)


driver.find_element(By.ID, 'submit').click()
time.sleep(3)
driver.close()
