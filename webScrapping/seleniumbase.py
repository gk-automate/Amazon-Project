from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

# --------------Headless Option------Do not miss to add parameter inside the webdriver.Chrome(options=headless_object)
# Create the Headless Option by creating Object of Option class
# headless_option = Options()

# Passing the Headless parameter in argument

# headless_option.add_argument("--headless")
# Start The Driver using chrome and adding healess parameter to webdriver object
driver = webdriver.Chrome()   # options=headless_option

# Open the url
driver.get("https://seleniumbase.io/demo_page")
# Stop the script for tie given
time.sleep(3)

# ------------------------explicit wait---------------

# Explicit wait till the element displayed it doesn't stop the script
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "myButton")))

# Find the btn element to perform click action on it
butn_element = driver.find_element(By.ID, "myButton")

# Get the text the from the butn element
text_before_click = butn_element.text
print("The Placeholder Text before click is:"+text_before_click)

# Text after the click
butn_element.click()
text_after_click = butn_element.text
print("The placeholder text after the click: "+text_after_click)
# --------------End Of Button Operation----------

# --------------Paragraph text Field---------
butn_element.click()
para_text = driver.find_element(By.ID, "pText")
print("Paragraph Text:"+para_text.text)
# --------------End of paratext---

# --------------Input Slider control--------Hard To understand-

# ------For this we need actionchains instance(actionObject)
slider = driver.find_element(By.ID, "mySlider")


action = ActionChains(driver)
# Move Slider to 80%
current_value = int(slider.get_attribute("value"))
target_value = 70
slider_width = slider.size['width']
# target_position = target_value
Current_position = slider.location['x']
move_offset = (target_value - current_value) * int(slider.size['width']) / (int(slider.get_attribute("max")) - int(slider.get_attribute("min")))
# Click and Hold action perform to target value
action.click_and_hold(slider).move_by_offset(move_offset, 0).release().perform()
time.sleep(3)

# -------------Write and Practice the Custom Xpath for this try all text boxes in the page----------

# text_input_field = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[2]/td[2]/input")
# Now this the Full Xpath And make this into the custom Xpath make sure does it work

text_input_field = driver.find_element(By.XPATH, "//*[@id='myTextInput']")
text_input_field.send_keys("Hi There This Works")
# print(t)  # Returns None if above statement consider as t
# //*[@id="myTextInput"]

# textArea = driver.find_element(By.XPATH, '//*[@id="myTextarea"]')
# /html/body/form/table/tbody/tr[2]/td[4]/textarea
textArea = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[2]/td[4]/textarea")
textArea.send_keys("characterized by or indicative of pleasure, contentment, or joy")

pre_filled_text = driver.find_element(By.XPATH, '//*[@name="preText2"]')
print(pre_filled_text.text)
pre_filled_text.clear()
pre_filled_text.send_keys("Hello there its filled with text")


# -----------------Select Hover DropDown and select 1st, 2nd and 3rd dropdown simultaneously--------------------
hover_dropdown = driver.find_element(By.ID, "myDropdown")
action.move_to_element(hover_dropdown).perform()

wait_hover_element = WebDriverWait(driver, 15)
#
# options_hover_elements = driver.find_elements(By.ID, "dropOption")
# wait_hover_element.until(EC.element_to_be_clickable((By.ID, "dropOption")))


# for option in options_hover_elements:
#     option.click()
#     print("Clicked: ", option.text)

for i in range(1, 4):
    options_id = f"dropOption{i}"
    option = driver.find_element(By.ID, options_id)
    wait_hover_element.until(EC.element_to_be_clickable(option))
    option.click()
    print(f"Clicked: Link {i} selected")
    action.move_to_element(hover_dropdown).perform()
    if i == 4:
        break

# Select Dropdown

driver.quit()
