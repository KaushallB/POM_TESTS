import time
import pickle
from selenium import webdriver


from src.pages.newlogin import Loginpage
from src.pages.ipoapplypage import Ipoapply

def test_login():
    try:
        driver=webdriver.Chrome()
        driver.get("http://localhost:3000")
        driver.maximize_window()
        time.sleep(2)
        login=Loginpage(driver)
       
        login.enter_email('KaushalIntujii@gmail.com')
        time.sleep(5)

        login.enter_pw('Kaushal@123')
        time.sleep(5)

        login.click_login()
        time.sleep(10)

        cookies=driver.get_cookies()
        with open("cookies.pkl", "wb")as file:
            pickle.dump(cookies,file)

        time.sleep(5)

    except Exception as e:
        driver.save_screenshot("Login_Error.png")
        print(f"Test Login failed: {e}")
        raise

    driver.quit()


"""
def test_load_cookie():
    try:
        driver=webdriver.Chrome()
        driver.get("http://localhost:3000")
        time.sleep(2)
        login=Loginpage(driver)
       
        with open("cookies.pkl", "rb") as file:
            cookies=pickle.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)
        print(cookie)
        
        #To apply cookie
        driver.refresh()
        

        login.click_login()

        cookies=driver.get_cookies()
        with open("cookies.pkl", "wb")as file:
            pickle.dump(cookies,file)

        time.sleep(5)

        applypage = Ipoapply(driver)

        applypage.apply()



    except Exception as e:
        driver.save_screenshot("Login_Error.png")
        print(f"Test Login failed: {e}")
        raise

    driver.quit()


"""
    


    
    

