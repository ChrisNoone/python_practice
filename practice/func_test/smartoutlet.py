
# coding:utf-8

from selenium import webdriver
from time import sleep
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.1.0'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['app'] = PATH(r'D:\smartoutlet.apk')
desired_caps['appPackage'] = 'com.etekcity.vesyncplatform'
desired_caps['appActivity'] = /
  'com.etekcity.vesyncplatform.presentation.ui.activities.LaunchActivity'

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

sleep(5)
