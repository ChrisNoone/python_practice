# coding: utf-8

from selenium import webdriver
from time import sleep
import os
import threading


def login(dr, u):
    url = 'https://apphosting.spmobileapi.net/home/application/publish.html'
    dr.get(url)
    sleep(2)
    dr.find_element_by_id('username').send_keys(u)
    dr.find_element_by_id('password').send_keys(u)
    dr.find_element_by_id('submitButton').click()
    sleep(3)


def upload(dr, file):
    dr.find_element_by_xpath('//span[contains(text(), "发布")]').click()
    sleep(1)
    dr.find_element_by_xpath('//div[contains(text(), "立刻上传")]//following-sibling::div').click()
    sleep(1)
    os.system('D:\\upload.exe "%s"' % file)


def do(*args):
    d = r'D:\kosun\下载\Telegram Desktop\apk'
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    login(driver, args[0])
    upload(driver, os.path.join(d, args[1]))
    sleep(10)
    driver.quit()


data = [('12345678961', 'app-c9-release.apk'),
        ('12345678962', 'app-cp111-release.apk'),
        ('12345678963', 'app-cp500w-release.apk'),
        ('12345678964', 'app-cp555-release.apk'),
        ('12345678965', 'app-cp899-release.apk'),
        ('12345678966', 'app-cp7070-release.apk'),
        ('12345678967', 'app-cpcp-release.apk'),
        ('12345678968', 'app-duocai-release.apk'),
        ('12345678969', 'app-yccp-release.apk'),
        ('12345678970', 'app-zccp-release.apk')]
for i in data:
    threading.Thread(target=do, args=i).start()
