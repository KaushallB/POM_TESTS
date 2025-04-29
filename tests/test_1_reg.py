import time
from selenium import webdriver
from src.pages.regpage import RegPage

def test_reg():

    try:

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://localhost:3000/register")  
        time.sleep(2)

        
        regpage = RegPage(driver)
        
        
        regpage.enter_name("Kaushal")
        regpage.enter_email("KaushalIntujii@gmail.com")
        regpage.enter_password("Kaushal@123")
        regpage.enter_confirm_password("Kaushal@123")
        regpage.click_signup()
        time.sleep(5)
        driver.get('http:localhost:8025')
        time.sleep(10)
          
       
    except Exception as e:
        driver.save_screenshot("Registration_error.png")
        print(f"Test Login failed: {e}")
        raise

    driver.quit()
