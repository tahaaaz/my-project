import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_valid_login(self):
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/login")

        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Wait and handle alert quickly
        try:
            WebDriverWait(driver, 10).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            
            print("Alert text:", alert.text)
            alert.accept()  # Click OK
        except:
            print("No alert appeared or it closed too fast.")

        # Now verify success message
        message = driver.find_element(By.ID, "flash").text
        self.assertIn("You logged into a secure area!", message)

    def test_invalid_login(self):
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/login")

        driver.find_element(By.ID, "username").send_keys("wronguser")
        driver.find_element(By.ID, "password").send_keys("wrongpass")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        message = driver.find_element(By.ID, "flash").text
        self.assertIn("Your username is invalid!", message)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
