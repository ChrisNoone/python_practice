# coding: utf-8

import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def login(dr, user):
    dr.find_element_by_xpath('//a[contains(text(), "登录")]').click()
    sleep(1)
    dr.find_element_by_xpath('//input[@type="userName"]').send_keys(user)
    dr.find_element_by_xpath('//input[@type="password"]').send_keys('kosun123')
    dr.find_element_by_xpath('//input[@type="captcha"]').send_keys('1234')
    sleep(1)
    dr.find_elements_by_xpath('//a[contains(text(), "登录")]')[1].click()
    sleep(2)
    try:
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//img[@class="close-dialog"]')))
        dr.find_element_by_xpath('//img[@class="close-dialog"]').click()
    except:
        pass
    sleep(1)


def bet(dr):
    random_index = random.randint(0, 20)
    num = random.randint(20, 100)
    dr.find_elements_by_xpath('//tr[@class="first-tr"]//a')[random_index].click()
    dr.find_element_by_xpath('//div[@class="amount-item"]/input').send_keys(Keys.CONTROL+'a')
    dr.find_element_by_xpath('//div[@class="amount-item"]/input').send_keys(Keys.BACKSPACE)
    dr.find_element_by_xpath('//div[@class="amount-item"]/input').send_keys(num)
    sleep(1)
    dr.find_element_by_xpath('//a[contains(text(), "确认交易")]').click()
    sleep(1)
    dr.find_element_by_xpath('//a[contains(text(), "确认交易")]').click()
    sleep(2)


def logout(dr):
    dr.find_element_by_xpath('//a[@class="popover-title"]').click()
    sleep(1)
    dr.find_element_by_xpath('//a[contains(text(), "退出")]').click()
    sleep(2)


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://fusion.spmobileapi.net/splobby#/home')
driver.maximize_window()
users = []
with open('user.txt', 'r')as f:
    for line in f:
        users.append(line.rstrip('\n'))
for i in users:
    login(driver, i)
    bet(driver)
    logout(driver)
driver.quit()
