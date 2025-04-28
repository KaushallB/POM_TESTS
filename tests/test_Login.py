import time

from selenium import webdriver

from src.pages.loginpage import Loginpage


def test_login():
    try:
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://localhost:3000")
        time.sleep(2)
        admpage=Loginpage(driver)
        admpage.enter_email()
        admpage.enter_pw()
        admpage.click_login()
        time.sleep(2)

    except Exception as e:
        driver.save_screenshot("Login_Error.png")
        print(f"Test Login failed: {e}")
        raise

    driver.quit()
    
    

