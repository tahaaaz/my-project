from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from concurrent.futures import ThreadPoolExecutor

# Test function for login
def login_test(thread_name):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/login")

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )

        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Wait for success message
        success_msg = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success"))
        )
        print(f"[{thread_name}] Login successful:", success_msg.text.strip())

    except Exception as e:
        print(f"[{thread_name}] Error:", e)
    finally:
        driver.quit()

# Main function to run parallel tests
def main():
    num_parallel_tests = 3  # number of parallel threads
    with ThreadPoolExecutor(max_workers=num_parallel_tests) as executor:
        for i in range(num_parallel_tests):
            executor.submit(login_test, f"Thread-{i+1}")

if __name__ == "__main__":
    main()
