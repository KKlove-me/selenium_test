#coding = utf-8
from handle.register_handle import RegisterHandle

#把handle的操作封装到case里面
class RegisterBusiness(object):
    def __init__(self,driver):
        self.register_h = RegisterHandle(driver)


    def user_base(self,email,name,password,code):
        self.register_h.send_user_email(email)
        self.register_h.send_user_email(name)
        self.register_h.send_user_password(password)
        self.register_h.send_user_code(code)
        self.register_h.click_register_button()
        self.register_h.get_register_text()


    def register_success(self):
        if self.register_h.get_register_text == None:
            return True
        else:
            False


    #执行操作把email,name,password,code输入进去，模拟邮箱失败的情况
    def login_email_error(self,email,name,password,code):
        self.user_base(email,name,password,code)
        #判断页面元素有没有出来，有没有错误
        if self.register_h.get_user_text('email_error',"请输入有效的电子邮件地址"):
            print("邮箱检验不成功")
            return True
        else:
            return False
    
    def login_name_error(self,email,name,password,code):
        self.user_base(email,name,password,code)
        #判断页面元素有没有出来，有没有错误
        if self.register_h.get_user_text('user_name_error',"字符长度必须大于等于4，一个中文字算2个字符"):
            print("用户名检验不成功")
            return True
        else:
            return False

    
    def login_password_error(self,email,name,password,code):
        self.user_base(email,name,password,code)
        if self.register_h.get_user_text('password_error',"最少需要输入5个字符"):
            print("密码检验不成功")
            return True
        else:
            return False

    def login_code_error(self,email,name,password,code):
        self.user_base(email,name,password,code)
        if self.register_h.get_user_text('code_text_error',"验证码错误"):
            print("验证码检验不成功")
            return True
        else:
            return False


