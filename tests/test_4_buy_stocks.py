import time
from selenium import webdriver
from src.pages.newlogin import Loginpage
from src.pages.buystockpage import StocksBuy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_buy_stock():
    try:
        driver=webdriver.Chrome()
        driver.maximize_window()


        driver.get("http://localhost:3000/login")
        loginpage=Loginpage(driver)

        loginpage.enter_email('KaushalIntujii@gmail.com')
        loginpage.enter_pw('Kaushal@123')
        loginpage.click_login()
        time.sleep(10)

        url="http://localhost:3000/buy"
        driver.get(url)
        time.sleep(20)
        buystocks = StocksBuy(driver)

        WebDriverWait(driver,10).until(
            EC.url_to_be(url)
        )
        
        time.sleep(5)

        buystocks.select_stock('AIHDF')
        time.sleep(10)

        buystocks.input(10)
        time.sleep(5)

        buystocks.buy_stock()
        time.sleep(10)

        driver.quit()

    except Exception as e:
        driver.save_screenshot("Buy_Stocks_Error.png")
        print(f"Test Login failed: {e}")
        raise

