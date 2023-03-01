from selenium import webdriver
from selenium.webdriver.common.by import By


class AOS_products:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def colors_elements(self):
        """Method to find the colors elements"""
        return self.driver.find_elements(By.CSS_SELECTOR, "div>span#bunny")

    def choose_color(self, num: int):
        """Method to choose the color of product"""
        return self.colors_elements()[num]
