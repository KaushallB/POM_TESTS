import time

from selenium import webdriver

from src.pages.loginpage import ADMpage

def test_login():

    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://admlucid.com/Identity/Account/Login")
    time.sleep(2)
    admpage=ADMpage(driver)
    admpage.select_username()
    admpage.select_password()
    admpage.select_sign_in()
    time.sleep(2)
    driver.quit()
    
    

