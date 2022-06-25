from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time


class AsosLoginTestCases(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_log_in_registered_user(self):
        driver = self.driver
        driver.get("https://asos.com")
        hover = ActionChains(self.driver).move_to_element(driver.find_element(by=By.ID, value='myAccountDropdown'))
        hover.perform()
        time.sleep(1)
        element = driver.find_element(by=By.CLASS_NAME, value="_1336dMe")
        element.click()
        time.sleep(2)
        loginLabel = driver.find_element(by=By.NAME, value="Username")
        loginLabel.send_keys("test1234@gmail.com")
        time.sleep(2)
        passwordLabel = driver.find_element(by=By.NAME, value="Password")
        passwordLabel.send_keys("test1234")
        time.sleep(2)
        signButton = driver.find_element(by=By.ID, value="signin")
        signButton.click()
        time.sleep(2)

    def test_log_in_with_unregistered_user(self):
        driver = self.driver
        driver.get("https://asos.com")
        hover = ActionChains(self.driver).move_to_element(driver.find_element(by=By.ID, value='myAccountDropdown'))
        hover.perform()
        time.sleep(1)
        element = driver.find_element(by=By.CLASS_NAME, value="_1336dMe")
        element.click()
        time.sleep(2)
        loginLabel = driver.find_element(by=By.NAME, value="Username")
        loginLabel.send_keys("testmail12@gmail.com")
        time.sleep(2)
        passwordLabel = driver.find_element(by=By.NAME, value="Password")
        passwordLabel.send_keys("test12345")
        time.sleep(2)
        signButton = driver.find_element(by=By.ID, value="signin")
        signButton.click()
        time.sleep(2)

    def test_log_in_with_empty_email(self):
        driver = self.driver
        driver.get("https://asos.com")
        hover = ActionChains(self.driver).move_to_element(driver.find_element(by=By.ID, value='myAccountDropdown'))
        hover.perform()
        time.sleep(1)
        element = driver.find_element(by=By.CLASS_NAME, value="_1336dMe")
        element.click()
        time.sleep(2)
        passwordLabel = driver.find_element(by=By.NAME, value="Password")
        passwordLabel.send_keys("test1234")
        time.sleep(2)
        signButton = driver.find_element(by=By.ID, value="signin")
        signButton.click()
        time.sleep(2)

    def test_log_in_with_empty_password(self):
        driver = self.driver
        driver.get("https://asos.com")
        hover = ActionChains(self.driver).move_to_element(driver.find_element(by=By.ID, value='myAccountDropdown'))
        hover.perform()
        time.sleep(1)
        element = driver.find_element(by=By.CLASS_NAME, value="_1336dMe")
        element.click()
        time.sleep(2)
        loginLabel = driver.find_element(by=By.NAME, value="Username")
        loginLabel.send_keys("testmail@gmail.com")
        time.sleep(2)
        signButton = driver.find_element(by=By.ID, value="signin")
        signButton.click()
        time.sleep(2)

    def test_log_in_with_empty_email_and_password(self):
        driver = self.driver
        driver.get("https://asos.com")
        hover = ActionChains(self.driver).move_to_element(driver.find_element(by=By.ID, value='myAccountDropdown'))
        hover.perform()
        time.sleep(1)
        element = driver.find_element(by=By.CLASS_NAME, value="_1336dMe")
        element.click()
        time.sleep(2)
        signButton = driver.find_element(by=By.ID, value="signin")
        signButton.click()
        time.sleep(2)

    def test_check_masked_password(self):
        driver = self.driver
        driver.get("https://asos.com")
        hover = ActionChains(self.driver).move_to_element(driver.find_element(by=By.ID, value='myAccountDropdown'))
        hover.perform()
        time.sleep(1)
        element = driver.find_element(by=By.CLASS_NAME, value="_1336dMe")
        element.click()
        time.sleep(2)
        passwordLabel = driver.find_element(by=By.NAME, value="Password")
        passwordLabel.send_keys("12345678abc")
        time.sleep(4)
        signButton = driver.find_element(by=By.ID, value="signin")
        signButton.click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
