# coding: utf-8

import threading
from selenium import webdriver
from time import sleep


def open_bro():
    dr = webdriver.Chrome()
    dr.get('http://10.10.10.224:10086/v1/static/index.html')
    dr.maximize_window()
    while(1):
        sleep(360)


for i in range(5):
    threading.Thread(target=open_bro).start()
