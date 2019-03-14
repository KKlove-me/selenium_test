#coding=utf-8
import unittest
import HTMLTestRunner
import os

class FirstCase01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("all pre")
    @classmethod
    def tearDownClass(cls):
        print("all post")

    def setUp(self):
        print('preconditions')

    def tearDown(self):
        print('postconditions')

    def testfirst01(self):
        self.assertEqual(5, 6)

    def testfirst02(self):
        self.assertEqual(5, 5)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(FirstCase01('testfirst02'))
    suite.addTest(FirstCase01('testfirst01'))

    file_path = os.path.join(os.getcwd()+"/report/"+"first_case.html")
    f = open(file_path,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='first report!!',description='第一次测试报告',verbosity=2)
    runner.run(suite)
