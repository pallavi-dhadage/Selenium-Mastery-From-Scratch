"""
🎯 LESSON 3.3: Dropdown Handling
Objective: Learn different ways to handle dropdown menus
Website: https://the-internet.herokuapp.com/dropdown
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get("https://the-internet.herokuapp.com/dropdown")
    driver.maximize_window()
    print("✅ Navigated to dropdown page")
    
    # Find the dropdown element
    dropdown_element = driver.find_element(By.ID, "dropdown")
    
    # Create a Select object
    dropdown = Select(dropdown_element)
    
    # Method 1: Select by visible text
    dropdown.select_by_visible_text("Option 1")
    print("✅ Selected Option 1 by visible text")
    time.sleep(1)
    
    # Method 2: Select by value
    dropdown.select_by_value("2")
    print("✅ Selected Option 2 by value")
    time.sleep(1)
    
    # Method 3: Select by index (starts from 0)
    dropdown.select_by_index(1)
    print("✅ Selected Option 2 by index")
    time.sleep(1)
    
    # Get all options
    all_options = dropdown.options
    print(f"📊 Total options: {len(all_options)}")
    
    # Print all options
    print("📋 All dropdown options:")
    for option in all_options:
        print(f"   - {option.text} (value: {option.get_attribute('value')})")
    
    # Get currently selected option
    selected = dropdown.first_selected_option
    print(f"✅ Currently selected: {selected.text}")
    
    time.sleep(2)

except Exception as e:
    print(f"❌ Error: {e}")

finally:
    driver.quit()
    print("🔚 Browser closed")
