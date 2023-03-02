from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from AOS_home_page import Home_page
from AOS_checkout import AdvantageCheckout
from AOS_cart_page import Cart
from AOS_sign_in_page import sign_in
from time import sleep
from selenium.webdriver.common.by import By
from AOS_icons_bar import AOS_icons_bar
from selenium.webdriver.common.action_chains import ActionChains

service_chrome = Service(r"C:\selenum1\chromedriver.exe")
driver = webdriver.Chrome(service=service_chrome)
driver.get("https://www.advantageonlineshopping.com/#/")
driver.implicitly_wait(10)
ad=sign_in(driver)
advantge = Home_page(driver)
icon=AOS_icons_bar(driver)
cart = Cart(driver)
icon.person_icon().click()
ad.username_element().send_keys("12345")
ad.password_element().send_keys("Orwa1234")
sleep(2)
ad.signIN_button().click()
sleep(2)
driver.find_element(By.ID, "menuCart").click()
sleep(4)
for i in cart.item_name_table():
    print(i)
cart.edit_button(1)
#checkout=AdvantageCheckout(driver)
#checkout.move_to_checkout().click()
#checkout.SafePayUsername().send_keys("12345")
#checkout.SafePayePassword().send_keys("Qaz12wsx")
#checkout.SafePay_Pay_Button().click()
sleep(2)

sleep(3)
