import time

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")
assert driver.title == "Google"
time.sleep(5)

search_element = driver.find_element(By.ID, "APjFqb")
search_element.send_keys("amanzon.in")
search_element.send_keys(Keys.ENTER)

time.sleep(4)
amazonIn = driver.find_element(By.ID, "LC20lb MBeuO DKV0Md")
amazonIn.click()

