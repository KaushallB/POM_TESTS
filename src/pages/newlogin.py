from seleniumpagefactory.Pagefactory import PageFactory as PF

class Loginpage(PF):
    def __init__(self,driver):
        self.driver=driver

    locators={
       "email":("NAME", "email"),
       "pw":("NAME","password"),
       "login":("XPATH","//button[text()='Login']")
    }

    def enter_email(self,email):
        self.email.set_text(email)
    
    def enter_pw(self,password):
        self.pw.set_text(password)

    def click_login(self):
        self.login.click()
