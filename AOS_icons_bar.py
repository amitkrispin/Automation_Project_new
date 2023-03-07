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
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "PopUp")))
        return self.driver.find_element(By.ID, "menuUser")

    def cart_icon(self):
        """Method to the cart icon"""
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "PopUp")))
        return self.driver.find_element(By.ID, "menuCart")

    def logo(self):
        """Method to the logo that help to get to the home page by clicking on it"""
        return self.driver.find_element(By.ID, "Layer_1").click()

    def search_icon(self):
        """Method to the search icon"""
        self.wait.until(EC.visibility_of_element_located((By.ID, "our_products")))
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
        """Method to find the cart popup window element"""
        self.AC.move_to_element(self.cart_icon()).perform()
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "table")))
        return self.driver.find_element(By.TAG_NAME, "table")

    def products_color(self):
        """Method to find the color element from the popup window of the cart icon"""
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "table")))
        return self.driver.find_elements(By.CSS_SELECTOR, "table>tbody>tr>td>a>label>span")

    def product_color_text(self, num: int):
        """Method that bring the color name from the popup window of the cart icon"""
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "table")))
        return self.products_color()[num - 1].text

    def products_name(self):
        """Method that find the product name element from the popup window of cart icon"""
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "table")))
        return self.driver.find_elements(By.CSS_SELECTOR, "table>tbody>tr>td>a>h3")

    def product_name_text(self, num: int):
        """Method that bring the product name from the popup window of the cart icon"""
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "table")))
        return self.products_name()[num - 1].text

    def products_prices(self):
        """Method that find the price element from the popup window of the cart icon"""
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "table")))
        return self.driver.find_elements(By.CSS_SELECTOR, "table>tbody>tr>td>p")

    def product_price_text(self, num: int):
        """Method that bring the price text of a product from the popup window of the cart icon"""
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "table")))
        return self.products_prices()[num - 1].text

    def product_price_float(self, num: int):
        """Method that change the price type from string to float"""
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "table")))
        price = self.products_prices()[num - 1].text
        price1 = price.replace((price[0]), '').replace(',', '')
        price2 = float(price1)
        return price2

    def checkout_button(self):
        """Method of the checkout button from the popup window of the cart icon"""
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "table")))
        return self.driver.find_element(By.ID, "checkOutPopUp")

    def quantity_element(self):
        """Method that find the quantity element in the popup cart icon window"""
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "table")))
        return self.driver.find_elements(By.CSS_SELECTOR, "a>label.ng-binding")

    def quantity_text(self, num: int):
        """Method that return the quantity number of a product from the popup cart icon window"""
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "table")))
        index = num - 1
        if (index % 2) != 0:
            QUA = self.quantity_element()[index + 1].text.replace("QTY: ", "")
            return QUA
        else:
            QUA1 = self.quantity_element()[num - 1].text.replace("QTY: ", "")
            return QUA1

    def remove_product(self, num: int):
        """Method of removing product from cart icon popup window"""
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "table")))
        eh = self.driver.find_elements(By.CSS_SELECTOR, ".removeProduct")
        return eh[num].click()

    def total_items(self):
        """Method that bring the number of the total items in the cart from the popup window of the cart icon"""
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "table")))
        el = self.driver.find_elements(By.CSS_SELECTOR, "tfoot>tr>td>span>label")
        total_items_text = el[0].text
        total_items = total_items_text.replace("(", "").replace(" Item)", "")
        return total_items

    def home_by_navigation(self):
        """Method that find the element of the home page from the navigation bar"""
        return self.driver.find_element(By.XPATH, "//nav/a[1]")
    def user_name_value(self):
        """"Method that returns the value of the username"""
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "PopUp")))
        us=self.driver.find_elements(By.CSS_SELECTOR,"ul>li>a>span")
        return us[3].text

