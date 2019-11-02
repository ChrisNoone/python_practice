# coding: utf-8

import pymysql


def sum_list(li):
    total = 0
    for ele in range(0, len(li)):
        total = total + li[ele]
    return total


def cul_cat(haoma):
    for no1 in haoma:
        tmp1 = haoma.copy()
        tmp1.remove(no1)
        for no2 in tmp1:
            tmp2 = tmp1.copy()
            tmp2.remove(no2)
            for no3 in tmp2:
                tmp3 = tmp2.copy()
                tmp3.remove(no3)
                if (no1 + no2 + no3) % 10 == 0:
                    sec = sum_list(tmp3)
                    if sec % 10 == 0:
                        return '牛牛'
                    else:
                        return '牛' + str(sec % 10)


def get_haoma_from_sql(issue_no):
    pwd = 'Vp8WlTSsNnsQ1aWibWM='
    db = pymysql.connect('fusion.mysql.polardb.rds.aliyuncs.com', 'dscp', pwd,
                         'dscp', charset='utf8')
    cursor = db.cursor()
    cursor.execute('SELECT lottery_issue_prize_num FROM ds_lottery_issue WHERE lottery_id = (SELECT lottery_id FROM ds_lottery WHERE lottery_name = "五分PK牛牛") AND lottery_issue_no = %s;' % issue_no)
    data = cursor.fetchall()
    try:
        for i in data:
            return list(map(int, i[0].split(',')))
    except:
        print('未获取到开奖号码！')


def gen_num(li):
    group = []
    if len(li) != 10:
        print('开奖号码有问题！')
    else:
        for i in range(6):
            group.append(li[i:i+5])
    return group


while(1):
    try:
        issue_no = int(input('请输入五分pk牛牛的期号：'))
        num = gen_num(get_haoma_from_sql(issue_no))
        for i in range(len(num)):
            result = cul_cat(num[i])
            if result == None:
                result = '无牛'
            if i == 0:
                print('庄家：' + result + '  -  ' + str(num[i]))
            else:
                print('闲' + str(i) + '：' + result + '  -  ' + str(num[i]))
    except:
        print('请重试！')
    print('---------------------------------------')
