from selenium import webdriver
from selenium.webdriver.common.by import By


class AOS_categories:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def category_title(self):
        """Method that find the category title"""
        return self.driver.find_element(By.CSS_SELECTOR, ".categoryTitle")

    def category_title_text(self):
        """Method that bring the category title as text"""
        return self.category_title().text

    def products(self):
        """Method to find the products elements"""
        return self.driver.find_elements(By.CSS_SELECTOR, "ul>li[class='ng-scope']>img")

    def choose_product(self, num: int):
        """Method to choose the product"""
        return self.products()[num-1]

