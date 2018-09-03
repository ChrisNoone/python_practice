# coding:utf-8

import time

class loginPage(object):
    """登录页面"""
    
    def __init__(self,driver):
        self.driver = driver
        
    def passname_ele(self):
        """返回用户名输入框"""
        ele = self.driver.find_element_by_xpath("//input[@type='text']")
        return ele
    
    def passpwd_ele(self):
        """返回密码输入框"""
        ele = self.driver.find_element_by_xpath("//input[@type='password']")
        return ele
    
    def login_ele(self):
        """返回登录按钮"""
        ele = self.driver.find_element_by_xpath("//html//body//main//div[5]")
        return ele
    
    def login_action(self,name='WEI',pwd='123456'):
        """登录业务"""
        self.passname_ele().send_keys(name)
        self.passpwd_ele().send_keys(pwd)
        time.sleep(1)
        self.login_ele().click()