
# coding:utf-8

from selenium import webdriver
from time import sleep
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'MAY9X17728W11076'
# desired_caps['app'] = PATH(r'D:\smartoutlet.apk')
desired_caps['appPackage'] = 'com.example.android.notepad'
desired_caps['appActivity'] = '.NotePadActivity'

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

sleep(2)

ds = driver.find_elements_by_id('com.example.android.notepad:id/app_bar_menu')
# print type(ds),ds
print type(ds[0]),ds[0]
ds[0].click()
# print "test"

sleep(2)

driver.quit()
