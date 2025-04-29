import time
from selenium import webdriver
from src.pages.googlesigninpage import Google
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_google():
    try:

        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get('http://localhost:3000/login')
        google_page=Google(driver)

        original_window = driver.current_window_handle 

        google_page.clickgoogle()
        time.sleep(5)

        all_windows = driver.window_handles
        for handle in all_windows:
            if handle != original_window:
                driver.switch_to.window(handle)
                break
        
        print("Switched to Google Sign-In window.")


        google_page.send_email('021bim013@sxc.edu.np')
        time.sleep(3)

        google_page.next_click()
        time.sleep(3)

        google_page.send_pw('Sefutbol@11s')
        time.sleep(3)

        google_page.pw_next_click()
        time.sleep(3)

        google_page.continue_click()
        time.sleep(10)

    except Exception as e:
        driver.save_screenshot("Google_login_error.png")
        print(f"Test Login failed: {e}")
        raise

    driver.quit()

