from seleniumpagefactory.Pagefactory import PageFactory as PF
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Buypage(PF):
    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    locators = {
        "stock_symbol_dropdown": ("XPATH", '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[1]/select'),  # Assuming the stock symbol input is named 'symbol'
        "quantity_input": ("XPATH", '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[3]/input'),  # Assuming the quantity input is named 'quantity'
        "buy_button": ("XPATH", '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/button'),  # Assuming the Buy button has this text
        "price_display": ("XPATH", '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[2]/input'),  # Assuming the price is shown in a div with class 'price'
    }
    
    def select_stock_symbol(self, symbol):
        dropdown = self.stock_symbol_dropdown
        select = Select(dropdown)
        select.select_by_visible_text(symbol)

    def enter_quantity(self, quantity):
        self.quantity_input.set_text(quantity)

    def click_buy_button(self):
        self.buy_button.click()

    def get_stock_price(self):
        return self.price_display.text  # Get the current stock price displayed on the page

    
