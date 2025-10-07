import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class LoginTest(unittest.TestCase):

    def setUp(self):
        # Start Chrome
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_valid_login(self):
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/login")

        # Enter username
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        # Enter password
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        # Click login
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Wait a bit
        time.sleep(2)

        # Verify success message
        message = driver.find_element(By.ID, "flash").text
        self.assertIn("You logged into a secure area!", message)

    def test_invalid_login(self):
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/login")

        driver.find_element(By.ID, "username").send_keys("wronguser")
        driver.find_element(By.ID, "password").send_keys("wrongpass")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        time.sleep(2)

        message = driver.find_element(By.ID, "flash").text
        self.assertIn("Your username is invalid!", message)

    def tearDown(self):
        # Close browser after each test
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
