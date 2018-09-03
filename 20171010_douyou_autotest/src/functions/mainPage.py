# coding:utf-8

import time

class mainPage(object):
    """主页"""
    
    def __init__(self,driver):
        self.driver = driver
        
    def base_ele(self):
        """基础模块"""
        ele = self.driver.find_element_by_xpath("//div[text()='基础模块']")
        return ele
    
    def marketing_ele(self):
        """营销"""
        ele = self.driver.find_element_by_xpath("//div[text()='营销']")
        return ele
    
    def next_ele(self):
        """向下翻页"""
        ele = self.driver.find_element_by_xpath("//div[@node-name='next']")
        return ele
    
    def prev_ele(self):
        """向上翻页"""
        ele = self.driver.find_element_by_xpath("//div[@node-name='prev']")
        return ele
    
    def orders_ele(self):
        """订单"""
        ele = self.driver.find_element_by_xpath("//div[text()='订单']")
        return ele
    
    def base_click(self):
        """打开基础模块"""
        self.base_ele().click()
        
    def orders_click(self):
        """打开订单中心"""
        self.next_ele().click()
        time.sleep(1)
        self.orders_ele().click()