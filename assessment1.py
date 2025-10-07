from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# LambdaTest credentials
USERNAME = "tahazuberi"
ACCESS_KEY = "LT_NveyivNCuwDwJJesaV324eY866GSuQ0kiQXxCQreEGTsZq0"

# Create Chrome Options
options = Options()

# Add LambdaTest capabilities inside options
options.set_capability("platformName", "Windows 10")
options.set_capability("browserName", "Chrome")
options.set_capability("browserVersion", "114.0")
options.set_capability("LT:Options", {
    "username": USERNAME,
    "accessKey": ACCESS_KEY,
    "build": "SimpleFormDemo",
    "name": "SimpleFormTest",
    "selenium_version": "4.12.1",
    "w3c": True
})

# Connect to LambdaTest
driver = webdriver.Remote(
    command_executor="https://hub.lambdatest.com/wd/hub",
    options=options
)

try:
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground")

    driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()
    assert "simple-form-demo" in driver.current_url, "URL does not contain 'simple-form-demo'"

    message = "Welcome to LambdaTest"
    message_input = driver.find_element(By.ID, "user-message")
    message_input.clear()
    message_input.send_keys(message)

    driver.find_element(By.ID, "showInput").click()

    output_message = driver.find_element(By.ID, "message").text
    assert output_message == message, f"Expected '{message}', got '{output_message}'"

    print("✅ Test Passed: Message displayed correctly!")
    time.sleep(3)

finally:
    driver.quit()
