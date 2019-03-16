#coding=utf-8
#运行所有的case的地方
import sys
sys.path.append(r"F:\\selenium_test")
from util.excel_util import ExcelUtil
from keywordselenium.actionMethod import ActionMethod

class KeywordCase:
    def run_main(self):
        self.action_method = ActionMethod()
        handle_excel = ExcelUtil(r"F:\selenium_test\config\keyword.xls")
        #拿到行数
        case_lines = handle_excel.get_lines()
        #循环行数，去执行每一行的case
        if case_lines:
            for i in range(1,case_lines):
                is_run = handle_excel.get_col_value(i,3)
                #是否执行
                if is_run == 'yes':
                    #拿到执行方法
                    method = handle_excel.get_col_value(i,4)
                    #拿到输入的数据
                    send_value = handle_excel.get_col_value(i,5)
                    #拿到操作元素
                    handle_value = handle_excel.get_col_value(i,6)
                    
                    #开始运行啦
                    self.run_method(method,send_value,handle_value)
   
    def run_method(self,method,send_value,handle_value):
        #getattr(object, name)是从对象object中获取名称为name的属性
        #等效与调用object.name
        method_value = getattr(self.action_method,method)
        
        if send_value:
            #执行方法(输入数据，元素)
            method_value(handle_value,send_value)
        elif send_value == '' and handle_value != '':
            #没有输入数据
            #执行方法(操作元素)
            method_value(handle_value)
        else:
            method_value()
            
if __name__ == "__main__":
    test = KeywordCase()
    test.run_main()