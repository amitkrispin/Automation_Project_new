from AOS_home_page import Home_page
from AOS_cart_page import Cart
from AOS_icons_bar import AOS_icons_bar
from AOS_sign_in_page import sign_in
from AOS_products_pages import AOS_products
from AOS_categories_pages import AOS_categories
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_chrome = Service(r"C:\Users\akris\Selenium\chromedriver.exe")
driver = webdriver.Chrome(service=service_chrome)
driver.get("https://www.advantageonlineshopping.com/#/")

home = Home_page(driver)
cart = Cart(driver)
icons = AOS_icons_bar(driver)
signin = sign_in(driver)
products = AOS_products(driver)
categories = AOS_categories(driver)

home.speakers_category().click()
categories.choose_product(2).click()
products.choose_color(1).click()
products.add_to_cart().click()
products.choose_color(2).click()
products.product_quantity_element().clear()
products.product_quantity_plus_button().click()
print(products.product_quantity_value())
print("the total price is:", products.quantity_float()*products.unit_price())
products.add_to_cart().click()
icons.cart_lil_window()
print(icons.product_name_text(1))
print(icons.product_color_text(1))
print(icons.product_price_text(1))
print(icons.quantity_text(1))
print()
print(icons.product_name_text(2))
print(icons.product_color_text(2))
print(icons.product_price_text(2))
print(icons.quantity_text(2))
sleep(5)
