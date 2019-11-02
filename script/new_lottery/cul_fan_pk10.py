# coding: utf-8

import pymysql


def sum_list(li):
    total = 0
    for ele in range(0, len(li)):
        total = total + li[ele]
    return total


def cul_fan(haoma):
    tmp = haoma[0:3]
    result = sum_list(tmp) % 4
    if result == 0:
        result = 4
    return result


def get_haoma_from_sql(issue_no):
    pwd = 'Vp8WlTSsNnsQ1aWibWM='
    db = pymysql.connect('fusion.mysql.polardb.rds.aliyuncs.com', 'dscp', pwd,
                         'dscp', charset='utf8')
    cursor = db.cursor()
    cursor.execute('SELECT lottery_issue_prize_num FROM ds_lottery_issue WHERE lottery_id = (SELECT lottery_id FROM ds_lottery WHERE lottery_name = "五分PK番摊") AND lottery_issue_no = %s;' % issue_no)
    data = cursor.fetchall()
    try:
        for i in data:
            return list(map(int, i[0].split(',')))
    except:
        print('未获取到开奖号码！')


while(1):
    try:
        issue_no = int(input('请输入五分pk番摊的期号：'))
        print('本期和值：' + str(cul_fan(get_haoma_from_sql(issue_no))))
    except :
        print('请重试！')
    print('---------------------------------------')
