# coding:utf-8

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://172.16.10.55:41/login.html")
driver.maximize_window()
sleep(1)

driver.find_element_by_xpath("//input[@type='text']").send_keys("wei")
driver.find_element_by_xpath("//input[@type='password']").send_keys("123456")
sleep(1)
driver.find_element_by_xpath("//html//body//main//div[5]").click()
sleep(1)

driver.find_element_by_xpath("//div[text()='基础模块']").click()
sleep(1)
driver.find_element_by_xpath("//a[@title='基础设置']").click()
sleep(1)

menu_a = driver.find_elements_by_xpath("//*[@class='sub-menu parent-selected']/a")
print type(menu_a),menu_a

for a in menu_a:
    print type(a),a
    a.click()
    sleep(1)
    
driver.quit()