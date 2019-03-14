#coding= utf-8
from base.find_element import FindElement
    #为了handle提供元素,简言之拿元素
class RegisterPage(object):
    def __init__(self,driver):
        self.fd = FindElement(driver)
    #用FindElement中的get_element方法来调用配置文件中的信息来获取邮箱元素
    def get_email_element(self):
        return self.fd.get_element("user_email")

    #获取用户名
    def get_username_element(self):
        return self.fd.get_element("user_name")

    #获取密码
    def get_password_element(self):
        return self.fd.get_element("password")

    #获取验证码
    def get_code_element(self):
        return self.fd.get_element("code_text")

    #点击事件
    def get_button_element(self):
        return self.fd.get_element("register_button")

    def get_email_error_element(self):
        return self.fd.get_element("user_email_error")

    def get_name_error_element(self):
        return self.fd.get_element("user_name_error")

    def get_password_error_element(self):
        return self.fd.get_element("password_error")

    def get_code_error_element(self):
        return self.fd.get_element("code_text_error")