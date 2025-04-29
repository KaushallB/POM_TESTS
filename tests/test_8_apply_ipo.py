import time
from selenium import webdriver
from src.pages.newlogin import Loginpage
from src.pages.ipoapplypage import Ipoapply
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_apply_ipo():
    try:
        
        driver = webdriver.Edge()
        driver.maximize_window()

        driver.get("http://localhost:3000/login")
        loginpage=Loginpage(driver)

        loginpage.enter_email('KaushalIntujii@gmail.com')
        loginpage.enter_pw('Kaushal@123')
        loginpage.click_login()
        time.sleep(10)

      
        driver.get("http://localhost:3000/shares")
        applypage = Ipoapply(driver)

        applypage.apply()
        time.sleep(5)

        current_url=driver.current_url
        WebDriverWait(driver,5).until(
            EC.url_to_be(current_url)
        )

        applypage.apply_kitta_input(20)
        time.sleep(2)

        applypage.tick_checkbox()
        time.sleep(2)

        applypage.submit()
        time.sleep(5)
    
   
    except Exception as e:
        driver.save_screenshot("IPO_APPLICATIOIN_ERROR.png")
        print(f"Test Login failed: {e}")
        raise

    driver.quit()
