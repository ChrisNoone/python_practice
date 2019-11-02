# coding: utf-8

import random
import pymysql
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import traceback


def get_users():
    # pwd = input('请输入数据库密码：')
    pwd = 'MvozNyb4fnZbAcjmAcMpgtCo'
    db = pymysql.connect('rm-3nsj79cd3oaiu72x9vo.mysql.rds.aliyuncs.com', 'dscp', pwd,
                         'dscp', charset='utf8')

    cursor = db.cursor()
    cursor.execute('SELECT user_name FROM ds_user WHERE FIND_IN_SET(134,user_all_pid);')
    data = cursor.fetchall()
    result = []
    for i in data:
        result.append(i[0])
    return result


def login(dr):
    dr.find_element_by_xpath('//input[@placeholder="用户名"]').send_keys(u)
    dr.find_element_by_xpath('//input[@placeholder="密码"]').send_keys('kosun123')
    dr.find_element_by_xpath('//input[@placeholder="验证码"]').send_keys('4444')
    dr.find_element_by_xpath('//button[contains(text(), "登录")]').click()
    # WebDriverWait(driver, 10, 0.5).until(ec.element_to_be_clickable((by.By.XPATH, '//div[@class="dialog"]/i')))
    # dr.find_element_by_xpath('//div[@class="dialog"]/i').click()
    sleep(1)


def close(dr):
    handles = dr.window_handles
    length = len(handles)
    for i in range(length):
        if i != 0:
            dr.switch_to.window(handles[length - i])
            dr.close()
            sleep(0.5)
    dr.switch_to.window(handles[0])


def logout(dr):
    close(dr)
    dr.find_element_by_xpath('//span[contains(text(), "退出")]').click()
    sleep(2)


def online_recharge(dr):
    dr.find_element_by_xpath('//div[@class="user"]/a[contains(text(), "充值")]').click()
    handles = dr.window_handles
    dr.switch_to.window(handles[1])
    sleep(3)

    dr.find_element_by_xpath('//p[contains(text(), "支付宝")]').click()
    dr.find_element_by_xpath('//button[contains(text(), "下一步")]').click()
    sleep(1)
    dr.find_elements_by_xpath('//p[contains(text(), "扫码")]')[0].click()
    dr.find_element_by_xpath('//input[@placeholder="请输入金额"]').send_keys(Keys.CONTROL+'a')
    dr.find_element_by_xpath('//input[@placeholder="请输入金额"]').send_keys(Keys.BACKSPACE)
    sleep(0.5)
    dr.find_element_by_xpath('//input[@placeholder="请输入金额"]').send_keys(random.randint(50, 100))
    dr.find_element_by_xpath('//button[contains(text(), "下一步")]').click()
    sleep(3)
    close(dr)
    sleep(1)


def company_recharge(dr):
    dr.find_element_by_xpath('//div[@class="user"]/a[contains(text(), "充值")]').click()
    handles = dr.window_handles
    dr.switch_to.window(handles[1])
    sleep(3)

    dr.find_element_by_xpath('//p[contains(text(), "公司入款")]').click()
    dr.find_element_by_xpath('//button[contains(text(), "下一步")]').click()
    sleep(1)
    dr.find_elements_by_xpath('//p[contains(text(), "银行")]')[0].click()
    dr.find_element_by_xpath('//input[@placeholder="请输入金额"]').send_keys(Keys.CONTROL + 'a')
    dr.find_element_by_xpath('//input[@placeholder="请输入金额"]').send_keys(Keys.BACKSPACE)
    sleep(0.5)
    dr.find_element_by_xpath('//input[@placeholder="请输入金额"]').send_keys(random.randint(50, 100))
    dr.find_element_by_xpath('//button[contains(text(), "下一步")]').click()
    sleep(3)
    dr.find_element_by_xpath('//input[@placeholder="存款人姓名"]').send_keys('银行卡入款')
    dr.find_element_by_xpath('//span[contains(text(), "确认存款")]').click()
    sleep(2)
    close(dr)
    sleep(1)


def friend_recharge(dr):
    dr.find_element_by_xpath('//div[@class="user"]/a[contains(text(), "充值")]').click()
    handles = dr.window_handles
    dr.switch_to.window(handles[1])
    sleep(3)

    dr.find_element_by_xpath('//p[contains(text(), "公司入款")]').click()
    dr.find_element_by_xpath('//button[contains(text(), "下一步")]').click()
    sleep(1)
    dr.find_elements_by_xpath('//p[contains(text(), "好友支付")]')[0].click()
    dr.find_element_by_xpath('//input[@placeholder="请输入金额"]').send_keys(Keys.CONTROL + 'a')
    dr.find_element_by_xpath('//input[@placeholder="请输入金额"]').send_keys(Keys.BACKSPACE)
    sleep(0.5)
    dr.find_element_by_xpath('//input[@placeholder="请输入金额"]').send_keys(random.randint(50, 100))
    dr.find_element_by_xpath('//button[contains(text(), "下一步")]').click()
    sleep(3)
    dr.find_element_by_xpath('//label[contains(text(), "转账备注")]/following-sibling::div/input').send_keys('好友支付')
    dr.find_element_by_xpath('//input[@placeholder="转账订单后四位"]').send_keys('5420')
    dr.find_element_by_xpath('//button[contains(text(), "确认充值")]').click()
    sleep(2)
    close(dr)
    sleep(1)


# users = get_users()
# url = 'https://online.baifu-tech.net/home'
users = ['super01', 'super02', 'super03', 'super04', 'super05', 'super06', 'super07', 'super08', 'super09', 'super11', 'super15']
url = 'https://fusion.spmobileapi.net/home'
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get(url)
driver.maximize_window()
for u in users:
    try:
        login(driver)
        online_recharge(driver)
        company_recharge(driver)
        # friend_recharge(driver)
        print('用户 %s 充值完成.' % u)
    except:
        print('执行出现异常，账号：%s' % u)
        # driver.get_screenshot_as_file('d:\\%s.png' % u)
        traceback.print_exc()
    logout(driver)
driver.quit()
