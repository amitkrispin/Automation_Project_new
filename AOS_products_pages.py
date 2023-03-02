from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AOS_products:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def colors_elements(self):
        """Method to find the colors elements"""
        self.wait.until(EC.visibility_of_element_located((By.ID, "Description")))
        return self.driver.find_elements(By.CSS_SELECTOR, "div>span#bunny")

    def choose_color(self, num: int):
        """Method to choose the color of product"""
        self.wait.until(EC.visibility_of_element_located((By.ID, "Description")))
        return self.colors_elements()[num-1]

    def product_quantity_element(self):
        """Method to find the quantity element"""
        self.wait.until(EC.visibility_of_element_located((By.ID, "Description")))
        return self.driver.find_element(By.NAME, "quantity")

    def product_quantity(self, quantity: str):
        """Method to enter amount of quantity"""
        self.wait.until(EC.visibility_of_element_located((By.ID, "Description")))
        return self.product_quantity_element().send_keys(quantity)

    def product_quantity_plus_button(self):
        """Method to find the + button element"""
        self.wait.until(EC.visibility_of_element_located((By.ID, "Description")))
        return self.driver.find_element(By.CLASS_NAME, "plus")

    def product_quantity_minus_button(self):
        """Method to find the - button element"""
        self.wait.until(EC.visibility_of_element_located((By.ID, "Description")))
        return self.driver.find_element(By.CSS_SELECTOR, ".minus")

    def product_quantity_value(self):
        """Method that get the amount of the quantity as float"""
        quantity = self.product_quantity_element().get_attribute("value")
        return quantity

    def price_element(self):
        """Method to find the price element"""
        return self.driver.find_elements(By.CSS_SELECTOR, "h2.screen768")

    def unit_price(self):
        """Method that show the unit price of a product as float"""
        price1 = self.price_element()[0].text
        price2 = price1.replace((price1[0]), '').replace(',', '')
        price3 = float(price2)
        return price3

    def quantity_float(self):
        """Method that change the type of quantity from string to float"""
        return float(self.product_quantity_value())

    def add_to_cart(self):
        """Method that find the add to cart button"""
        self.wait.until(EC.visibility_of_element_located((By.ID, "Description")))
        return self.driver.find_element(By.NAME, "save_to_cart")
