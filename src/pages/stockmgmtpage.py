from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumpagefactory.Pagefactory import PageFactory as PF
from selenium.webdriver.support.select import Select
import time

class AddStocks(PF):
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)

    locators={
        "add_stock_btn":(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/button'),
        "symbol":(By.NAME,'symbol'),
        "company_name":(By.NAME,'company_name'),
        "select":(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[2]/div[3]/div/form/div[3]/select'),
        "desc":(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/textarea'),
        "save":(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[2]/div[3]/div/form/div[5]/button[1]'),
        }
       
    
    def click_add(self):
        self.add_stock_btn.click()

    def enter_symbol(self,symbol):
        self.symbol.set_text(symbol)
    
    def enter_companyname(self,name):
        self.company_name.set_text(name)

    def select_sector(self,sector):
        select_element=self.select
        select = Select(select_element)
        time.sleep(5)
        select.select_by_visible_text(sector)
        
    
    def description(self,des):
        self.desc.set_text(des)

    def click_save(self):
        self.save.click()


    
