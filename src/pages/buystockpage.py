from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumpagefactory.Pagefactory import PageFactory as PF
from selenium.webdriver.support.select import Select
import time


class StocksBuy(PF):
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)

    locators={
        "Select_stock":(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[1]/select'),
        "input_qty":(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[3]/input'),
        "buy_button":(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/button'),
        }
       
    
    def select_stock(self, stock_name):
        select_element = self.Select_stock

        # Create a Select object to interact with the dropdown
        select = Select(select_element)
        time.sleep(5)
        
        # Select the option by visible text
        select.select_by_visible_text(stock_name)
        
    
    def input(self,qty):
        self.input_qty.set_text(qty)

    def buy_stock(self):
        self.buy_button.click()


    
