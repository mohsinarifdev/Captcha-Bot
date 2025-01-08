from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from twocaptcha import TwoCaptcha
import time
from selenium.webdriver.chrome.service import Service

API_KEY="your api key"
print("key is loaded !")

solver = TwoCaptcha(API_KEY)
print("solver created")
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled") 

driver = Chrome(options=options)
#driver=webdriver.Chrome()
print("driver is ready")
url="https://2captcha.com/demo/recaptcha-v2-invisible"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(100)

captcha_elemenet= driver.find_element(By.ID, "g-recaptcha")
site_key=captcha_elemenet.get_attribute("data-sitekey")

result = solver.recaptcha(sitekey=site_key, url=driver.current_url,invisible=1)
print(result)

code = result['code']


text_area=driver.find_element(By.XPATH, "//textarea[@name='g-recaptcha-response']")
if text_area:
    print("text are ais found")


driver.execute_script(f'arguments[0].innerHTML= "{code}";', text_area)



time.sleep(5)
driver.execute_script(f"verifyDemoRecaptcha('{code}');")
time.sleep(8)
driver.quit()
