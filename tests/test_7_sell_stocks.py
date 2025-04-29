import time
from selenium import webdriver
from src.pages.newlogin import Loginpage
from src.pages.holdingspage import Holdings
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_apply_ipo():
    try:
        
        driver = webdriver.Chrome()
        driver.maximize_window()

        
        driver.get("http://localhost:3000/login")
        loginpage = Loginpage(driver)
        
        loginpage.enter_email('KaushalIntujii@gmail.com')
        loginpage.enter_pw('Kaushal@123')
        loginpage.click_login()
        time.sleep(10)
        
      
        driver.get("http://localhost:3000/portfolio/holdings")
        holding = Holdings(driver)
        time.sleep(15)

        holding.click_sell()
        time.sleep(5)

        current_url=driver.current_url
        WebDriverWait(driver,10).until(
            EC.url_to_be(current_url)
        )
        time.sleep(5)

        holding.enter_qty(10)
        time.sleep(2)

        holding.final_click()
        time.sleep(15)

    
   
    except Exception as e:
        driver.save_screenshot("SellStocksFailure.png")
        print(f"Test Login failed: {e}")
        raise

    driver.quit()
