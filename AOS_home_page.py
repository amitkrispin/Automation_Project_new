from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Home_page:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def speakers_category(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, "speakersImg")))
        return self.driver.find_element(By.ID, "speakersImg")

    def tablets_category(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, "tabletsImg")))
        return self.driver.find_element(By.ID, "tabletsImg")

    def laptops_category(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, "laptopsImg")))
        return self.driver.find_element(By.ID, "laptopsImg")

    def mice_category(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, "miceImg")))
        return self.driver.find_element(By.ID, "miceImg")

    def headphones_category(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, "headphonesImg")))
        return self.driver.find_element(By.ID, "headphonesImg")

    def move_to_special_offer(self):
        sp_offer = self.wait.until(EC.visibility_of_element_located((By.ID, "see_offer_btn")))
        actions = ActionChains(self.driver)
        actions.move_to_element(sp_offer).perform()
        spic=self.driver.find_elements(By.CSS_SELECTOR,"article>h3")
        return spic[0].text
