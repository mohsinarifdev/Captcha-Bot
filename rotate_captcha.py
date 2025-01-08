import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium import webdriver
from twocaptcha import TwoCaptcha
from selenium.webdriver.chrome.options import Options
import requests
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
url="https://2captcha.com/demo/rotatecaptcha"
driver.get(url)
driver.implicitly_wait(100)
driver.maximize_window()

time.sleep(10)
image=driver.find_element(By.CLASS_NAME,"_captchaImage_kywjg_5").find_element(By.TAG_NAME,"img")


image_response = requests.get(image.get_attribute("src"))


with open("rotate_captcha.jpg", "wb") as f:
    f.write(image_response.content)

result = solver.rotate("rotate_captcha.jpg")
print(result)
code = result['code']
code=int(code)
code=15*round(code/15)
print("after rounding this value: ",code)

right_button = driver.find_element(By.XPATH, "//button[span[contains(text(), 'Rotate right')]]")

while(1):
    right_button.click()
    style=image.get_attribute("style")
    current_angle = int(style.split("rotate(")[1].split("deg)")[0])
    print(current_angle)
    if current_angle==code:
        break



driver.find_element(By.XPATH, "//button[contains(text(), 'Check')]").click()

time.sleep(8)
driver.quit() 