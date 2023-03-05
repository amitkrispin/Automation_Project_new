from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class New_Account:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def New_Account(self, usr: str, ema: str, pas: str, cpas: str):
        self.driver.find_element(By.NAME, "usernameRegisterPage").send_keys(usr)
        self.driver.find_element(By.NAME, "emailRegisterPage").send_keys(ema)
        self.driver.find_element(By.NAME, "passwordRegisterPage").send_keys(pas)
        self.driver.find_element(By.NAME, "confirm_passwordRegisterPage").send_keys(cpas)
        momo = ActionChains(self.driver)
        momo.move_to_element(self.driver.find_element(By.NAME, "i_agree")).click().perform()
        self.driver.find_element(By.ID, "register_btnundefined").click()
