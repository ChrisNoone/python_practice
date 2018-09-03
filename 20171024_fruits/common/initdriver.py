# coding:utf-8

from selenium import webdriver
from time import sleep

class initdriver():
    global url
    url = "http://192.168.25.213:8080/examples/jsp/checkbox/check.html"

    def driver(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
#         self.driver.maximize_window()
        sleep(1)
        return self.driver