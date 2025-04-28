import time
from selenium import webdriver
from src.pages.loginpage import Loginpage
from src.pages.stockspage import stockspage

def test_add_stock_to_watchlist():
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Navigate to login page
    driver.get("http://localhost:3000/login")
    login_page = Loginpage(driver)
    
    # Perform login
    login_page.enter_email()
    login_page.enter_pw()
    login_page.click_login()
    time.sleep(2)  # Wait for the login to complete
    
    # After login, navigate to the stocks page
    driver.get("http://localhost:3000/stocks")
    stocks_page = stockspage(driver)
    
    # Add a stock to the watchlist
    stocks_page.click_add_to_watchlist()
    time.sleep(2)  # Wait for the stock to be added

    # You can assert something to verify the stock is added, for example, check if a confirmation message appears
    # assert "Stock added to your watchlist" in driver.page_source

    driver.quit()
