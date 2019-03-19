#coding=utf-8
import logging
import os#以获取定位文件目录
import datetime#以获取当前时间

#封装一下下
class UserLog(object):
    def __init__(self):
        #新建logger对象，全局变量
        self.logger = logging.getLogger()
        #设置一个等级
        self.logger.setLevel(logging.DEBUG)

        #控制台输出日志
        #consle = logging.StreamHandler()#logging成为一个流对象
        #添加流
        #logger.addHandler(consle)#现在就有往控制台输出文件的一个流


        #我们需要拿到当前文件目录同级的log文件夹下面的路径
        #当前文件名字os.path.abspath(__file__)，即user_log.py
        #当前文件夹名字os.path.dirname(os.path.abspath(__file__))，即log
        base_dir = os.path.dirname(os.path.abspath(__file__))
        #拼接目录log_dir为log/logs文件夹的目录
        log_dir = os.path.join(base_dir,"logs")
        #获取当前时间，以年-月-日格式输出，并加上.log后缀，作为文件名
        log_file = datetime.datetime.now().strftime("%Y-%m-%d")+".log"
        #log_name为最终文件路径，即文件夹与文件名拼接起来
        log_name = log_dir+"/"+log_file

        #文件输出日志
        #使logging成为一个流对象，传入file_handle中
        self.file_handle = logging.FileHandler(log_name,'a',encoding='utf-8')
        #设置日志级别为info
        self.file_handle.setLevel(logging.INFO)
        #定义日志格式
        formatter = logging.Formatter('%(asctime)s %(filename)s ')
        self.file_handle.setFormatter(formatter)

        #添加流
        self.logger.addHandler(self.file_handle)
        #logging.debug("test12342")

    def get_log(self):
        return self.logger

    def close_handle(self):
        #记得要关闭
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()

if __name__ == "__main__":
    user = UserLog()
    log = user.get_log()
    log.debug('test')
    user.close_handle()
    