from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Home_page:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def user_button(self):
        return self.driver.find_element(By.ID, "menuUser")

    def username(self):
        return self.driver.find_element(By.NAME, "username")

    def password(self):
        return self.driver.find_element(By.NAME, "password")

    def signIN_button(self):
        return self.driver.find_element(By.ID, "sign_in_btnundefined")

    def speakers_category(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, "speakersImg")))
        return self.driver.find_element(By.ID, "speakersImg")

    def tablets_category(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, "tabletsImg")))
        return self.driver.find_element(By.ID, "tabletsImg")

    def laptops_category(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, "laptopsImg")))
        return self.driver.find_element(By.ID, "laptopsImg")

    def mice_category(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, "miceImg")))
        return self.driver.find_element(By.ID, "miceImg")

    def headphones_category(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, "headphonesImg")))
        return self.driver.find_element(By.ID, "headphonesImg")

    def home_page(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, By.ID, "Layer_1")))
        return self.driver.find_element(By.ID, "Layer_1")
