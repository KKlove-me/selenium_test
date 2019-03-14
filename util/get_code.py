#coding=utf-8
from PIL import Image
from ShowapiRequest import ShowapiRequest
class GetCode:
    def __init__(self,driver):
        self.driver = driver
    
    #获取图片
    def get_code_image(self,file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.driver.find_element_by_id("getcode_num")

        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width']+left
        height = code_element.size['height']+top

        im = Image.open(self,file_name)
        img = im.crop((left,top,right,height))
        img.save(file_name)

    #解析图片获取验证码
    def code_online(self,file_name):
        r = ShowapiRequest("http://route.showapi.com/184-4","88379","53a5ce673e1c464c98bd83ad3fe5276d" )
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addBodyPara("needMorePrecise", "0")
        r.addFilePara("img", file_name) #文件上传时设置
        res = r.post()
        text = res.json()['showapi_res_body']['Result']
        print(text)
        return text
