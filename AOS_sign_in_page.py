from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class sign_in:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def username_element(self):
        """Method to find the username element"""
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[class='login ng-scope']")))
        return self.driver.find_element(By.NAME, "username")

    def username_text(self, text: str):
        """Method to enter the UseName"""
        return self.username_element().send_keys(text)

    def username_value(self):
        """Method that get the attribute from the username field"""
        self.username_element().get_attribute("value")

    def password_element(self):
        """Method to find the password element"""
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[class='login ng-scope']")))
        return self.driver.find_element(By.NAME, "password")

    def password_text(self, text: str):
        """Method to enter the Password"""
        return self.password_element().send_keys(text)

    def signIN_button(self):
        """Method to find the signin button"""
        self.wait.until(EC.visibility_of_element_located((By.ID, "sign_in_btnundefined")))
        return self.driver.find_element(By.ID, "sign_in_btnundefined")

    def account_name(self):
        """Method that show the user username after login"""
        return self.driver.find_element(By.CSS_SELECTOR, "a#menuUserLink>span.hi-user").text
