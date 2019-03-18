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
                #handle_excel.write_value(i,9,'test')
                #continue
                is_run = handle_excel.get_col_value(i,3)
                #是否执行
                if is_run == 'yes':
                    #拿到执行方法
                    method = handle_excel.get_col_value(i,4)
                    #拿到输入的数据
                    send_value = handle_excel.get_col_value(i,5)
                    #拿到操作元素
                    handle_value = handle_excel.get_col_value(i,6)
                    #拿到预期结果的方法
                    except_result_method = handle_excel.get_col_value(i,7)
                    #拿到预期结果值
                    except_result = handle_excel.get_col_value(i,8)
                    if except_result  != '' :
                        except_value = self.get_except_result_value(except_result)
                        if except_value[0] == 'text':
                            result = self.run_method(except_result_method)
                            if except_value[1] in result:
                                handle_excel.write_value(i,9,'pass')
                            else:
                                handle_excel.write_value(i,9,'fail')
                        elif except_value[0] == 'element' :
                            result = self.run_method(except_result_method,except_value[1])
                            
                            if result:
                                handle_excel.write_value(i,9,'pass')
                            else:
                                handle_excel.write_value(i,9,'fail')
                        else:
                            print('没有else')
                    else:
                        print('预期结果为空')
                    #开始运行啦
                    self.run_method(method,send_value,handle_value)
   
    def get_except_result_value(self,data):
        return data.split('=')


    def run_method(self,method,send_value = '', handle_value = ''):
        #getattr(object, name)是从对象object中获取名称为name的属性
        #等效与调用object.name
        method_value = getattr(self.action_method,method)

        if send_value != '' and handle_value != '':
            result = method_value(handle_value,send_value)

        elif send_value != '' and handle_value == '':
            result = method_value(send_value)

        elif send_value == '' and handle_value != '':
            result = method_value(handle_value)

        else:
            result =  method_value()
        return result
            
if __name__ == "__main__":
    test = KeywordCase()
    test.run_main()