from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumpagefactory import PageFactory as PF
import time

class Addtowatchlist(PF):
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)

    
    locators={
        "search":(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[1]/div/input')   
    }

    def search_stock(self,symbol):
        self.search.set_text(symbol)

    def click_button(self):
        add_button=self.driver.find_element(By.CSS_SELECTOR,'#root > div > div.h-screen.flex.overflow-hidden > div.flex-1.flex.flex-col > div.flex-1.overflow-auto.bg-\[\#000000\].text-white > div > div.outlet-container.rounded-md.p-4.transition-colors.duration-300.bg-dark-bg.border.border-dark-bg.shadow-md.shadow-black\/30 > main > section > div.overflow-y-auto.h-90.flex-1.scrollbar-hidden.transition-opacity.duration-300 > div > div:nth-child(1) > div > svg')
        self.add_button.click()