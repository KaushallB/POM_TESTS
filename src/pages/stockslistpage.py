from seleniumpagefactory.Pagefactory import PageFactory as PF
from selenium.webdriver.common.by import By

class RegPage(PF):
   
    def __init__(self, driver):
        self.driver = driver
        

    locators = {
        "name": ("NAME", "name"),
        "email": ("NAME", "email"),
        "password": ("NAME", "password"),
        "password_confirmation": ("NAME", "password_confirmation"),
        "signup_button": ("XPATH", "//button[text()='Sign Up']")
    }

    
    def enter_name(self, name):
        self.name.set_text(name)
    
    def enter_email(self, email):
        self.email.set_text(email)
    
    def enter_password(self, password):
        self.password.set_text(password)
    
    def enter_confirm_password(self, password):
        self.password_confirmation.set_text(password)

    def click_signup(self):
        self.signup_button.click()

