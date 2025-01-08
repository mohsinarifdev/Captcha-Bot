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
options.add_argument("--disable-blink-features=AutomationControlled")
driver = uc.Chrome(options=options)

#driver=webdriver.Chrome()
print("driver is ready")
url="https://2captcha.com/demo/recaptcha-v3-enterprise"
driver.get(url)
driver.implicitly_wait(100)
driver.maximize_window()

time.sleep(10)

# site_key=driver.find_element(By.ID,"g-recaptcha").get_attribute("data-sitekey")
# page_url = driver.current_url

result = solver.recaptcha(
        sitekey='6LfB5_IbAAAAAMCtsjEHEHKqcB9iQocwwxTiihJu',
        url='https://2captcha.com/demo/recaptcha-v3',
        version='v3',
        action='demo_action',
        score=0.9
    )

print(result)
code = result['code']

check_button = driver.find_element(By.XPATH, "//button[text()='Check']").click()
time.sleep(8)
driver.quit() 