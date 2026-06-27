"""
🎯 LESSON 2: Finding Elements using XPath
Objective: Automate Google Search using XPath locators
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get("https://www.google.com")
    driver.maximize_window()
    
    # Find search box using XPath
    search_box = driver.find_element(By.XPATH, "//textarea[@name='q']")
    
    # Type text
    search_box.send_keys("Selenium Automation Mastery")
    
    # Click search button using XPath
    search_button = driver.find_element(By.XPATH, "//input[@name='btnK']")
    search_button.click()
    
    time.sleep(3)
    
    # Get the search results count
    results = driver.find_element(By.XPATH, "//div[@id='result-stats']")
    print(f"✅ Search Results: {results.text}")
    
except Exception as e:
    print(f"❌ Error: {e}")

finally:
    driver.quit()
