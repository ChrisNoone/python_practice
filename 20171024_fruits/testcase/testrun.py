# coding:utf-8
import unittest
from time import sleep
from src.common import initdriver
from src.functions import firstPage
from src.functions import secondPage

class fruitstest(unittest.TestCase):
    def setUp(self):
        self.driver = initdriver.initdriver().driver()
        
    def tearDown(self):
        sleep(1)
        self.driver.quit()
        
    def base_func(self,num):
        fir = firstPage.firstPage(self.driver)
        sec = secondPage.secondPage(self.driver)
        sleep(1)
        fir.ele_checkbox_check(num)
        sleep(1)
        fir.ele_submit_click()
        first = fir.ele_checkbox_check(num)
        second = sec.ele_fruit_request()
        self.list = []
        self.list.append(first)
        self.list.append(second)
        return self.list
        
    def test_case1(self):
        a = self.base_func(1)
        msg = "assert error!"
        self.assertEqual(a[0], a[1], msg)
       
    def test_case2(self):
        a = self.base_func(2)
        msg = "assert error!"
        self.assertEqual(a[0], a[1], msg)
          
    def test_case3(self):
        a = self.base_func(3)
        msg = "assert error!"
        self.assertEqual(a[0], a[1], msg)
       
    def test_case4(self):
        a = self.base_func(4)
        msg = "assert error!"
        self.assertEqual(a[0], a[1], msg)
           
if __name__ == "__main__":
    unittest.main()
