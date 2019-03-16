#coding=utf-8
import xlrd
from xlutils.copy import copy

class ExcelUtil:
    def __init__(self,excel_path=None,index=None):
        if excel_path == None:
            excel_path = r"F:\selenium_test\config\casedata.xls"
        if index == None:
            index = 0
        #打开excel
        self.data = xlrd.open_workbook(excel_path)
        #通过索引顺序获取sheet=0
        self.table = self.data.sheets()[index]

    #table.nrows获取sheet中的有效行数
    def get_lines(self):
        rows = self.table.nrows
        if rows >= 1 :
            return rows
        return None

    def get_data(self):
        result = []
        rows = self.get_lines()
        if rows != None :
            #遍历每一行，然后打印出来
            for i in range(self.get_lines()):
                #返回由i行中所有单元格的数据组成的列表
                col = self.table.row_values(i)
                result.append(col)
            return result
        return None

    #获取单元格
    def get_col_value(self,row,col):
        if self.get_lines() > row :
            data = self.table.cell(row,col).value
            return data
        return None

    #写入数据
    def write_value(self,row,cell,value):
        #读取excel数据
        read_value = self.data
        #复制一份
        write_data = copy(read_value)
        #写入数据
        write_data.get_sheet(0).write(row,3,value)
        #保存表格
        write_data.save(r"F:\selenium_test\config\casedata.xls")

