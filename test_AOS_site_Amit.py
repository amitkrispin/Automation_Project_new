from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from AOS_checkout import AdvantageCheckout
from AOS_home_page import Home_page
from AOS_cart_page import Cart
from AOS_icons_bar import AOS_icons_bar
from AOS_sign_in_page import sign_in
from AOS_products_pages import AOS_products
from AOS_categories_pages import AOS_categories
from AOS_New_Account import New_Account
from AOS_my_orders_page import My_orders
from  time import sleep


class Test_AOS_Site(TestCase):
    def setUp(self):
        self.service_chrome = Service(r"C:\Users\akris\Selenium\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service_chrome)
        self.driver.get("https://www.advantageonlineshopping.com/#/")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        self.home_page = Home_page(self.driver)
        self.categories = AOS_categories(self.driver)
        self.product = AOS_products(self.driver)
        self.icons = AOS_icons_bar(self.driver)
        self.cart = Cart(self.driver)
        self.REGISTRATION = New_Account(self.driver)
        self.check = AdvantageCheckout(self.driver)
        self.sginIn = sign_in(self.driver)
        self.orders_num_list = []
        self.orders = My_orders(self.driver)
        self.AC = ActionChains(self.driver)

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
        pro_qua = self.icons.total_items()
        self.assertEqual(pro_qua, self.icons.total_items())
        self.icons.home_by_navigation().click()

    def test_cart_window_2(self):
        self.home_page.speakers_category().click()
        self.categories.choose_product(1).click()
        self.product.product_quantity_element().click()
        self.product.product_quantity("3")
        self.product.add_to_cart().click()
        prod_1_price = self.icons.product_price_text(1)
        prod_1_qua = self.icons.quantity_text(1)
        prod_1_color = self.icons.product_color_text(1)
        self.assertIn("BOSE SOUNDLINK BLUETOOTH", self.icons.product_name_text(1))
        self.assertEqual(prod_1_price, self.icons.product_price_text(1))
        self.assertEqual(prod_1_color, self.icons.product_color_text(1))
        self.assertEqual(prod_1_qua, self.icons.quantity_text(1))
        self.icons.logo()
        self.home_page.laptops_category().click()
        self.categories.choose_product(1).click()
        self.product.product_quantity_element().click()
        self.product.product_quantity("2")
        self.product.add_to_cart().click()
        prod_2_price = self.icons.product_price_text(1)
        prod_2_qua = self.icons.quantity_text(1)
        prod_2_color = self.icons.product_color_text(1)
        self.assertIn("HP CHROMEBOOK 14", self.icons.product_name_text(1))
        self.assertEqual(prod_2_price, self.icons.product_price_text(1))
        self.assertEqual(prod_2_color, self.icons.product_color_text(1))
        self.assertEqual(prod_2_qua, self.icons.quantity_text(1))
        self.icons.logo()
        self.home_page.mice_category().click()
        self.categories.choose_product(1).click()
        self.product.product_quantity_element().click()
        self.product.product_quantity("1")
        self.product.add_to_cart().click()
        prod_3_price = self.icons.product_price_text(1)
        prod_3_qua = self.icons.quantity_text(1)
        prod_3_color = self.icons.product_color_text(1)
        self.assertIn("HP USB 3 BUTTON", self.icons.product_name_text(1))
        self.assertEqual(prod_3_price, self.icons.product_price_text(1))
        self.assertEqual(prod_3_color, self.icons.product_color_text(1))
        self.assertEqual(prod_3_qua, self.icons.quantity_text(1))
        self.icons.home_by_navigation().click()

    def test_cart_window_3(self):
        self.home_page.speakers_category().click()
        self.categories.choose_product(1).click()
        self.product.product_quantity_element().click()
        self.product.product_quantity("3")
        self.product.add_to_cart().click()
        self.icons.logo()
        self.home_page.mice_category().click()
        self.categories.choose_product(2).click()
        self.product.product_quantity_element().click()
        self.product.product_quantity("1")
        self.product.add_to_cart().click()
        self.icons.cart_lil_window()
        self.icons.remove_product(1)
        total_prod = self.icons.total_items()
        self.assertEqual(total_prod, self.icons.quantity_text(1))
        self.icons.home_by_navigation().click()

    def test_cart_page_4(self):
        self.home_page.speakers_category().click()
        self.categories.choose_product(1).click()
        self.product.product_quantity_element().click()
        self.product.product_quantity("3")
        self.product.add_to_cart().click()
        self.icons.cart_icon().click()
        self.wait.until(EC.invisibility_of_element_located(self.product.add_to_cart()))
        self.assertEqual("SHOPPING CART", self.cart.cartshopping())
        self.icons.home_by_navigation().click()

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

        self.icons.home_by_navigation().click()

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
        self.cart.edit_button(1)
        self.product.product_quantity_element().click()
        self.product.product_quantity("5")
        self.product.add_to_cart().click()
        self.cart.edit_button(2)
        self.product.product_quantity_element().click()
        self.product.product_quantity("5")
        self.product.add_to_cart().click()
        self.assertEqual("10", self.icons.total_items())
        self.icons.home_by_navigation().click()

    def test_tablets_home_7(self):
        self.home_page.tablets_category().click()
        self.categories.choose_product(3).click()
        self.product.add_to_cart()
        self.driver.back()
        self.assertEqual("TABLETS", self.categories.category_title_text())
        self.icons.logo()
        self.assertEqual("SPECIAL OFFER", self.home_page.move_to_special_offer())

    def test_checkout_8(self):
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
        self.check.New_Account("dav7894", "nono@gmail.com", "Abc123", "Abc123")
        self.check.move_to_checkout().click()
        self.check.SafePayUsername("mama123")
        self.check.SafePayePassword("Baba123")
        self.check.SafePay_Pay_Button().click()
        self.assertEqual("Thank you for buying with Advantage", self.check.Payment_sucssfully())
        self.orders_num_list.append(self.check.order_number())
        self.icons.person_icon().click()
        self.icons.my_orders_click()
        self.assertEqual(self.orders_num_list[0], self.orders.order_num(1))
        self.icons.cart_icon().click()
        self.assertEqual(self.cart.item_name_table(), [])
        self.icons.home_by_navigation().click()

    def test_checkout_9(self):
        self.home_page.tablets_category().click()
        self.categories.choose_product(3).click()
        self.product.add_to_cart().click()
        self.icons.logo()
        self.home_page.speakers_category().click()
        self.categories.choose_product(2).click()
        self.product.add_to_cart().click()
        self.icons.cart_lil_window()
        self.icons.checkout_button().click()
        self.check.user_name("Asd11")
        self.check.pass_word("Asd11")
        self.check.login_button().click()
        self.check.move_to_checkout().click()
        self.check.CreidtButton()
        self.check.pay_now().click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div>h2>span")))
        self.orders_num_list.append(self.check.order_number())
        self.icons.person_icon().click()
        self.icons.my_orders_click()
        self.assertEqual(self.orders_num_list[0], self.orders.order_num(1))
        self.icons.cart_icon().click()
        self.assertEqual(self.cart.item_name_table(), [])
        self.icons.home_by_navigation().click()

    def test_login_out_10(self):
        self.icons.person_icon().click()
        self.sginIn.username_text("Amit5")
        self.sginIn.password_text("Amit5")
        self.sginIn.signIN_button().click()
        self.assertEqual("Amit5", self.icons.user_name_value())
        self.icons.person_icon().click()
        self.icons.logout_click()
        self.assertNotIn('Amit5', self.icons.user_name_value())
