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

        loginpage.enter_email('KaushalB@gmail.com')
        loginpage.enter_pw('Kaushal@123')
        loginpage.click_login()
        time.sleep(2)

        url="http://localhost:3000/buy"
        driver.get(url)
        buystocks = StocksBuy(driver)

        WebDriverWait(driver,5).until(
            EC.url_to_be(url)
        )


        buystocks.select_stock('AIHDF')

        buystocks.input(10)
        time.sleep(2)

        buystocks.buy_stock()
        time.sleep(3)

        driver.quit()

    except Exception as e:
        driver.save_screenshot("Buy_Stocks_Error.png")
        print(f"Test Login failed: {e}")
        raise

