from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumpagefactory.Pagefactory import PageFactory as PF

class Google(PF):
        def __init__(self,driver):
            self.driver=driver

        locators={
                "google_click":(By.XPATH,'//*[@id="google-button"]/div/div/div/div[2]/span[1]'),
                "email_field":(By.XPATH,'//*[@id="identifierId"]'),
                "next_btn":(By.XPATH,'//*[@id="identifierNext"]/div/button/span'),
                "password":(By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input'),
                "pw_next":(By.XPATH,'//*[@id="passwordNext"]/div/button/span'),
                "continue_btn":(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div[3]/div/div/div[2]/div/div/button/span')
         }

        def clickgoogle(self):
                self.google_click.click()

        def send_email(self,email):
                self.email_field.set_text(email)

        def next_click(self):
               self.next_btn.click()

        def send_pw(self,pw):
                self.password.set_text(pw)

        def pw_next_click(self):
               self.pw_next.click()

        def continue_click(self):
                self.continue_btn.click()
