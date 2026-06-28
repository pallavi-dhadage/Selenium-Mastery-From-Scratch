"""
🎯 LESSON 3.2: Complete Form Filling
Objective: Fill a web form with different types of inputs
Website: https://formy-project.herokuapp.com/form
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Navigate to form
    driver.get("https://formy-project.herokuapp.com/form")
    driver.maximize_window()
    print("✅ Navigated to form page")
    
    # Wait for form to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )
    
    # 1. Fill First Name
    first_name = driver.find_element(By.ID, "first-name")
    first_name.send_keys("Pallavi")
    print("✅ Entered first name")
    
    # 2. Fill Last Name
    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys("Dhadage")
    print("✅ Entered last name")
    
    # 3. Fill Job Title
    job_title = driver.find_element(By.ID, "job-title")
    job_title.send_keys("Automation Engineer")
    print("✅ Entered job title")
    
    # 4. Select Education Level (Radio button)
    education = driver.find_element(By.ID, "radio-button-2")
    education.click()
    print("✅ Selected education level")
    
    # 5. Select Gender (Checkbox)
    gender = driver.find_element(By.ID, "checkbox-2")
    gender.click()
    print("✅ Selected gender")
    
    # 6. Select Experience (Dropdown)
    experience = driver.find_element(By.ID, "select-menu")
    select = Select(experience)
    select.select_by_visible_text("2-4")
    print("✅ Selected experience level")
    
    # 7. Fill Date
    date = driver.find_element(By.ID, "datepicker")
    date.send_keys("06/28/2026")
    print("✅ Entered date")
    
    # 8. Submit the form
    submit_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Submit')]")
    submit_button.click()
    print("✅ Submitted form")
    
    # Wait for confirmation
    time.sleep(2)
    
    # Check success
    success = driver.find_element(By.XPATH, "//div[contains(@class, 'alert-success')]")
    print(f"✅ Form submitted successfully: {success.text}")
    
    # Take screenshot
    driver.save_screenshot("form_submitted.png")
    print("📸 Screenshot saved as 'form_submitted.png'")
    
    time.sleep(3)

except Exception as e:
    print(f"❌ Error: {e}")
    driver.save_screenshot("form_error.png")

finally:
    driver.quit()
    print("🔚 Browser closed")
