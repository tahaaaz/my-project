from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time

# =========================
# LambdaTest credentials from environment variables
# =========================
USERNAME = os.environ.get('LT_USERNAME')
ACCESS_KEY = os.environ.get('LT_ACCESS_KEY')

if not USERNAME or not ACCESS_KEY:
    raise Exception("LambdaTest credentials not found in environment variables!")

# =========================
# Configure Chrome options and LambdaTest capabilities
# =========================
options = Options()
options.set_capability("platformName", "Windows 10")
options.set_capability("browserName", "Chrome")
options.set_capability("browserVersion", "114.0")
options.set_capability("LT:Options", {
    "username": USERNAME,
    "accessKey": ACCESS_KEY,
    "build": "GitHub Actions - Assessment1",
    "name": "Assessment1 Test",
    "selenium_version": "4.12.1",
    "w3c": True
})

# =========================
# Connect to LambdaTest Remote WebDriver
# =========================
driver = webdriver.Remote(
    command_executor="https://hub.lambdatest.com/wd/hub",
    options=options
)

try:
    # Maximize browser window
    driver.maximize_window()

    # Open Selenium Playground
    driver.get("https://www.lambdatest.com/selenium-playground")

    # Click Simple Form Demo
    driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()
    assert "simple-form-demo" in driver.current_url, "URL does not contain 'simple-form-demo'"

    # Enter a message and submit
    message = "Welcome to LambdaTest"
    message_input = driver.find_element(By.ID, "user-message")
    message_input.clear()
    message_input.send_keys(message)
    driver.find_element(By.ID, "showInput").click()

    # Verify output message
    output_message = driver.find_element(By.ID, "message").text
    assert output_message == message, f"Expected '{message}', got '{output_message}'"

    print("✅ Test Passed: Message displayed correctly!")
    time.sleep(2)

except Exception as e:
    print(f"❌ Test Failed: {e}")
    raise

finally:
    # Quit browser session
    driver.quit()
