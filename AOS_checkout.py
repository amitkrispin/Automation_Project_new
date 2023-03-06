from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class AdvantageCheckout:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def move_to_checkout(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, "next_btn")))
        return self.driver.find_element(By.ID, "next_btn")

    def SafePayUsername(self, user: str):
        return self.driver.find_element(By.NAME, "safepay_username").send_keys(user)

    def SafePayePassword(self, password: str):
        return self.driver.find_element(By.NAME, "safepay_password").send_keys(password)

    def CreditCard(self, num: str, cvv: str, name: str, mm: str, yyyy: str):
        self.driver.find_element(By.NAME, "masterCredit").click()
        self.driver.find_element(By.ID, "creditCard").send_keys(num)
        self.driver.find_element(By.NAME, "cvv_number").send_keys(cvv)
        self.driver.find_element(By.NAME, "cardholder_name").send_keys(name)
        m = Select(self.driver.find_element(By.NAME, "mmListbox"))
        m.select_by_visible_text(mm)
        y = Select(self.driver.find_element(By.NAME, "yyyyListbox"))
        y.select_by_visible_text(yyyy)

    def Crideit_Pay_Button(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, "pay_now_btn_ManualPayment")))
        return self.driver.find_element(By.ID, "pay_now_btn_ManualPayment")

    def SafePay_Pay_Button(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, "pay_now_btn_SAFEPAY")))
        return self.driver.find_element(By.ID, "pay_now_btn_SAFEPAY")

    def New_Account_page(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, "registration_btnundefined")))
        self.driver.find_element(By.ID, "registration_btnundefined").click()

    def New_Account(self, usr: str, ema: str, pas: str, cpas: str):
        self.driver.find_element(By.NAME, "usernameRegisterPage").send_keys(usr)
        self.driver.find_element(By.NAME, "emailRegisterPage").send_keys(ema)
        self.driver.find_element(By.NAME, "passwordRegisterPage").send_keys(pas)
        self.driver.find_element(By.NAME, "confirm_passwordRegisterPage").send_keys(cpas)
        self.driver.find_element(By.NAME, "i_agree").click()
        self.driver.find_element(By.ID, "register_btnundefined").click()

    def Payment_sucssfully(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div>h2>span")))
        mas = self.driver.find_element(By.CSS_SELECTOR, "div>h2>span").text
        return mas

    def user_name(self, user: str):
        return self.driver.find_element(By.NAME, "usernameInOrderPayment").send_keys(user)

    def pass_word(self, password: str):
        return self.driver.find_element(By.NAME, "passwordInOrderPayment").send_keys(password)

    def login_button(self):
        return self.driver.find_element(By.ID, "login_btnundefined")

    def pay_now(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, "pay_now_btn_MasterCredit")))
        return self.driver.find_element(By.ID, "pay_now_btn_MasterCredit")

    def order_number(self):
        order_num = self.driver.find_element(By.ID, "orderNumberLabel")
        return order_num.text
