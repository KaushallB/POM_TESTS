from seleniumpagefactory.Pagefactory import PageFactory as PF

class ADMpage(PF):
    def __init__(self,driver):
        self.driver=driver

    locators={
        "sign_in": ("ID", "login-submit"),
        "user_name": ("ID", "Input_Email"),
        "user_password": ("ID", "Input_Password"),
        "link_login":("XPATH", "/html/body/header/nav/ul/li/a")
    }





    def select_username(self):

        self.user_name.set_text('test2@admlucid.com')



    def select_password(self):

        self.user_password.set_text('p8FrK4pE!g.ryKs')



    def click_sign_in(self):

        self.sign_in.click()

    def click_login_link(self):
        self.link_login.click()
        