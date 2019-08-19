# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random


def login(dr, member='super', pwd='123456'):
    dr.find_element_by_xpath('//input[@placeholder="用户名"]').send_keys(member)
    dr.find_element_by_xpath('//input[@placeholder="密码"]').send_keys(pwd)
    # dr.find_element_by_xpath('//input[@placeholder="验证码"]').click()
    # sleep(5)
    dr.find_element_by_xpath('//input[@placeholder="验证码"]').send_keys('1234')
    sleep(1)
    dr.find_element_by_xpath('//button[contains(text(), "登录")]').click()
    sleep(2)


def jump_usermanagemant(dr):
    dr.find_element_by_xpath('//a[contains(text(), "用户")]').click()
    sleep(1)
    dr.find_element_by_xpath('//a[contains(text(), "会员管理")]').click()
    sleep(2)


def change_pwd(dr, user):
    dr.find_element_by_xpath('//input[@placeholder="请输入用户名"]').send_keys(Keys.CONTROL+'a')
    dr.find_element_by_xpath('//input[@placeholder="请输入用户名"]').send_keys(Keys.BACKSPACE)
    dr.find_element_by_xpath('//input[@placeholder="请输入用户名"]').send_keys(user)
    dr.find_element_by_xpath('//span[contains(text(), "搜 索")]/..').click()
    sleep(1)
    dr.find_element_by_xpath('//span[contains(text(), "会员详情")]').click()
    sleep(1)
    dr.find_element_by_xpath('//input[@type="password"]').send_keys("kosun123")
    dr.find_elements_by_xpath('//span[contains(text(), "保存设置")]/..')[0].click()
    sleep(1)
    dr.find_element_by_xpath('//button[contains(text(), "确定")]').click()
    sleep(2)
    dr.refresh()
    sleep(1)


def change_realname(dr, user):
    dr.find_element_by_xpath('//input[@placeholder="请输入用户名"]').send_keys(Keys.CONTROL + 'a')
    dr.find_element_by_xpath('//input[@placeholder="请输入用户名"]').send_keys(Keys.BACKSPACE)
    dr.find_element_by_xpath('//input[@placeholder="请输入用户名"]').send_keys(user)
    dr.find_element_by_xpath('//span[contains(text(), "搜 索")]/..').click()
    sleep(1)
    dr.find_element_by_xpath('//span[contains(text(), "会员详情")]').click()
    sleep(1)
    dr.find_element_by_xpath('//*[@title="真实姓名"]/../..//input').send_keys(Keys.CONTROL + 'a')
    dr.find_element_by_xpath('//*[@title="真实姓名"]/../..//input').send_keys(Keys.BACKSPACE)
    dr.find_element_by_xpath('//*[@title="真实姓名"]/../..//input').send_keys(user + "名")
    dr.find_elements_by_xpath('//span[contains(text(), "保存设置")]/..')[2].click()
    sleep(1)
    dr.find_element_by_xpath('//button[contains(text(), "确定")]').click()
    sleep(2)
    dr.refresh()
    sleep(1)


def change_financial(dr, user):
    dr.find_element_by_xpath('//input[@placeholder="请输入用户名"]').send_keys(Keys.CONTROL + 'a')
    dr.find_element_by_xpath('//input[@placeholder="请输入用户名"]').send_keys(Keys.BACKSPACE)
    dr.find_element_by_xpath('//input[@placeholder="请输入用户名"]').send_keys(user)
    dr.find_element_by_xpath('//span[contains(text(), "搜 索")]/..').click()
    sleep(1)
    dr.find_element_by_xpath('//span[contains(text(), "会员详情")]').click()
    sleep(1)
    dr.find_element_by_xpath('//*[@title="资金密码"]/../..//input').send_keys('123456')
    dr.find_elements_by_xpath('//span[contains(text(), "保存设置")]/..')[3].click()
    sleep(1)
    dr.find_element_by_xpath('//button[contains(text(), "确定")]').click()
    sleep(2)
    dr.refresh()
    sleep(1)


def add_number(dr, user):
    dr.find_element_by_xpath('//input[@placeholder="请输入用户名"]').send_keys(Keys.CONTROL + 'a')
    dr.find_element_by_xpath('//input[@placeholder="请输入用户名"]').send_keys(Keys.BACKSPACE)
    dr.find_element_by_xpath('//input[@placeholder="请输入用户名"]').send_keys(user)
    dr.find_element_by_xpath('//span[contains(text(), "搜 索")]/..').click()
    sleep(1)
    dr.find_element_by_xpath('//span[contains(text(), "会员详情")]').click()
    sleep(1)
    dr.find_element_by_xpath('//div[contains(text(), "设置银行资料")]').click()
    sleep(1)
    if len(dr.find_elements_by_xpath('//span[contains(text(), "删 除")]')) == 1:
        dr.find_element_by_xpath('//span[contains(text(), "删 除")]/..').click()
        sleep(1)
        dr.find_element_by_xpath('//button[@class="comfrim"]').click()
        sleep(1)
    dr.find_element_by_xpath('//span[contains(text(), "添加银行资料")]/..').click()
    sleep(1)
    num = '44218' + ''.join(str(random.choice(range(10))) for _ in range(13))
    dr.find_elements_by_xpath('//input[@placeholder="请输入银行账号"]')[1].send_keys(num)
    dr.find_element_by_xpath('//input[@placeholder="请输入开户行"]').send_keys('万达碧桂园')
    sleep(1)
    dr.find_element_by_xpath('//span[contains(text(), "提 交")]/..').click()
    sleep(2)
    dr.refresh()
    sleep(1)

"""
-- SELECT user_id,user_name,user_pid,user_last_login_time FROM ds_user WHERE user_pid IN (SELECT DISTINCT(user_pid) FROM ds_user) 
-- AND user_last_login_time <'2019-04-01 00:00:00' GROUP BY user_pid ORDER BY user_id DESC LIMIT 300,5;
-- 
"""

driver = webdriver.Chrome()
# driver.implicitly_wait(10)
driver.get('https://fusion.spgamesmanager.net/#/home/login')
driver.maximize_window()
login(driver)
jump_usermanagemant(driver)
users = []
with open('user.txt', 'r')as f:
    for line in f:
        users.append(line.rstrip('\n'))
for i in users:
    # change_pwd(driver, i)
    # change_realname(driver, i)
    # change_financial(driver, i)
    add_number(driver, i)
driver.quit()
