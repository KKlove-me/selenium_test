#coding=utf-8
import unittest
import os
class RunCase(unittest.TestCase):
    def test_case01(self):
        case_path = os.path.join(os.getcwd(),'case')
        suite = unittest.defaultTestLoader.discover(case_path,'unittest_*.py')
        unittest.TextTestRunner().run(suite)
        #discover(start_dir,pattern='test*.py',top_level_dir=None)
        #从指定的start_dir（起始目录）递归查找所有子目录下的测试模块并返回一个TestSuite对象
        #只有符合pattern模式匹配的测试文件才会被加载

if __name__ == "__main__":
    unittest.main()