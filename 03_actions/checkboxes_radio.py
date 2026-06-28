"""
🎯 LESSON 3.4: Checkboxes & Radio Buttons
Objective: Handle checkboxes and radio buttons
Website: https://the-internet.herokuapp.com/checkboxes
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Checkbox page
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    driver.maximize_window()
    print("✅ Navigated to checkboxes page")
    
    # Find checkboxes
    checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    
    print(f"📊 Found {len(checkboxes)} checkboxes")
    
    # Check each checkbox
    for i, checkbox in enumerate(checkboxes, 1):
        # Check if checkbox is selected
        is_selected = checkbox.is_selected()
        print(f"   Checkbox {i}: {'✅ Selected' if is_selected else '❌ Not selected'}")
        
        # Click to toggle
        checkbox.click()
        
        # Verify toggle
        new_state = checkbox.is_selected()
        print(f"   After click: {'✅ Selected' if new_state else '❌ Not selected'}")
        print("   ---")
        time.sleep(1)
    
    # Radio button page
    driver.get("https://formy-project.herokuapp.com/radiobutton")
    time.sleep(2)
    print("\n✅ Navigated to radio buttons page")
    
    # Find and click radio buttons
    radio1 = driver.find_element(By.ID, "radio-button-1")
    radio1.click()
    print("✅ Selected Radio Button 1")
    time.sleep(1)
    
    radio2 = driver.find_element(By.ID, "radio-button-2")
    radio2.click()
    print("✅ Selected Radio Button 2")
    time.sleep(1)
    
    radio3 = driver.find_element(By.ID, "radio-button-3")
    radio3.click()
    print("✅ Selected Radio Button 3")
    time.sleep(1)
    
    # Check which is selected
    all_radios = driver.find_elements(By.XPATH, "//input[@type='radio']")
    for radio in all_radios:
        if radio.is_selected():
            print(f"📌 Selected radio: {radio.get_attribute('id')}")
    
    time.sleep(2)

except Exception as e:
    print(f"❌ Error: {e}")

finally:
    driver.quit()
    print("🔚 Browser closed")
