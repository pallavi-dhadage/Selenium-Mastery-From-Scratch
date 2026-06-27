"""
🎯 LESSON 1: Your First Selenium Script
Objective: Open a browser, navigate to a website, and get the title
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Using webdriver-manager - no need to download chromedriver manually!
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Navigate to Google
    driver.get("https://www.google.com")
    driver.maximize_window()
    
    # Get and print the title
    title = driver.title
    print(f"✅ Page Title: {title}")
    
    # Verify we're on the right page
    if "Google" in title:
        print("✅ Successfully navigated to Google!")
    else:
        print("❌ Something went wrong!")
    
    # Wait 3 seconds so you can see the result
    time.sleep(3)

finally:
    # Always quit the driver
    driver.quit()
    print("🔚 Browser closed successfully")
