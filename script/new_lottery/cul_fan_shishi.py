# coding: utf-8

import pymysql


def sum_list(li):
    total = 0
    for ele in range(0, len(li)):
        total = total + li[ele]
    return total


def cul_fan(haoma):
    result = sum_list(haoma) % 4
    if result == 0:
        result = 4
    return result


def get_haoma_from_sql(issue_no):
    pwd = 'Vp8WlTSsNnsQ1aWibWM='
    # db = pymysql.connect('fusion.mysql.polardb.rds.aliyuncs.com', 'dscp', pwd,
    #                      'dscp', charset='utf8')
    db = pymysql.connect('rm-3nsj79cd3oaiu72x9vo.mysql.rds.aliyuncs.com', 'dscp', 'MvozNyb4fnZbAcjmAcMpgtCo', 'dscp',
                         charset='utf8')
    cursor = db.cursor()
    cursor.execute('SELECT lottery_issue_prize_num FROM ds_lottery_issue WHERE lottery_id = (SELECT lottery_id FROM ds_lottery WHERE lottery_name = "五分时时番摊") AND lottery_issue_no = %s;' % issue_no)
    data = cursor.fetchall()
    try:
        for i in data:
            return list(map(int, i[0].split(',')))
    except:
        print('未获取到开奖号码！')


while(1):
    try:
        issue_no = int(input('请输入五分时时番摊的期号：'))
        print('本期和值：' + str(cul_fan(get_haoma_from_sql(issue_no))))
    except Exception as e:
        print('请重试！')
        print(e)
    print('---------------------------------------')
