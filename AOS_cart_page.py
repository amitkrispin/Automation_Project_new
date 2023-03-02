from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Cart:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def table_cart(self):
        return self.driver.find_element(By.CLASS_NAME, "fixedTableEdgeCompatibility")

    def table_rows(self):
        return self.table_cart().find_elements(By.TAG_NAME, "tr")

    def item_name_table(self) :
        num = 1
        rows = self.table_rows()[num:]
        for row in rows:
            td_list = row.find_elements(By.TAG_NAME, "td")
            name = td_list[1].text
            quantity = td_list[4].text
            price = td_list[5].text
            return (name ,quantity ,price)
