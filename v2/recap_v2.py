import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium import webdriver
from twocaptcha import TwoCaptcha
from selenium.webdriver.chrome.options import Options
import time

API_KEY="376856f5386c731f51e98830324cfda5"
print("key is loaded !")

solver = TwoCaptcha(API_KEY)
print("solver created")
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # Removes bot detection flags

driver = uc.Chrome(options=options)

#driver=webdriver.Chrome()
print("driver is ready")
driver.get("https://2captcha.com/demo/recaptcha-v2")
driver.implicitly_wait(100)
driver.maximize_window()

time.sleep(10)

site_key=driver.find_element(By.ID,"g-recaptcha").get_attribute("data-sitekey")
page_url = driver.current_url

result = solver.recaptcha(sitekey=site_key, url=page_url)
print(result)
code = result['code']

recaptcha_response_element = driver.find_element(By.NAME, 'g-recaptcha-response')
driver.execute_script(f'arguments[0].value = "{code}";', recaptcha_response_element)
time.sleep(5)
check_button = driver.find_element(By.XPATH, "//button[text()='Check']").click()
time.sleep(8)
driver.quit() 