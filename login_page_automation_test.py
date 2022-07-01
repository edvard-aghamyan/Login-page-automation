from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


def try_to_login(driver, login, password):
    loginLabel = driver.find_element(by=By.NAME, value="Username")
    loginLabel.send_keys(login)
    passwordLabel = driver.find_element(by=By.NAME, value="Password")
    passwordLabel.send_keys(password)
    signButton = driver.find_element(by=By.ID, value='signin')
    signButton.click()


class AsosLoginTestCases(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.get("https://asos.com")
        hover = ActionChains(self.driver).move_to_element(
            self.driver.find_element(by=By.ID, value='myAccountDropdown')
        )
        hover.perform()
        Wait = WebDriverWait(self.driver, 10)
        Wait.until(EC.element_to_be_clickable((By.CLASS_NAME, '_1336dMe'))).click()

    def test_log_in_registered_user(self):
        try_to_login(self.driver, "test1234@gmail.com", "test1234")

    def test_log_in_with_unregistered_user(self):
        try_to_login(self.driver, "testmail12@gmail.com", "test12345")

    def test_log_in_with_empty_email(self):
        try_to_login(self.driver, "", "test1234")

    def test_log_in_with_empty_password(self):
        try_to_login(self.driver, "testmail@gmail.com", "")

    def test_log_in_with_empty_email_and_password(self):
        try_to_login(self.driver, " ", " ")

    def test_check_masked_password(self):
        try_to_login(self.driver, "", "12345678abc")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
