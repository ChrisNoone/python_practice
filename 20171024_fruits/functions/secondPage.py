# coding:utf-8

class secondPage():
    def __init__(self,driver):
        self.driver = driver
        
    def ele_fruit_request(self):
        fruits = self.driver.find_element_by_xpath("//font[@size=5]/ul[1]/li")
        name = fruits.text.decode('utf-8')
        return name