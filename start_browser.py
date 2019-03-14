import time
import pytesseract
from PIL import Image
from selenium import webdriver
from ShowapiRequest import ShowapiRequest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver =webdriver.Chrome()
driver.get("http://www.5itest.cn/register")
driver.maximize_window()
time.sleep(5)


print(expected_conditions.title_contains("注册"))

email_element = driver.find_element_by_id("register_email")
driver.save_screenshot("E:/memeda.png")

code_element = driver.find_element_by_id("getcode_num")
print(code_element.location)

left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width']+left
height = code_element.size['height']+top

im = Image.open("E://1.png")
img = im.crop((left,top,right,height))
img.save("E://miaomiao.png")

r = ShowapiRequest("http://route.showapi.com/184-4","88379","53a5ce673e1c464c98bd83ad3fe5276d" )
r.addBodyPara("typeId", "34")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
r.addFilePara("img", r"E://miaomiao.png") #文件上传时设置
res = r.post()
text = res.json()['showapi_res_body']['Result']

print(text)
time.sleep(2)
driver.find_element_by_id('captcha_code').send_keys(text)