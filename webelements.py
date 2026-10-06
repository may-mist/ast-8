import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()

print("==================================================")
print("   PRACTICAL 8: FORM CONTROLS & ADVANCED ACTIONS   ")
print("==================================================")

driver.get("https://trytestingthis.netlify.app/")

dropdown_element = driver.find_element(By.ID, "option")
select = Select(dropdown_element)
select.select_by_value("option 2")
print("1. Selected Dropdown Option: Option 2")

radio_button = driver.find_element(By.ID, "male")
if not radio_button.is_selected():
    radio_button.click()
    print("2. Radio Button Selected: Male")

checkbox = driver.find_element(By.NAME, "option1")
if not checkbox.is_selected():
    checkbox.click()
    print("3. Checkbox Selected: Option 1")



actions = ActionChains(driver)


hover_target = driver.find_element(By.CLASS_NAME, "button")
actions.move_to_element(hover_target).perform()
print("4. Mouse Hover performed on target element.")


fname_input = driver.find_element(By.ID, "fname")
actions.click(fname_input)\
       .key_down(Keys.SHIFT)\
       .send_keys("selenium")\
       .key_up(Keys.SHIFT)\
       .perform()
print("5. Keyboard Action: Entered 'SELENIUM' using SHIFT key.")


driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
alert = driver.switch_to.alert
print("6. Alert Text Captured:", alert.text)
alert.accept()
print("   Alert Accepted Successfully.")

driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
editor = driver.find_element(By.ID, "tinymce")
print("7. Text inside IFrame:", editor.text)
driver.switch_to.default_content()  # Switch back to main DOM

driver.get("https://the-internet.herokuapp.com/windows")
main_window = driver.current_window_handle

driver.find_element(By.LINK_TEXT, "Click Here").click()
time.sleep(1)

for window_handle in driver.window_handles:
    if window_handle != main_window:
        driver.switch_to.window(window_handle)
        break

print("8. New Window Title:", driver.title)

driver.close()
driver.switch_to.window(main_window)
print("9. Switched back to Main Window Title:", driver.title)

print("==================================================")
print("         PRACTICAL COMPLETED SUCCESSFULLY!        ")
print("==================================================")

time.sleep(3)
driver.quit()