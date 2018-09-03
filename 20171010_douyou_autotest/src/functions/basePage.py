# coding:utf-8

class basePage(object):
    """基础模块"""
    
    def __init__(self,driver):
        self.driver = driver
       
    def baseSetting_ele(self):
        """基础设置""" 
        ele = self.driver.find_element_by_xpath("//a[@title='基础设置']")
        return ele
    
    def accessTypes_ele(self):
        """接入类型""" 
        ele = self.driver.find_element_by_xpath("//a[@title='接入类型']")
        return ele
    
    def cinemaGroup_ele(self):
        """影院组管理""" 
        ele = self.driver.find_element_by_xpath("//a[@title='影院组管理']")
        return ele
    
    def films_ele(self):
        """影片管理""" 
        ele = self.driver.find_element_by_xpath("//a[@title='影片管理']")
        return ele
    
    def cinemas_ele(self):
        """影院管理""" 
        ele = self.driver.find_element_by_xpath("//a[@title='影院管理']")
        return ele
    
    def shows_ele(self):
        """排期管理""" 
        ele = self.driver.find_element_by_xpath("//a[@title='排期管理']")
        return ele
    
    def cinemaShows_ele(self):
        """影院排期管理""" 
        ele = self.driver.find_element_by_xpath("//a[@title='影院排期管理']")
        return ele
    
    def channelShows_ele(self):
        """渠道排期管理""" 
        ele = self.driver.find_element_by_xpath("//a[@title='渠道排期管理']")
        return ele
    
    def parameterSet_ele(self):
        """参数设置""" 
        ele = self.driver.find_element_by_xpath("//a[@title='参数设置']")
        return ele
    
    def cityGroup_ele(self):
        """城市分组""" 
        ele = self.driver.find_element_by_xpath("//a[@title='城市分组']")
        return ele
    
    def channels_ele(self):
        """渠道管理""" 
        ele = self.driver.find_element_by_xpath("//a[@title='渠道管理']")
        return ele
    
    def baseSetting_click(self):
        """打开基础设置"""
        self.baseSetting_ele().click()
    
    def accessTypes_click(self):
        """打开接入类型"""
        self.accessTypes_ele().click()
        
    def cinemaGroup_click(self):
        """打开影院组管理"""
        self.cinemaGroup_ele().click()
        
    def films_click(self):
        """打开影片管理"""
        self.films_ele().click()
    
    def cinemas_click(self):
        """打开影院管理"""
        self.cinemas_ele().click()
        
    def shows_click(self):
        """打开排期管理"""
        self.shows_ele().click()
        
    def cinemaShows_click(self):
        """打开影院排期管理"""
        self.cinemaShows_ele().click()
        
    def channelShows_click(self):
        """打开渠道排期管理"""
        self.channelShows_ele().click()
    
    def parameterSet_click(self):
        """打开参数设置"""
        self.parameterSet_ele().click()
        
    def cityGroup_click(self):
        """打开城市分组"""
        self.cityGroup_ele().click()
        
    def channels_click(self):
        """打开渠道管理"""
        self.channels_ele().click()
        
    def menu_eles(self):
        self.driver.fi
        