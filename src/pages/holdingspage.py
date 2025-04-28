from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumpagefactory.Pagefactory import PageFactory as PF
import time

class Holdings(PF):
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)

    locators={
        "sell":(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/button'),
        "qty":(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[2]/form/div[2]/input'),
        "sell_button":(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[2]/form/div[3]/button[2]')
    }

    def click_sell(self):
        self.sell.click()

    def enter_qty(self,quantity):
        self.qty.set_text(quantity)
    
    def final_click(self):
        self.sell_button.click()