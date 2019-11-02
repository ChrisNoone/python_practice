# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pymysql


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


def login(dr, *args):
    dr.find_element_by_xpath('//input[@placeholder="用户名"]').send_keys(args[0])
    dr.find_element_by_xpath('//input[@placeholder="密码"]').send_keys(args[1])
    dr.find_element_by_xpath('//input[@placeholder="验证码"]').click()
    sleep(5)
    dr.find_element_by_xpath('//button[contains(text(), "登录")]').click()
    sleep(3)
    dr.find_element_by_xpath('//a[contains(text(), "现金系统")]').click()
    sleep(1)
    dr.find_element_by_xpath('//span[contains(text(), "现金管理")]').click()
    sleep(1)


def deal_online(dr, users):
    dr.find_element_by_xpath('//a[contains(text(), "线上入款")]').click()
    sleep(3)
    try:
        for u in users:
            dr.find_element_by_xpath('//input[@placeholder="请输入内容"]').send_keys(Keys.CONTROL+'a')
            dr.find_element_by_xpath('//input[@placeholder="请输入内容"]').send_keys(Keys.BACKSPACE)
            dr.find_element_by_xpath('//input[@placeholder="请输入内容"]').send_keys(u)
            dr.find_element_by_xpath('//span[contains(text(), "搜 索")]/..').click()
            sleep(2)
            try:
                dr.find_elements_by_xpath('//span[contains(text(), "强制入款")]')[0].click()
                sleep(1)
                dr.find_element_by_xpath('//span[contains(text(), "确 定")]/..').click()
                sleep(1)
            except:
                pass
    except Exception as e:
        print('出现异常，用户：', u)
        print(e)


def deal_company(dr, users):
    dr.find_element_by_xpath('//a[contains(text(), "公司入款")]').click()
    sleep(3)
    try:
        for u in users:
            dr.find_element_by_xpath('//input[@placeholder="请输入内容"]').send_keys(Keys.CONTROL+'a')
            dr.find_element_by_xpath('//input[@placeholder="请输入内容"]').send_keys(Keys.BACKSPACE)
            dr.find_element_by_xpath('//input[@placeholder="请输入内容"]').send_keys(u)
            dr.find_element_by_xpath('//span[contains(text(), "搜 索")]/..').click()
            sleep(2)
            try:
                dr.find_elements_by_xpath('//div[contains(text(), "确认入款")]')[0].click()
                sleep(1)
                dr.find_element_by_xpath('//span[contains(text(), "确 定")]/..').click()
                sleep(1)
            except:
                pass
    except Exception as e:
        print('出现异常，用户：', u)
        print(e)


# user_data = get_users()
# url = 'https://demo.dggamesmanager.net/#/home/login'
# login_data = ('qa', '123456')

user_data = ['super01', 'super02', 'super03', 'super04', 'super05', 'super06', 'super07', 'super08', 'super09', 'super11', 'super15']
url = 'https://fusion.spgamesmanager.net/#/home/login'
login_data = ('super', '123456')
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(url)
driver.maximize_window()
sleep(3)
try:
    login(driver, *login_data)
    deal_company(driver, user_data)
    # deal_company(driver, user_data)
    deal_online(driver, user_data)
except Exception as e:
    print(e)
driver.quit()
