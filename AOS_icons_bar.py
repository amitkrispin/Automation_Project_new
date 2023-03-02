from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class AOS_icons_bar:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.AC = ActionChains(self.driver)

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

    def cart_lil_window(self):
        """Method to find the cart flow window element"""
        self.AC.move_to_element(self.cart_icon()).perform()
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "table")))
        return self.driver.find_element(By.TAG_NAME, "table")

    def products_color(self):
        """Method to find the color element from the lil flow window of the cart icon"""
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "table")))
        return self.driver.find_elements(By.CSS_SELECTOR, "table>tbody>tr>td>a>label>span")

    def product_color_text(self, num: int):
        """Method that bring the color text from the lil flow window of the cart icon"""
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "table")))
        return self.products_color()[num-1].text

    def products_name(self):
        """Method that find the product name element from the lil flow window of cart icon"""
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "table")))
        return self.driver.find_elements(By.CSS_SELECTOR, "table>tbody>tr>td>a>h3")

    def product_name_text(self, num: int):
        """Method that bring the product name text from the lil flow window of the cart icon"""
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "table")))
        return self.products_name()[num-1].text

    def products_prices(self):
        """Method to find the price element from the lil flow window of the cart icon"""
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "table")))
        return self.driver.find_elements(By.CSS_SELECTOR, "table>tbody>tr>td>p")

    def product_price_text(self, num: int):
        """Method that bring the price text from the lil flow window of the cart icon"""
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "table")))
        return self.products_prices()[num - 1].text

    def product_price_float(self, num: int):
        """Method that change the price type from string to float"""
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "table")))
        price = self.products_prices()[num-1].text
        price1 = price.replace((price[0]), '').replace(',', '')
        price2 = float(price1)
        return price2

    def checkout_button(self):
        """Method of check out button from the lil flow window of the cart icon"""
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "table")))
        return self.driver.find_element(By.ID, "checkOutPopUp")

    def quantity_element(self):
        """Method that find the quantity element in the lil flow cart icon window"""
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "table")))
        return self.driver.find_elements(By.CSS_SELECTOR, "a>label.ng-binding")

    def quantity_text(self, num: int):
        """Method that find the quantity text in the lil flow cart icon window"""
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "table")))
        index = num-1
        if (index % 2) != 0:
            return self.quantity_element()[index+1].text
        else:
            return self.quantity_element()[num-1].text
