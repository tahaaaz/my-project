from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

USERNAME = "tahazuberi"
ACCESS_KEY = "LT_NveyivNCuwDwJJesaV324eY866GSuQ0kiQXxCQreEGTsZq0"

# Setup LambdaTest options
options = Options()
options.set_capability("platformName", "Windows 10")
options.set_capability("browserName", "Chrome")
options.set_capability("browserVersion", "114.0")
options.set_capability("LT:Options", {
    "username": USERNAME,
    "accessKey": ACCESS_KEY,
    "build": "DragSliderDemo",
    "name": "DragSliderTest",
    "selenium_version": "4.12.1",
    "w3c": True
})

# Create Remote WebDriver for LambdaTest
driver = webdriver.Remote(
    command_executor=f"https://{USERNAME}:{ACCESS_KEY}@hub.lambdatest.com/wd/hub",
    options=options
)

try:
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground")

    driver.find_element(By.LINK_TEXT, "Drag & Drop Sliders").click()

    wait = WebDriverWait(driver, 10)
    slider = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//input[@type='range' and @value='15']")
    ))

    # Move slider to 95 using JavaScript
    driver.execute_script(
        "arguments[0].value = 95; arguments[0].dispatchEvent(new Event('change'))",
        slider
    )

    # Verify the value
    current_value = slider.get_attribute("value")
    print(f"✅ Slider value is now: {current_value}")

finally:
    driver.quit()
