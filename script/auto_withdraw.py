# coding: utf-8

import random
import threading
import traceback
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def withdraw(user, url):
    pwd = 'kosun123'
    ac_pwd = '123456'
    captcha = '4444'
    min_line = 200

    dr = webdriver.Chrome()
    dr.implicitly_wait(20)
    dr.get(url)
    dr.maximize_window()
    WebDriverWait(dr, 15, 1).until(ec.element_to_be_clickable((By.XPATH, '//input[@placeholder="用户名"]')))
    dr.find_element_by_xpath('//input[@placeholder="用户名"]').send_keys(user)
    dr.find_element_by_xpath('//input[@placeholder="密码"]').send_keys(pwd)
    dr.find_element_by_xpath('//input[@placeholder="验证码"]').send_keys(captcha)
    dr.find_element_by_xpath('//button[contains(text(), "登录")]').click()
    sleep(5)
    dr.find_element_by_xpath('//div[@class="dialog"]/i').click()
    sleep(1)
    dr.find_element_by_xpath('//a[contains(text(), "提现")]').click()
    sleep(1)
    handles = dr.window_handles
    dr.switch_to.window(handles[1])

    n = 0
    err = 1
    while 1:
        try:
            WebDriverWait(dr, 15, 1).until(ec.visibility_of_element_located((By.XPATH, '//tbody/tr[2]/td[2]')))
            balance = dr.find_element_by_xpath('//tbody/tr[2]/td[2]').text
            balance = balance[:-1]
            if float(balance) < min_line:
                print('%s 可提现金额不足%s元，终止脚本...' % (user, min_line))
                break
            else:
                num = random.randint(10, 200)
                dr.find_element_by_xpath('//input[@placeholder="请输入提现金额"]').send_keys(num)
                dr.find_element_by_xpath('//input[@placeholder="请输入资金密码"]').send_keys(ac_pwd)
                sleep(1)
                dr.find_element_by_xpath('//button[contains(text(), "提现")]').click()
                sleep(3)
                n = n + 1
                print('%s 第%s次提现结束.' % (user, str(n)))
                dr.refresh()
            sleep(57)
        except:
            if err <= 5:
                print("发生错误，第%s次重试[%s]" % (err, user))
                err = err + 1
                # dr.refresh()
                dr.get('https://online.baifu-tech.net/memberCenter#/home/withdraw')
                continue
            else:
                # dr.get_screenshot_as_file('d:\\%s.png' % user)
                traceback.print_exc()
                break
    dr.quit()


# url = 'https://online.baifu-tech.net/home'
# users = ['demo01', 'demo02', 'demo0329', 'artee24']

url = 'https://fusion.spmobileapi.net/home'
# users = ['super01', 'super06', 'super07', 'super08', 'super09']
users = ['super06']
for u in users:
    threading.Thread(target=withdraw, args=(u, url)).start()
print('开始多线程执行...')
