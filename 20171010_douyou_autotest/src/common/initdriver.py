# coding:utf-8

from selenium import webdriver

class initdriver():
    global url
    url = "http://172.16.10.55:41/login.html"
    
    def initDriver(self):
        self.driver = webdriver.Chrome()
#         隐性等待10秒
        self.driver.implicitly_wait(10)
        self.driver.get(url)
        self.driver.maximize_window()
        return self.driver