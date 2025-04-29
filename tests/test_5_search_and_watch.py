import time
from selenium import webdriver
from src.pages.newlogin import Loginpage
from src.pages.stocklistpage import Addtowatchlist as AW
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add():
    try:
        driver=webdriver.Chrome()
        driver.maximize_window()

        driver.get("http://localhost:3000/login")
        login_page=Loginpage(driver)

        login_page.enter_email('KaushalIntujii@gmail.com')
        login_page.enter_pw('Kaushal@123')
        login_page.click_login()
        time.sleep(5) 

        driver.get('http://localhost:3000/stocks')
        addtowatchlist=AW(driver)
        time.sleep(15)

        addtowatchlist.search_stock('KYRXN')
        time.sleep(10)

        addtowatchlist.click_button()
        time.sleep(5)

        driver.quit()

    except Exception as e:
        driver.save_screenshot("SearchandAddError.png")
        print(f"Test Login failed: {e}")
        raise

    



