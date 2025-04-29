import time
from selenium import webdriver
from src.pages.newlogin import Loginpage
from src.pages.stockmgmtpage import AddStocks
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

        url="http://localhost:3000/stockmanagement"
        driver.get(url)
        time.sleep(10)
        addstocks = AddStocks(driver)

        WebDriverWait(driver,10).until(
            EC.url_to_be(url)
        )
        
        time.sleep(10)

        addstocks.click_add()
        time.sleep(3)

        addstocks.enter_symbol('INTUJ')
        time.sleep(5)

        addstocks.enter_companyname('Intuji Inc')
        time.sleep(5)

        addstocks.select_sector('Others')
        time.sleep(5)

        addstocks.description("Best IT Company In Nepal")
        time.sleep(3)

        addstocks.click_save()
        time.sleep(4)

        addstocks.search_stock('INTU')
        time.sleep(5)

        addstocks.click_search()
        time.sleep(10)

        driver.quit()

    except Exception as e:
        driver.save_screenshot("Add_stocks_failure.png")
        print(f"Test Login failed: {e}")
        raise

