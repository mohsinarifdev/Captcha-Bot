import requests
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from twocaptcha import TwoCaptcha
import time

API_KEY="376856f5386c731f51e98830324cfda5"
print("key is loaded !")

solver = TwoCaptcha(API_KEY)
print("solver created")

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = uc.Chrome(options=options)


#driver=webdriver.Chrome()
print("driver is ready")
url="https://2captcha.com/demo/recaptcha-v2-enterprise"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(100)

captcha_elemenet= driver.find_element(By.CSS_SELECTOR, "div.g-recaptcha")
site_key=captcha_elemenet.get_attribute("data-sitekey")

result = solver.recaptcha(sitekey=site_key, url=driver.current_url,invisible=1,enterprise=1)
print(result)

code = result['code']


text_area=driver.find_element(By.XPATH, "//textarea[@name='g-recaptcha-response']")
if text_area:
    print("text are ais found")
try:
    driver.execute_script(f'arguments[0].innerHTML= "{code}";', text_area)
except:
    print("couldnt execute script")

check_button = driver.find_element(By.XPATH, "//button[text()='Check']").click()



time.sleep(8)
driver.quit() 