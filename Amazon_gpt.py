from selenium import webdriver
import time
from selenium.webdriver.common.by import By


# Create a Chrome WebDriver instance
driver = webdriver.Chrome()

# Navigate to Amazon.com
driver.get("https://www.amazon.in/")

# Find and click the "All" menu
all_menu = driver.find_element(By.CSS_SELECTOR,"#nav-hamburger-menu > i")
all_menu.click()

# Find and click the "Programs and Features" link
programs_and_features = driver.find_element(By.LINK_TEXT,"Programs & Features")
programs_and_features.click()

# Wait for a moment to ensure the page loads
time.sleep(3)

# Find and print the list of items under "Programs & Features"
list_elements = driver.find_elements(By.CSS_SELECTOR,".hmenu-item")
for item in list_elements:
    print(item.text)

# Navigate back to the Amazon homepage
driver.get("https://www.amazon.com")

# Find and click the "Gift Cards & Mobile Recharges" link
gift_cards_mobile_recharges = driver.find_element(By.LINK_TEXT,"Gift Cards & Mobile Recharges")
gift_cards_mobile_recharges.click()

# Wait for a moment to ensure the page loads
time.sleep(4)

# Close the WebDriver
driver.quit()
