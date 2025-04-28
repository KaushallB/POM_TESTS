from seleniumpagefactory.Pagefactory import PageFactory as PF

class Ipo(PF):
    def __init__(self,driver):
        self.driver=driver

    locators={
        "company_name":("XPATH",'//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[2]/table/tbody/tr[1]/td[1]'),
        "apply_button":("XPATH",'//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[2]/table/tbody/tr[1]/td[7]/a/button'),
        "no_of_share":("XPATH",'//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/div/input'),
        "agree_checklist":("ID",'terms'),
        "submit_button":("XPATH",'//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div/button')

    }

    def select_name(self):
        


        