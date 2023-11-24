import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com")
element = driver.find_element(By.CLASS_NAME, "card-up")
time.sleep(3)
element.click()

checkBox_Element = driver.find_element(By.ID, "item-1")
time.sleep(4)
ho = driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/span/label/span[1]/svg')

if ho.is_selected():
    print("CheckBox is selected")
else:
    print("Checkbox is not Selected")
    ho.click()

result_check_box = driver.find_element(By.ID, "result")
print(result_check_box.text)
time.sleep(3)
driver.close()