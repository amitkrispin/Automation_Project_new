from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AOS_icons_bar:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def person_icon(self):
        """Method to the person icon"""
        self.wait.until(EC.visibility_of_element_located((By.ID, "menuUser")))
        return self.driver.find_element(By.ID, "menuUser")

    def cart_icon(self):
        """Method to the cart icon"""
        self.wait.until(EC.visibility_of_element_located((By.ID, "menuCart")))
        return self.driver.find_element(By.ID, "menuCart")

    def logo(self):
        """Method to the logo that help to get to the home page by clicking on it"""
        self.wait.until(EC.visibility_of_element_located((By.ID, "Layer_1")))
        return self.driver.find_element(By.ID, "Layer_1")

    def search_icon(self):
        """Method to the search icon"""
        self.wait.until(EC.visibility_of_element_located((By.ID, "menuSearch")))
        return self.driver.find_element(By.ID, "menuSearch")

    def search_icon_textbox(self):
        """Method to find the search textbox element"""
        self.wait.until(EC.visibility_of_element_located((By.ID, "autoComplete")))
        return self.driver.find_element(By.ID, "autoComplete")

    def search_text(self, text: str):
        """Method to adding the text we want to search in the textbox"""
        return self.search_icon_textbox().send_keys(text)

    def logout(self):
        """Method to find the logout element"""
        self.wait.until(EC.visibility_of_element_located((By.ID, "loginMiniTitle")))
        return self.driver.find_element(By.CSS_SELECTOR, "a>div.mini-title>[translate='Sign_out']")

    def logout_click(self):
        """Method of clicking the logout button"""
        return self.logout().click()

    def my_orders(self):
        """Method that find My Orders page element"""
        self.wait.until(EC.visibility_of_element_located((By.ID, "loginMiniTitle")))
        return self.driver.find_element(By.CSS_SELECTOR, "a>div.mini-title>[translate='My_Orders']")

    def my_orders_click(self):
        """Method of clicking My Orders button"""
        return self.my_orders().click()

    def my_account(self):
        """Method that find My Account element"""
        self.wait.until(EC.visibility_of_element_located((By.ID, "loginMiniTitle")))
        return self.driver.find_element(By.CSS_SELECTOR, "a>div.mini-title>[translate='My_account']")

    def my_account_click(self):
        """Method of clicking My Account button"""
        return self.my_account().click()
