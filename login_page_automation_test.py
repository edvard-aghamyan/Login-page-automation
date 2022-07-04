from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class AsosLoginTestCases(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://my.asos.com/identity/login")

    def try_to_login(self, login, password):
        loginLabel = self.driver.find_element(by=By.NAME, value="Username")
        loginLabel.send_keys(login)
        passwordLabel = self.driver.find_element(by=By.NAME, value="Password")
        passwordLabel.send_keys(password)
        signButton = self.driver.find_element(by=By.ID, value='signin')
        signButton.click()

    def test_log_in_registered_user(self):
        self.try_to_login("test1234@gmail.com", "test1234")

    def test_log_in_with_unregistered_user(self):
        self.try_to_login("testmail12@gmail.com", "test12345")

    def test_log_in_with_empty_email(self):
        self.try_to_login("", "test1234")

    def test_log_in_with_empty_password(self):
        self.try_to_login("testmail@gmail.com", "")

    def test_log_in_with_empty_email_and_password(self):
        self.try_to_login(" ", " ")

    def test_check_masked_password(self):
        self.try_to_login("", "12345678abc")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
