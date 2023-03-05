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
        return self.table_cart().find_elements(By.CSS_SELECTOR, "tbody>tr")

    def item_name_table(self):
        rows = self.table_rows()
        title = []
        for row in rows:
            td_list = row.find_elements(By.TAG_NAME, "td")
            name = td_list[1].text
            quantity = td_list[4].text
            x = td_list[5].text.index("\n")
            price = td_list[5].text[1:x]
            title.append([name, quantity, price])
        return title

    def cartshopping(self):
        return self.driver.find_element(By.CLASS_NAME, "select")

    def edit_button(self, num: int):
        button = self.driver.find_elements(By.CSS_SELECTOR, ".edit")
        return button[num - 1].click()

    def remove_button(self, num: int):
        but = self.driver.find_elements(By.CSS_SELECTOR, ".remove")
        return but[num - 1].click()
