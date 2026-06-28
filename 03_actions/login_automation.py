"""
🎯 LESSON 3: Login Automation & Form Filling
Objective: Automate login process on a practice website
Website: https://the-internet.herokuapp.com/login
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Navigate to the login page
    driver.get("https://the-internet.herokuapp.com/login")
    driver.maximize_window()
    print("✅ Navigated to login page")
    
    # Wait for page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    
    # Find username field and type username
    username = driver.find_element(By.ID, "username")
    username.send_keys("tomsmith")
    print("✅ Entered username: tomsmith")
    
    # Find password field and type password
    password = driver.find_element(By.ID, "password")
    password.send_keys("SuperSecretPassword!")
    print("✅ Entered password")
    
    # Find login button and click it
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    print("✅ Clicked login button")
    
    # Wait for login to complete
    time.sleep(2)
    
    # Check if login was successful
    success_message = driver.find_element(By.XPATH, "//div[@id='flash']")
    if "You logged into a secure area" in success_message.text:
        print("✅ LOGIN SUCCESSFUL! 🎉")
        print(f"   Message: {success_message.text}")
    else:
        print("❌ Login failed. Check credentials.")
    
    # Check if we're on the secure page
    if "secure" in driver.current_url:
        print("✅ Navigated to secure area")
        print(f"   Current URL: {driver.current_url}")
    
    # Take a screenshot as proof
    driver.save_screenshot("login_success.png")
    print("📸 Screenshot saved as 'login_success.png'")
    
    # Get page title
    page_title = driver.title
    print(f"📄 Page Title: {page_title}")
    
    # Wait a moment to see the result
    time.sleep(3)

except Exception as e:
    print(f"❌ Error occurred: {e}")
    driver.save_screenshot("login_error.png")
    print("📸 Error screenshot saved as 'login_error.png'")

finally:
    # Close browser
    driver.quit()
    print("🔚 Browser closed successfully")
