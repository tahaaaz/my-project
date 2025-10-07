from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from concurrent.futures import ThreadPoolExecutor
import time

USERNAME = "tahazuberi"
ACCESS_KEY = "LT_NveyivNCuwDwJJesaV324eY866GSuQ0kiQXxCQreEGTsZq0"


browser_combos = [

    {"platformName": "Windows 10", "browserName": "Chrome", "browserVersion": "114.0", "name": "SimpleForm_WinChrome"},
    {"platformName": "macOS Catalina", "browserName": "Safari", "browserVersion": "13.1", "name": "SimpleForm_macSafari"},

    {"platformName": "Windows 10", "browserName": "Chrome", "browserVersion": "114.0", "name": "InputForm_WinChrome"},
    {"platformName": "macOS Catalina", "browserName": "Safari", "browserVersion": "13.1", "name": "InputForm_macSafari"},

    {"platformName": "Windows 10", "browserName": "Chrome", "browserVersion": "114.0", "name": "Slider_WinChrome"},
    {"platformName": "macOS Catalina", "browserName": "Safari", "browserVersion": "13.1", "name": "Slider_macSafari"}
]


def simple_form_test(cap):
    options = Options()
    options.set_capability("platformName", cap["platformName"])
    options.set_capability("browserName", cap["browserName"])
    options.set_capability("browserVersion", cap["browserVersion"])
    options.set_capability("LT:Options", {
        "username": USERNAME,
        "accessKey": ACCESS_KEY,
        "build": "Parallel_AllTests",
        "name": cap["name"],
        "selenium_version": "4.12.1",
        "w3c": True
    })

    driver = webdriver.Remote(
        command_executor=f"https://{USERNAME}:{ACCESS_KEY}@hub.lambdatest.com/wd/hub",
        options=options
    )
    wait = WebDriverWait(driver, 10)

    try:
        driver.maximize_window()
        driver.get("https://www.lambdatest.com/selenium-playground")
        driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

        message = "Welcome to LambdaTest"
        message_input = wait.until(EC.visibility_of_element_located((By.ID, "user-message")))
        message_input.clear()
        message_input.send_keys(message)

        driver.find_element(By.ID, "showInput").click()
        output_message = driver.find_element(By.ID, "message").text

        assert output_message == message
        print(f"✅ {cap['name']}: Simple Form Test Passed!")

    finally:
        driver.quit()


def input_form_test(cap):
    options = Options()
    options.set_capability("platformName", cap["platformName"])
    options.set_capability("browserName", cap["browserName"])
    options.set_capability("browserVersion", cap["browserVersion"])
    options.set_capability("LT:Options", {
        "username": USERNAME,
        "accessKey": ACCESS_KEY,
        "build": "Parallel_AllTests",
        "name": cap["name"],
        "selenium_version": "4.12.1",
        "w3c": True
    })

    driver = webdriver.Remote(
        command_executor=f"https://{USERNAME}:{ACCESS_KEY}@hub.lambdatest.com/wd/hub",
        options=options
    )
    wait = WebDriverWait(driver, 10)

    try:
        driver.maximize_window()
        driver.get("https://www.lambdatest.com/selenium-playground")
        driver.find_element(By.LINK_TEXT, "Input Form Submit").click()

        submit_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        driver.execute_script("arguments[0].scrollIntoView(true); arguments[0].click();", submit_btn)

        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#seleniumform input[name='name']"))).send_keys("Taha Zuberi")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#seleniumform input[name='email']"))).send_keys("taha@example.com")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#seleniumform input[name='password']"))).send_keys("Test@1234")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#seleniumform input[name='company']"))).send_keys("Test Company")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#seleniumform input[name='website']"))).send_keys("https://example.com")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#seleniumform input[name='city']"))).send_keys("New York")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#seleniumform input[name='address_line1']"))).send_keys("123 Test Street")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#seleniumform input[name='address_line2']"))).send_keys("Suite 456")

        country_dropdown = Select(wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#seleniumform select[name='country']"))))
        country_dropdown.select_by_visible_text("United States")

        try:
            state_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='inputState']")))
            state_field.send_keys("New York")
        except:
            pass

        try:
            zip_field = wait.until(EC.visibility_of_element_located((By.NAME, "zip")))
            zip_field.send_keys("10001")
        except:
            pass

        submit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='seleniumform']/div[6]/button")))
        driver.execute_script("arguments[0].scrollIntoView(true); arguments[0].click();", submit_btn)

        print(f"✅ {cap['name']}: Input Form Submitted!")

    finally:
        driver.quit()


def slider_test(cap):
    options = Options()
    options.set_capability("platformName", cap["platformName"])
    options.set_capability("browserName", cap["browserName"])
    options.set_capability("browserVersion", cap["browserVersion"])
    options.set_capability("LT:Options", {
        "username": USERNAME,
        "accessKey": ACCESS_KEY,
        "build": "Parallel_AllTests",
        "name": cap["name"],
        "selenium_version": "4.12.1",
        "w3c": True
    })

    driver = webdriver.Remote(
        command_executor=f"https://{USERNAME}:{ACCESS_KEY}@hub.lambdatest.com/wd/hub",
        options=options
    )
    wait = WebDriverWait(driver, 10)

    try:
        driver.maximize_window()
        driver.get("https://www.lambdatest.com/selenium-playground")
        driver.find_element(By.LINK_TEXT, "Drag & Drop Sliders").click()

        slider = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//input[@type='range' and @value='15']")
        ))

        driver.execute_script("arguments[0].value = 95; arguments[0].dispatchEvent(new Event('change'))", slider)
        current_value = slider.get_attribute("value")
        print(f"✅ {cap['name']}: Slider value = {current_value}")

    finally:
        driver.quit()

with ThreadPoolExecutor(max_workers=6) as executor:
    executor.submit(simple_form_test, browser_combos[0])
    executor.submit(simple_form_test, browser_combos[1])
    executor.submit(input_form_test, browser_combos[2])
    executor.submit(input_form_test, browser_combos[3])
    executor.submit(slider_test, browser_combos[4])
    executor.submit(slider_test, browser_combos[5])
