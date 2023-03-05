from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from AOS_home_page import Home_page
from AOS_checkout import AdvantageCheckout
from AOS_cart_page import Cart
from AOS_sign_in_page import sign_in
from time import sleep
from AOS_my_orders_page import My_orders
from selenium.webdriver.common.by import By
from AOS_icons_bar import AOS_icons_bar
from selenium.webdriver.common.action_chains import ActionChains

service_chrome = Service(r"C:\selenum1\chromedriver.exe")
driver = webdriver.Chrome(service=service_chrome)
driver.get("https://www.advantageonlineshopping.com/#/")
driver.implicitly_wait(10)
ad=sign_in(driver)
orders=My_orders(driver)
advantge = Home_page(driver)
icon=AOS_icons_bar(driver)
cart = Cart(driver)
icon.person_icon().click()
ad.username_text("12345")
ad.password_text("Orwa1234")
ad.signIN_button().click()
#icon.cart_icon().click()
#print(cart.item_name_table())
#if cart.item_name_table()==[]:
#    print("Empty")
#else:
#    print("Not Empty")
icon.person_icon().click()
icon.my_orders_click()
print(orders.order_num(0))
#print(advantge.move_to_special_offer())
#icon.cart_icon().click()
#print(cart.total_price())
#print(cart.cartshopping())
#print(cart.item_price())
#for i in cart.item_name_table():
#    print(i)
#cart.edit_button(1)
#checkout=AdvantageCheckout(driver)
#checkout.move_to_checkout().click()
#checkout.SafePayUsername().send_keys("12345")
#checkout.SafePayePassword().send_keys("Qaz12wsx")
#checkout.SafePay_Pay_Button().click()

sleep(3)
