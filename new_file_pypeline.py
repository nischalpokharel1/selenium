from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# Use headless Chrome for CI pipelines
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    # Open the login page
    driver.get("https://the-internet.herokuapp.com/login")

    # Find and fill username
    username = driver.find_element(By.ID, "username")
    username.send_keys("tomsmith")

    # Find and fill password
    password = driver.find_element(By.ID, "password")
    password.send_keys("SuperSecretPassword!")

    # Submit the form
    login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
    login_button.click()

    time.sleep(2)  # optional, for demonstration

    # Check if login was successful
    success_message = driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in success_message
    print("✅ Login successful - test passed.")

except Exception as e:
    print("❌ Login test failed:", str(e))

finally:
    driver.quit()
