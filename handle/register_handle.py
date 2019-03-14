#coding = utf-8

from page.register_page import RegisterPage
import os
from util.get_code import GetCode
#login页面的操作流程
class RegisterHandle(object):
    def __init__(self,driver):
        self.register_p = RegisterPage(driver)
    
    #输入邮箱，调用RegisterPage下的get_xx_element的方法
    def send_user_email(self,email):
        self.register_p.get_email_element().send_keys(email)

    #输入用户名
    def send_user_name(self,username):
        self.register_p.get_username_element().send_keys(username)

    #输入密码
    def send_user_password(self,password):
        self.register_p.get_password_element().send_keys(password)

    #输入验证码
    def send_user_code(self,code):
        self.register_p.get_code_element().send_keys(code)

    #获取文字信息,get_attribute获取错误文字信息
    def get_user_text(self,info,user_info):
        if info == 'email_error':
            text = self.register_p.get_email_error_element().get_attribute('value')
        elif info == 'name_error':
            text = self.register_p.get_name_error_element().get_attribute('value')
        elif info == 'password_error':
            text = self.register_p.get_password_error_element().get_attribute('value')
        elif info == 'code_text_error':
            text = self.register_p.get_code_error_element().get_attribute('value')
        return text


    #点击注册按钮
    def click_register_button(self):
        self.register_p.get_button_element().click()


    #获取注册按钮文字
    def get_register_text(self):
        self.register_p.get_button_element