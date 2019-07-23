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


# TODO: 自动公司入款，及确认入款
# TODO: 自动在线入款，及确认入款
# TODO: 自动投注增加拖动返利条

def get_users():
    # pwd = input('请输入数据库密码：')
    pwd = ''
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


def login(dr):
    dr.find_element_by_xpath('//input[@placeholder="用户名"]').send_keys(u)
    dr.find_element_by_xpath('//input[@placeholder="密码"]').send_keys('kosun123')
    dr.find_element_by_xpath('//input[@placeholder="验证码"]').send_keys('4444')
    dr.find_element_by_xpath('//button[contains(text(), "登录")]').click()
    try:
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//div[@class="dialog"]/i')))
        dr.find_element_by_xpath('//div[@class="dialog"]/i').click()
    except:
        pass
    sleep(1)


def bet(dr):
    dr.find_element_by_xpath('//a[contains(text(), "购彩大厅")]').click()
    # dr.find_element_by_xpath('//a[contains(text(), "数字彩")]').click()
    sleep(1)
    handles = dr.window_handles
    dr.switch_to.window(handles[1])
    dr.find_element_by_xpath('//div[contains(text(), "六合彩")]').click()
    sleep(1)
    dr.find_element_by_xpath(
        '//div[contains(text(), "分分六")]/../../following-sibling::div//div[contains(text(), "立即购彩")]').click()
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//input[@placeholder="单注金额"]')))
    dr.find_element_by_xpath('//input[@placeholder="单注金额"]').click()
    dr.find_element_by_xpath('//input[@placeholder="单注金额"]').send_keys(Keys.BACK_SPACE)
    sleep(1)
    num = random.randint(10, 50)
    dr.find_element_by_xpath('//input[@placeholder="单注金额"]').send_keys(num)
    # 拖动返利条
    actions = ActionChains(dr)
    el = dr.find_element_by_xpath('//span[contains(text(), "赔率")]/following-sibling::div/div[4]')
    actions.drag_and_drop_by_offset(el, '150', '0').perform()
    sleep(1)
    dr.find_element_by_xpath('//button[contains(text(), "随机1注")]').click()
    dr.find_element_by_xpath('//button[contains(text(), "确认投注")]').click()
    sleep(1)
    return num


def logout(dr):
    close(dr)
    dr.find_element_by_xpath('//span[contains(text(), "退出")]').click()
    sleep(2)


url = 'https://online.baifu-tech.net/home'
users = get_users()
# users = ['super01', 'super02', 'super03', 'super04', 'super05', 'super06', 'super07', 'super08', 'super09', 'super11', 'super15']
# url = 'https://fusion.spmobileapi.net/home'

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get(url)
driver.maximize_window()
for u in users:
    try:
        login(driver)
        money = bet(driver)
        print('%s下注%s元.' % (u, str(money)))
    except:
        print('执行出现异常，账号：%s' % u)
        driver.get_screenshot_as_file('d:\\%s.png' % u)
        traceback.print_exc()
    logout(driver)
driver.quit()

