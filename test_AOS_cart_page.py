from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from AOS_checkout import AdvantageCheckout
from AOS_home_page import Home_page
from AOS_cart_page import Cart
from AOS_icons_bar import AOS_icons_bar
from AOS_sign_in_page import sign_in
from AOS_products_pages import AOS_products
from AOS_categories_pages import AOS_categories
from AOS_New_Account import New_Account
from AOS_my_orders_page import My_orders
from time import sleep


class Test_AOS_Site(TestCase):
    def setUp(self):
        self.service_chrome = Service(r"C:\selenum1\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service_chrome)
        self.driver.get("https://www.advantageonlineshopping.com/#/")
        self.driver.implicitly_wait(10)
        self.home_page = Home_page(self.driver)
        self.categories = AOS_categories(self.driver)
        self.product = AOS_products(self.driver)
        self.icons = AOS_icons_bar(self.driver)
        self.cart = Cart(self.driver)
        self.REGISTRATION = New_Account(self.driver)
        self.check = AdvantageCheckout(self.driver)
        self.sginIn = sign_in(self.driver)

    def test_cart_window_1(self):
        self.home_page.speakers_category().click()
        self.categories.choose_product(1).click()
        self.product.product_quantity_element().click()
        self.product.product_quantity("3")
        self.product.add_to_cart().click()
        self.icons.logo()
        self.home_page.laptops_category().click()
        self.categories.choose_product(1).click()
        self.product.product_quantity_element().click()
        self.product.product_quantity("2")
        self.product.add_to_cart().click()
        self.icons.cart_lil_window()
        self.assertEqual("5", self.icons.total_items())

    def test_cart_window_2(self):
        self.home_page.speakers_category().click()
        self.categories.choose_product(1).click()
        self.product.product_quantity_element().click()
        self.product.product_quantity("3")
        self.product.add_to_cart().click()
        # self.assertEqual("BOSE SOUNDLINK BLUETOOTH SPEAKER III",self.icons.product_name_text(1))
        self.assertEqual("$809.97", self.icons.product_price_text(1))
        self.assertEqual("BLACK", self.icons.product_color_text(1))
        self.assertEqual("3", self.icons.quantity_text(1))
        self.icons.logo()
        self.home_page.laptops_category().click()
        self.categories.choose_product(1).click()
        self.product.product_quantity_element().click()
        self.product.product_quantity("2")
        self.product.add_to_cart().click()
        # self.assertEqual("HP CHROMEBOOK 14 G1(ENERGY STAR)",self.icons.product_name_text(1))
        self.assertEqual("$599.98", self.icons.product_price_text(1))
        self.assertEqual("BLACK", self.icons.product_color_text(1))
        self.assertEqual("2", self.icons.quantity_text(1))
        self.icons.logo()
        self.home_page.mice_category().click()
        self.categories.choose_product(1).click()
        self.product.product_quantity_element().click()
        self.product.product_quantity("1")
        self.product.add_to_cart().click()
        # self.assertEqual("HP USB 3 BUTTON OPTICAL MOUSE",self.icons.product_name_text(1))
        self.assertEqual("$9.99", self.icons.product_price_text(1))
        self.assertEqual("BLACK", self.icons.product_color_text(1))
        self.assertEqual("1", self.icons.quantity_text(1))

    def test_cart_window_3(self):
        self.home_page.speakers_category().click()
        self.categories.choose_product(1).click()
        self.product.product_quantity_element().click()
        self.product.product_quantity("3")
        self.product.add_to_cart().click()
        self.icons.logo()
        self.home_page.mice_category().click()
        self.categories.choose_product(1).click()
        self.product.product_quantity_element().click()
        self.product.product_quantity("1")
        self.product.add_to_cart().click()
        self.icons.cart_lil_window()
        self.icons.remove_product(1)
        self.assertNotIn("BOSE SOUNDLINK BLUETOOTH SPEAKER III", self.icons.product_name_text(1))

    def test_cart_page(self):
        self.home_page.speakers_category().click()
        self.categories.choose_product(1).click()
        self.product.product_quantity_element().click()
        self.product.product_quantity("3")
        self.product.add_to_cart().click()
        self.icons.cart_icon().click()
        self.assertEqual("SHOPPING CART", self.cart.cartshopping())

    def test_cart_5(self):
        self.home_page.speakers_category().click()
        self.categories.choose_product(1).click()
        self.product.product_quantity_element().click()
        self.product.product_quantity("3")
        self.product.add_to_cart().click()
        self.icons.logo()
        self.home_page.laptops_category().click()
        self.categories.choose_product(1).click()
        self.product.product_quantity_element().click()
        self.product.product_quantity("2")
        self.product.add_to_cart().click()
        self.icons.logo()
        self.home_page.mice_category().click()
        self.categories.choose_product(1).click()
        self.product.product_quantity_element().click()
        self.product.product_quantity("1")
        self.product.add_to_cart().click()
        self.icons.cart_icon().click()
        self.assertEqual(self.cart.total_price(), sum(self.cart.item_price()))
        for i in self.cart.item_name_table():
            print(i)

    def test_cart_6(self):
        self.home_page.speakers_category().click()
        self.categories.choose_product(1).click()
        self.product.product_quantity_element().click()
        self.product.product_quantity("3")
        self.product.add_to_cart().click()
        self.icons.logo()
        self.home_page.laptops_category().click()
        self.categories.choose_product(1).click()
        self.product.product_quantity_element().click()
        self.product.product_quantity("2")
        self.product.add_to_cart().click()
        self.icons.cart_icon().click()
        self.cart.edit_button(2)
        self.product.product_quantity_element().click()
        self.product.product_quantity("5")
        self.product.add_to_cart().click()
        self.cart.edit_button(1)
        self.product.product_quantity_element().click()
        self.product.product_quantity("5")
        self.product.add_to_cart().click()
        # self.assertEqual("10", self.icons.total_items())
        sleep(2)

    def test_tablets_home(self):
        self.home_page.tablets_category().click()
        self.categories.choose_product(3).click()
        self.product.add_to_cart()
        self.driver.back()
        self.assertEqual("TABLETS", self.categories.category_title_text())
        self.icons.logo()
        self.assertEqual("SPECIAL OFFER", self.home_page.move_to_special_offer())

    def test_checkout_1(self):
        self.home_page.tablets_category().click()
        self.categories.choose_product(3).click()
        self.product.add_to_cart().click()
        self.icons.logo()
        self.home_page.speakers_category().click()
        self.categories.choose_product(2).click()
        self.product.add_to_cart().click()
        self.icons.cart_icon().click()
        self.icons.cart_lil_window()
        self.icons.checkout_button().click()
        self.check.New_Account_page()
        self.check.New_Account("1234567", "nono@gmail.com", "Abc123", "Abc123")
        self.check.move_to_checkout().click()
        self.check.SafePayUsername("mama123")
        self.check.SafePayePassword("Baba123")
        self.check.SafePay_Pay_Button().click()
        self.assertEqual("Thank you for buying with Advantage", self.check.Payment_sucssfully())
        self.icons.cart_icon().click()
        self.assertEqual(self.cart.item_name_table(), [])
        sleep(10)

    def test_checkout_2(self):
        self.home_page.tablets_category().click()
        self.categories.choose_product(3).click()
        self.product.add_to_cart().click()
        self.icons.logo()
        self.home_page.speakers_category().click()
        self.categories.choose_product(2).click()
        self.product.add_to_cart().click()
        self.icons.cart_lil_window()
        self.icons.checkout_button().click()
        self.check.user_name("1234567")
        self.check.pass_word("Abc123")
        self.check.login_button().click()
        self.check.move_to_checkout().click()
        self.check.CreditCard("123456789012", "123", "abc", "12", "2027")
        self.check.Crideit_Pay_Button().click()
        self.icons.cart_icon().click()
        self.assertEqual(self.cart.item_name_table(), [])
        sleep(7)

    def test_login_out(self):
        self.icons.person_icon().click()
        self.sginIn.username_text("12345")
        self.sginIn.password_text("Orwa1234")
        self.sginIn.signIN_button().click()
        self.icons.person_icon().click()
        self.icons.logout_click()
