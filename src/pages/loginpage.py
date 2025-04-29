from seleniumpagefactory.Pagefactory import PageFactory as PF

class Loginpage(PF):
    def __init__(self,driver):
        self.driver=driver

    locators={
       "email":("NAME", "email"),
       "pw":("NAME","password"),
       "login":("XPATH","//button[text()='Login']")
    }

    def enter_email(self):
        self.email.set_text('KaushalInt@gmail.com')
    
    def enter_pw(self):
        self.pw.set_text('Kaushal@123')

    def click_login(self):
        self.login.click()
