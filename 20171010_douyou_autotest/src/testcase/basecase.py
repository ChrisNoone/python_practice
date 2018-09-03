# coding:utf-8

from src.common import *
from src.functions import *
import unittest
import time

class base_case(unittest.TestCase):
    def setUp(self):
        self.driver = initdriver.initdriver().initDriver()
        time.sleep(3)
        
    @unittest.skip(u"跳过示例")    
    def testcase1(self):
        loginPage.loginPage(self.driver).login_action('WEI','123456')
        resultlist = mainPage.mainPage(self.driver).base_ele().text.encode("utf-8")
#         resultlist要进行utf-8编码，否则后面断言会和“基础模块”不相等，打印resultlist的type可以看到编码前的类型和编码后的类型
#         print type(resultlist)
#         mytest类继承了unittest.TestCase类，它有一个默认的断言方法assertEqual，所以这里直接调用，调用这个方法对比前两个参数，如果不相等，抛出第三个参数的内容
        self.assertEqual(resultlist,"基础模块","实际结果[%s]与预期不匹配"%resultlist)
        
    def testcase2(self):
        loginPage.loginPage(self.driver).login_action()
        mainPage.mainPage(self.driver).base_click()
        time.sleep(1)
        page = basePage.basePage(self.driver)
        time.sleep(1)
        page.baseSetting_click()
        time.sleep(1)
        page.accessTypes_click()
        time.sleep(1)
        page.cinemaGroup_click()
        time.sleep(1)
        page.films_click()
        time.sleep(1)
        page.cinemas_click()
        time.sleep(1)
        page.shows_click()
        time.sleep(1)
        page.cinemaShows_click()
        time.sleep(1)
        page.channelShows_click()
        time.sleep(1)
        page.parameterSet_click()
        time.sleep(1)
        page.cityGroup_click()
        time.sleep(1)
        page.channels_click()
        time.sleep(1)
       
    # @unittest.skip(u"跳过示例")
    def testcase3(self):
        loginPage.loginPage(self.driver).login_action()
        mainPage.mainPage(self.driver).orders_click()
        
    def tearDown(self):
        time.sleep(3)
        self.driver.quit()
        
if __name__ == "__main__":
#     main()方法使用TestLoader类来搜索所有包含在该模块中以“test”命名开头的测试方法，并自动执行他们
    unittest.main()