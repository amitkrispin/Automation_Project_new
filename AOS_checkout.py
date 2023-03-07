from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class AdvantageCheckout:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def move_to_checkout(self):
        """Method that find the next button after we press the checkout button"""
        self.wait.until(EC.visibility_of_element_located((By.ID, "next_btn")))
        return self.driver.find_element(By.ID, "next_btn")

    def SafePayUsername(self, user: str):
        """Method that entering the user safe-pay UserName"""
        return self.driver.find_element(By.NAME, "safepay_username").send_keys(user)

    def SafePayePassword(self, password: str):
        """Method that entering the user safe-pay Password"""
        return self.driver.find_element(By.NAME, "safepay_password").send_keys(password)

    def CreditCard(self, num: str, cvv: str, name: str, mm: str, yyyy: str):
        """Method that filling the fields with the user credit card information"""
        self.driver.find_element(By.NAME, "masterCredit").click()
        self.driver.find_element(By.ID, "creditCard").send_keys(num)
        self.driver.find_element(By.NAME, "cvv_number").send_keys(cvv)
        self.driver.find_element(By.NAME, "cardholder_name").send_keys(name)
        m = Select(self.driver.find_element(By.NAME, "mmListbox"))
        m.select_by_visible_text(mm)
        y = Select(self.driver.find_element(By.NAME, "yyyyListbox"))
        y.select_by_visible_text(yyyy)
    def CreidtButton(self):
        return self.driver.find_element(By.NAME, "masterCredit").click()
    def Crideit_Pay_Button(self):
        """Method to the pay now button after editing the credit card fields"""
        self.wait.until(EC.visibility_of_element_located((By.ID, "pay_now_btn_ManualPayment")))
        return self.driver.find_element(By.ID, "pay_now_btn_ManualPayment")

    def SafePay_Pay_Button(self):
        """Method to the pay now button for the safe-pay option"""
        self.wait.until(EC.visibility_of_element_located((By.ID, "pay_now_btn_SAFEPAY")))
        return self.driver.find_element(By.ID, "pay_now_btn_SAFEPAY")

    def New_Account_page(self):
        """Method to the register button if the user have no account"""
        self.wait.until(EC.visibility_of_element_located((By.ID, "registration_btnundefined")))
        self.driver.find_element(By.ID, "registration_btnundefined").click()

    def Payment_sucssfully(self):
        """Method that bring the text after the payment was successfully"""
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div>h2>span")))
        mas = self.driver.find_element(By.CSS_SELECTOR, "div>h2>span").text
        return mas

    def user_name(self, user: str):
        """Method to fill the UserName field"""
        return self.driver.find_element(By.NAME, "usernameInOrderPayment").send_keys(user)

    def pass_word(self, password: str):
        """Method to fill the Password field"""
        return self.driver.find_element(By.NAME, "passwordInOrderPayment").send_keys(password)

    def login_button(self):
        """Method of the login button after filling the account information"""
        return self.driver.find_element(By.ID, "login_btnundefined")

    def pay_now(self):
        """Method of the pay now button"""
        self.wait.until(EC.visibility_of_element_located((By.ID, "pay_now_btn_MasterCredit")))
        return self.driver.find_element(By.ID, "pay_now_btn_MasterCredit")

    def order_number(self):
        """Method that bring the order number after the payment id done"""
        order_num = self.driver.find_element(By.ID, "orderNumberLabel")
        return order_num.text

    def New_Account(self, usr: str, ema: str, pas: str, cpas: str):
        """Method that fill the fields with the information from the user and the register proces"""
        self.driver.find_element(By.NAME, "usernameRegisterPage").send_keys(usr)
        self.driver.find_element(By.NAME, "emailRegisterPage").send_keys(ema)
        self.driver.find_element(By.NAME, "passwordRegisterPage").send_keys(pas)
        self.driver.find_element(By.NAME, "confirm_passwordRegisterPage").send_keys(cpas)
        momo = ActionChains(self.driver)
        momo.move_to_element(self.driver.find_element(By.NAME, "i_agree")).click().perform()
        self.driver.find_element(By.ID, "register_btnundefined").click()
