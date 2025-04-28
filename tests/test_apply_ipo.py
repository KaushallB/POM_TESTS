import time
from selenium import webdriver
from src.pages.loginpage import Loginpage
from src.pages.ipoapplypage import Ipoapply
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_apply_ipo():
    try:
        # Setup the Chrome driver
        driver = webdriver.Edge()
        driver.maximize_window()

        # Navigate to login page
        driver.get("http://localhost:3000/login")
        login_page = Loginpage(driver)
        
        # Perform login
        login_page.enter_email()
        login_page.enter_pw()
        login_page.click_login()
        time.sleep(2)  # Wait for the login to complete
        
        # After login, navigate to the buy page
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
