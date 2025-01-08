import requests
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from twocaptcha import TwoCaptcha
from selenium.webdriver.chrome.options import Options
import time

API_KEY="your api key"
print("key is loaded !")

solver = TwoCaptcha(API_KEY)
print("solver created")
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = uc.Chrome(options=options)

#driver=webdriver.Chrome()
print("driver is ready")
url="https://2captcha.com/demo/recaptcha-v2-callback"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(100)

captcha_elemenet=driver.find_element(By.ID,"g-recaptcha")
site_key=captcha_elemenet.get_attribute("data-sitekey")

result = solver.recaptcha(sitekey=site_key, url=driver.current_url)
print(result)

code = result['code']

text_area=driver.find_element(By.ID,"g-recaptcha-response")
if text_area:
    print("text are ais found")
driver.execute_script(f'arguments[0].innerHTML= "{code}";', text_area)

driver.execute_script(f"verifyDemoRecaptcha('{code}');")

time.sleep(8)
driver.quit() 
