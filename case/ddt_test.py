import ddt
import unittest
@ddt.ddt
class DataTest(unittest.TestCase):
    def setUp(self):
        print("start")
    def tearDown(self):
        print("end")
    @ddt.data([1,2],[3,4],[5,6])
    @ddt.unpack
    def test_case(self,a,b):
        print(a+b)
if __name__ == "__main__":
    unittest.main()