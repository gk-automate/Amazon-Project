import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Create the Headless Option
headless_object = Options()
# Add headless arugument inside the chrome
headless_object.add_argument("--headless")
# Create a Chrome WebDriver instance
driver = webdriver.Chrome(options=headless_object)

# Navigate to the Amazon website
driver.get("http://www.amazon.com")
time.sleep(6)

try:
    All = driver.find_element(By.CLASS_NAME, "hm-icon-label")
    All.click()
    print(All.get_attribute('value'))

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="hmenu-content"]/ul[1]/li[21]/div')))

    program_features = driver.find_element(By.XPATH, '//*[@id="hmenu-content"]/ul[1]/li[21]/div')
    print(program_features.text)

except TimeoutException:
    print("TimeOut Exception: Element Not Found within given specific time")


# tabs = driver.find_elements(By.XPATH, "//a[@class='hmenu-item']")
# for tab in tabs:
#     print(tab.text)

driver.quit()

# element = (By.CSS_SELECTOR, 'hmenu-content > ul.hmenu.hmenu-visible > li:nth-child(23) > div')
# wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located(element))
# print(program_features.text)
#
# # for item in program_features:
# #     print(item.text)
#
# # Print the title of the page
# print(driver.title)

# Don't forget to close the WebDriver when you're done
# driver.quit()
