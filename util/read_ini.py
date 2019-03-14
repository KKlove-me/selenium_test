#coding=utf-8
import configparser

class ReadIni(object):

    #通过构造函数，使cf一来就有，file_name文件名和node节点容错处理
    def __init__(self,file_name=None,node=None):
        if file_name == None:
            file_name = "F:/selenium_test/config/LocalElement.ini"
        if node == None:
            self.node = "RegisterElement"
        else:
            self.node = node
        self.cf = self.load_ini(file_name)

    #加载ini文件
    def load_ini(self,file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf

    #获取value值
    def get_value(self,key):
        data = self.cf.get(self.node,key)
        return data












