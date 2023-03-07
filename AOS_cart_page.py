from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Cart:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def table_cart(self):
        """Method that find the table of the items in the cart page"""
        return self.driver.find_element(By.CLASS_NAME, "fixedTableEdgeCompatibility")

    def table_rows(self):
        """Method that find the rows from the table"""
        return self.table_cart().find_elements(By.CSS_SELECTOR, "tbody>tr")

    def item_name_table(self):
        """Method that bring the items name from the table"""
        rows = self.table_rows()
        title = []
        for row in rows:
            td_list = row.find_elements(By.TAG_NAME, "td")
            name = td_list[1].text
            quantity = td_list[4].text
            x = td_list[5].text.index("\n")
            price = td_list[5].text[1:x]
            price = price.replace(',', '')
            title.append([name, quantity, float(price)])
        return title

    def item_price(self):
        """Method that bring the items price from the table"""
        rows = self.table_rows()
        price2 = []
        for row in rows:
            td_list = row.find_elements(By.TAG_NAME, "td")
            x = td_list[5].text.index("\n")
            price = td_list[5].text[1:x]
            price = price.replace(',', '')
            price2.append(float(price))
        return price2

    def cartshopping(self):
        """Method to find cart page name"""
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "table")))
        return self.driver.find_element(By.CLASS_NAME, "select").text

    def edit_button(self, num: int):
        """Method to the edit button in the cart page"""
        wait = self.driver.find_elements(By.CSS_SELECTOR, "table[ng-show='cart.productsInCart.length > 0']")
        self.wait.until(EC.invisibility_of_element((wait[0])))
        button = self.driver.find_elements(By.CSS_SELECTOR, ".edit")
        return button[num - 1].click()

    def remove_button(self, num: int):
        """Method to the remove button in the cart page"""
        but = self.driver.find_elements(By.CSS_SELECTOR, ".remove")
        return but[num - 1].click()

    def total_price(self):
        """Method that bring the total price of the order from the cart page"""
        checkout_button = self.driver.find_element(By.ID, "checkOutButton")
        checkout_text = checkout_button.text
        price_text = checkout_text.replace("CHECKOUT ", "").replace("(", "").replace(")", "").replace("$", "").replace(",", "")
        return float(price_text)
