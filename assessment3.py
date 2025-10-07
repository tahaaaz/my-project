from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


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
    "build": "FullForm-sub",
    "name": "Fullformsub",
    "selenium_version": "4.12.1",
    "w3c": True
})

# Create Remote WebDriver for LambdaTest
driver = webdriver.Remote(
    command_executor=f"https://{USERNAME}:{ACCESS_KEY}@hub.lambdatest.com/wd/hub",
    options=options
)



# Setup Chrome driver
#service = Service()
#driver = webdriver.Chrome(service=service)
#driver.maximize_window()

# WebDriverWait object (10s timeout)
wait = WebDriverWait(driver, 10)

try:
    # Step 1: Open page
    driver.get("https://www.lambdatest.com/selenium-playground")

    # Click "Input Form Submit"
    input_form_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Input Form Submit")))
    input_form_link.click()

    # Step 2: Trigger Submit without filling (use JS click)
    submit_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
    driver.execute_script("arguments[0].click();", submit_btn)  # JS click

    # Step 3: Assert validation message
    name_field = wait.until(EC.presence_of_element_located((By.NAME, "name")))
    assert name_field.get_attribute("required") is not None
    print("✅ Validation triggered: Required field is enforced.")

    # Step 4: Fill the form
    form = wait.until(EC.presence_of_element_located((By.ID, "seleniumform")))

    # Standard fields
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#seleniumform input[name='name']"))).send_keys("Taha Zuberi")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#seleniumform input[name='email']"))).send_keys("taha@example.com")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#seleniumform input[name='password']"))).send_keys("Test@1234")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#seleniumform input[name='company']"))).send_keys("Test Company")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#seleniumform input[name='website']"))).send_keys("https://example.com")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#seleniumform input[name='city']"))).send_keys("New York")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#seleniumform input[name='address_line1']"))).send_keys("123 Test Street")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#seleniumform input[name='address_line2']"))).send_keys("Suite 456")

    # Country dropdown
    country_dropdown = Select(wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#seleniumform select[name='country']"))))
    country_dropdown.select_by_visible_text("United States")

    # Dynamically fill State and Zip if present
    # State (dropdown)
    try:
        state_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='inputState']")   ))
        state_dropdown.send_keys("New York")
        print("✅ State selected")
    except:
          print("⚠️ State field not found, skipping")


# Zip
    try:
        zip_field = wait.until(EC.visibility_of_element_located((By.NAME, "zip")))
        zip_field.send_keys("10001")
        print("✅ Zip filled")
    except:
        print("⚠️ Zip field not found, skipping")

# Submit using JS click
    submit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='seleniumform']/div[6]/button")))
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
    time.sleep(1)  # optional
    driver.execute_script("arguments[0].click();", submit_btn)


finally:
    time.sleep(3)  # see results before closing
    driver.quit()
