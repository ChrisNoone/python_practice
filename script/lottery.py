# coding: utf-8

import random
import pymysql
import traceback
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def get_users():
    # pwd = input('请输入数据库密码：')
    pwd = 'MvozNyb4fnZbAcjmAcMpgtCo'
    db = pymysql.connect('rm-3nsj79cd3oaiu72x9vo.mysql.rds.aliyuncs.com', 'dscp', pwd,
                         'dscp', charset='utf8')
    cursor = db.cursor()
    cursor.execute('SELECT user_name FROM ds_user WHERE FIND_IN_SET(134,user_all_pid) order by user_name DESC;')
    data = cursor.fetchall()
    result = []
    for i in data:
        result.append(i[0])
    return result


def login(dr, user):
    url = 'https://fusion.spmobileapi.net/dglobby#'
    dr.get(url)
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//div[contains(text(), "请您先登录/注册")]')))
    dr.find_element_by_xpath('//div[contains(text(), "请您先登录/注册")]').click()
    sleep(1)
    dr.find_element_by_xpath('//input[@placeholder="请输入用户名"]').send_keys(Keys.CONTROL + 'a')
    dr.find_element_by_xpath('//input[@placeholder="请输入用户名"]').send_keys(Keys.BACKSPACE)
    dr.find_element_by_xpath('//input[@placeholder="请输入用户名"]').send_keys(user)
    dr.find_element_by_xpath('//input[@placeholder="请输入密码"]').send_keys('kosun123')
    dr.find_element_by_xpath('//input[@placeholder="请输入验证码"]').send_keys('4444')
    dr.find_element_by_xpath('//button[contains(text(), "登录")]').click()
    sleep(1)


def logout(dr):
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//*[contains(text(), "退出")]')))
    dr.find_element_by_xpath('//*[contains(text(), "退出")]').click()
    sleep(2)


def gen_url(n):
    lotterys = ['24', '29', '31', '16', '25', '56', '46']
    url = 'https://fusion.spmobileapi.net/dglobby#/play/'
    urls = []
    for i in range(n):
        urls.append(url + lotterys[i])
    return urls


def bet(dr, user, n):
    urls = gen_url(n)
    for url in urls:
        dr.get(url)
        sleep(3)
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//input[@placeholder="单注金额"]')))
        dr.find_element_by_xpath('//input[@placeholder="单注金额"]').click()
        dr.find_element_by_xpath('//input[@placeholder="单注金额"]').send_keys(Keys.BACK_SPACE)
        sleep(1)
        num = random.randint(20, 100)
        dr.find_element_by_xpath('//input[@placeholder="单注金额"]').send_keys(num)
        # 拖动返利条
        actions = ActionChains(dr)
        el = dr.find_element_by_xpath('//span[contains(text(), "赔率")]/following-sibling::div/div[4]')
        actions.drag_and_drop_by_offset(el, '150', '0').perform()
        sleep(1)
        dr.find_element_by_xpath('//button[contains(text(), "随机1注")]').click()
        dr.find_element_by_xpath('//button[contains(text(), "确认投注")]').click()
        print('%s，下注%s元，彩种id[%s].' % (user, str(num), url[-2:]))
        dr.refresh()
        sleep(1)


users = ['super01', 'super02', 'super03', 'super04', 'super05', 'super06', 'super07', 'super08', 'super09', 'super11', 'super15']
driver = webdriver.Chrome()
driver.maximize_window()
for u in users:
    try:
        login(driver, u)
        bet(driver, u, 7)
    except:
        print('执行出现异常，账号：%s' % u)
        driver.get_screenshot_as_file('d:\\%s.png' % u)
        traceback.print_exc()
    logout(driver)
driver.quit()
