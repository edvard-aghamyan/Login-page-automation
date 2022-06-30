from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class AsosLoginTestCases(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_log_in_registered_user(self):
        driver = self.driver
        driver.get("https://asos.com")
        hover = ActionChains(self.driver).move_to_element(driver.find_element(by=By.ID, value='myAccountDropdown'))
        hover.perform()
        Wait = WebDriverWait(driver, 10)
        Wait.until(EC.element_to_be_clickable((By.CLASS_NAME, '_1336dMe')))
        element = driver.find_element(by=By.CLASS_NAME, value="_1336dMe")
        element.click()
        loginLabel = driver.find_element(by=By.NAME, value="Username")
        loginLabel.send_keys("test1234@gmail.com")
        passwordLabel = driver.find_element(by=By.NAME, value="Password")
        passwordLabel.send_keys("test1234")
        signButton = driver.find_element(by=By.ID, value="signin")
        signButton.click()

    def test_log_in_with_unregistered_user(self):
        driver = self.driver
        driver.get("https://asos.com")
        hover = ActionChains(self.driver).move_to_element(driver.find_element(by=By.ID, value='myAccountDropdown'))
        hover.perform()
        Wait = WebDriverWait(driver, 10)
        Wait.until(EC.element_to_be_clickable((By.CLASS_NAME, '_1336dMe')))
        element = driver.find_element(by=By.CLASS_NAME, value="_1336dMe")
        element.click()
        loginLabel = driver.find_element(by=By.NAME, value="Username")
        loginLabel.send_keys("testmail12@gmail.com")
        passwordLabel = driver.find_element(by=By.NAME, value="Password")
        passwordLabel.send_keys("test12345")
        signButton = driver.find_element(by=By.ID, value="signin")
        signButton.click()

    def test_log_in_with_empty_email(self):
        driver = self.driver
        driver.get("https://asos.com")
        hover = ActionChains(self.driver).move_to_element(driver.find_element(by=By.ID, value='myAccountDropdown'))
        hover.perform()
        Wait = WebDriverWait(driver, 10)
        Wait.until(EC.element_to_be_clickable((By.CLASS_NAME, '_1336dMe')))
        element = driver.find_element(by=By.CLASS_NAME, value="_1336dMe")
        element.click()
        passwordLabel = driver.find_element(by=By.NAME, value="Password")
        passwordLabel.send_keys("test1234")
        signButton = driver.find_element(by=By.ID, value="signin")
        signButton.click()

    def test_log_in_with_empty_password(self):
        driver = self.driver
        driver.get("https://asos.com")
        hover = ActionChains(self.driver).move_to_element(driver.find_element(by=By.ID, value='myAccountDropdown'))
        hover.perform()
        Wait = WebDriverWait(driver, 10)
        Wait.until(EC.element_to_be_clickable((By.CLASS_NAME, '_1336dMe')))
        element = driver.find_element(by=By.CLASS_NAME, value="_1336dMe")
        element.click()
        loginLabel = driver.find_element(by=By.NAME, value="Username")
        loginLabel.send_keys("testmail@gmail.com")
        signButton = driver.find_element(by=By.ID, value="signin")
        signButton.click()

    def test_log_in_with_empty_email_and_password(self):
        driver = self.driver
        driver.get("https://asos.com")
        hover = ActionChains(self.driver).move_to_element(driver.find_element(by=By.ID, value='myAccountDropdown'))
        hover.perform()
        Wait = WebDriverWait(driver, 10)
        Wait.until(EC.element_to_be_clickable((By.CLASS_NAME, '_1336dMe')))
        element = driver.find_element(by=By.CLASS_NAME, value="_1336dMe")
        element.click()
        signButton = driver.find_element(by=By.ID, value="signin")
        signButton.click()

    def test_check_masked_password(self):
        driver = self.driver
        driver.get("https://asos.com")
        hover = ActionChains(self.driver).move_to_element(driver.find_element(by=By.ID, value='myAccountDropdown'))
        hover.perform()
        Wait = WebDriverWait(driver, 10)
        Wait.until(EC.element_to_be_clickable((By.CLASS_NAME, '_1336dMe')))
        element = driver.find_element(by=By.CLASS_NAME, value="_1336dMe")
        element.click()
        passwordLabel = driver.find_element(by=By.NAME, value="Password")
        passwordLabel.send_keys("12345678abc")
        signButton = driver.find_element(by=By.ID, value="signin")
        signButton.click()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
