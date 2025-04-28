from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory as PF

class Ipoapply(PF):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Locators
    locators={
        "apply_button":(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[2]/table/tbody/tr[2]/td[7]/a'),   #need to replace this by inspecting and copying xpath of the a tag
        "kitta_input" :(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/div/input'),
        "checkbox":(By.XPATH,'//*[@id="terms"]'),
        "submitbutton":(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div/button')
        }

    def apply(self):
        self.apply_button.click()
        
    def apply_kitta_input(self,qty):
        self.kitta_input.set_text(qty)
    
    def tick_checkbox(self):
        self.checkbox.click()

    def submit(self):
        self.submitbutton.click()
