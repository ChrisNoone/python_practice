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


def close(dr):
    handles = dr.window_handles
    length = len(handles)
    for i in range(length):
        if i != 0:
            dr.switch_to.window(handles[length - i])
            dr.close()
            sleep(0.5)
    dr.switch_to.window(handles[0])


def login(dr, user):
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//div[contains(text(), "请您先登录/注册")]')))
    dr.find_element_by_xpath('//div[contains(text(), "请您先登录/注册")]').click()
    sleep(1)
    dr.find_element_by_xpath('//input[@placeholder="请输入用户名"]').send_keys(Keys.CONTROL + 'a')
    dr.find_element_by_xpath('//input[@placeholder="请输入用户名"]').send_keys(Keys.BACKSPACE)
    dr.find_element_by_xpath('//input[@placeholder="请输入用户名"]').send_keys(user)
    dr.find_element_by_xpath('//input[@placeholder="请输入密码"]').send_keys('kosun123')
    dr.find_element_by_xpath('//input[@placeholder="请输入验证码"]').send_keys('4444')
    dr.find_element_by_xpath('//button[contains(text(), "登录")]').click()
    sleep(3)


def bet(dr):
    dr.find_element_by_xpath('//div[@class="hallMenu"]/div[contains(text(), "六合彩")]').click()
    sleep(1)
    dr.find_element_by_xpath(
        '//div[contains(text(), "分分六")]/../../following-sibling::div//div[contains(text(), "立即购彩")]').click()
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
    sleep(1)
    dr.refresh()
    return num


def logout(dr):
    dr.get('https://fusion.spmobileapi.net/dglobby#')
    sleep(1)
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//*[contains(text(), "退出")]')))
    dr.find_element_by_xpath('//*[contains(text(), "退出")]').click()
    sleep(2)


users = []
with open('user.txt', 'r')as f:
    for line in f:
        users.append(line.rstrip('\n'))
url = 'https://fusion.spmobileapi.net/dglobby#/'

driver = webdriver.Chrome()
driver.implicitly_wait(15)
driver.get(url)
driver.maximize_window()
for u in users:
    try:
        login(driver, u)
        money = bet(driver)
        print('%s下注%s元.' % (u, str(money)))
    except:
        print('执行出现异常，账号：%s' % u)
        # driver.get_screenshot_as_file('d:\\%s.png' % u)
        traceback.print_exc()
        break
    logout(driver)
driver.quit()
