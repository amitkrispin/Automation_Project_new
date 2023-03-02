from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class My_orders:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.AC = ActionChains(self.driver)

    def orders_numbers(self):
        """Method to find the orders numbers element"""
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h3.roboto-regular")))
        return self.driver.find_elements(By.XPATH, "//table/tbody/tr/td[1]/label")

    def order_num(self, num: int):
        """Method to find a specific order number"""
        return self.orders_numbers()[num-1].text

    def page_name(self):
        """Method that show the page name"""
        return self.driver.find_element(By.CSS_SELECTOR, ".sticky").text


