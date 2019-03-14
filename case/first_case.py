#coding=utf-8
import sys
sys.path.append('F:/selenium_test')
from business.register_business import RegisterBusiness
from selenium import webdriver
import HTMLTestRunner
import unittest
import os
#测试用例、数据》》业务层
class FirstCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register")
        self.login = RegisterBusiness(self.driver)
    def tearDown(self):
        self.driver.close()

    def test_login_email_error(self):
        email_error = self.login.login_email_error('35','123','123456','2365')
        if email_error == True:
            print('注册成功了，此条case执行失败')

    def test_login_name_error(self):
        code_error = self.login.login_code_error('asxder@c.com','asxder','1234567','888')
        if code_error == True:
            print('注册成功了，此条case执行失败')

    def test_login_password_error(self):
        password_error = self.login.login_password_error('asxder@c.com','asxder','1234567','888')
        if password_error == True:
            print('注册成功了，此条case执行失败')

    def test_login_code_error(self):
        code_error = self.login.login_code_error('asxder@c.com','asxder','1234567','888')
        if code_error == True:
            print('注册成功了，此条case执行失败')

    def test_login_success(self):
        self.login.user_base('asxder@c.com','asxder','1234567','888')
        if self.login.register_success() == True:
            print("注册成功！")

if __name__ == "__main__":
    unittest.main()
    file_path = os.path.join(os.getcwd()+"/report/"+"first_case.html")
    f = open(file_path,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='first report!!',description='第一次测试报告',verbosity=2)
    runner.run()


