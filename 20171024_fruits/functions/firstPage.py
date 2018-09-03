# coding:utf-8

class firstPage():
    def __init__(self,driver):
        self.driver = driver
        
    def ele_checkboxs(self):
        ele_checkboxs = self.driver.find_elements_by_xpath("//input[@type='checkbox']")
        return ele_checkboxs
    
    def ele_submit(self):
        ele_submit = self.driver.find_element_by_xpath("//input[@type='submit']")
        return ele_submit
    
    def ele_checkbox_check(self,num):
        global eles,name
        eles = len(self.ele_checkboxs())
        for n in range(eles):
            if n == num-1:
                name = self.ele_checkboxs()[n].get_attribute("value")
                self.ele_checkboxs()[n].click()
        return name
            
    def ele_submit_click(self):
        self.ele_submit().click()