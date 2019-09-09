# coding:utf-8

import requests
import json
import string
import pymysql


def get_paychannel(headers):
    url = 'https://fusion.spgamesmanager.net/admin/PayCenterChannel/getPayCenterChannelList'
    res = requests.post(url, headers=headers)
    r = json.loads(res.text)
    li = r['data']['list']
    paychannels = []
    for i in li:
        tmp = (i['payChannelId'], i['name'])
        paychannels.append(tmp)
    return paychannels


def get_paytype(paychannels, headers):
    url = 'https://fusion.spgamesmanager.net/admin/PayCenterChannel/getUsablePayTypeList'
    sqldata = []
    for i in paychannels:
        body = {'channelId': int(i[0])}
        res = requests.post(url, data=body, headers=headers)
        r = json.loads(res.text)
        list = r['data']['list']
        ptype = ''
        paytypeid = ''
        for l in list:
            ptype = ptype + l['name'] + ','
            paytypeid = paytypeid + str(l['payTypeId']) + ','
        info = {
            'channelId': i[0],
            'name': i[1],
            'paytype': ptype.strip(string.punctuation),
            'paytypeid': paytypeid.strip(string.punctuation)
        }
        # print(info)
        sqldata.append(info)
        if len(sqldata) % 20 == 0:
            data_to_database(sqldata)
            sqldata = []


def fix_str(strx):
    """
    处理sql语句中包含单引号和双引号的问题，使用replace方法给引号前加反斜线
    :param strx:
    :return:
    """
    return strx.replace('"', '\\\"').replace("'", "\\\'")


def data_to_database(data):
    conn = pymysql.connect('127.0.0.1', 'root', 'root', 'spider')
    cursor = conn.cursor()
    list_sql = []
    for item in data:
        list_sql.append(dict_to_str(item))
        '''
        sql = 'insert into chouti(`content`, `summary`, `digg`,`discus`, `user`, `time`, `href`, `img`) values ("%s","%s","%s","%s","%s","%s","%s","%s");' % dict_to_str(item)
        sql_str = sql_str + sql + '\n'
        '''
    tem = 'insert into paychannel(`channelId`, `name`, `paytype`,`paytypeid`) values (%s,%s,%s,%s);'
    # %s 不需要再用引号括起来
    cursor.executemany(tem, list_sql)
    conn.commit()


def dict_to_str(data):
    # li = list(data.values())
    # return '"' + '","'.join(li) + '"'
    return tuple(data.values())


if __name__ == '__main__':
    headers = {
        'auth-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOjE5Mywibmlja25hbWUiOiJzdXBlciIsInVzZXJBZ2VudCI6Ik1vemlsbGFcLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdFwvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lXC83Ni4wLjM4MDkuMTMyIFNhZmFyaVwvNTM3LjM2IiwibmVlZFR3b0F1dGgiOjAsImV4cCI6MTU2ODAxMjgwMH0.h1lQIiA3aVDp3kN-FsmKvdc5yIKLaVMfPPT_cttKDBI',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        'cookie': 'PHPSESSID=e85a9cfab72ea23651d9d7781c4a23b8'
    }
    channels = get_paychannel(headers)
    get_paytype(channels, headers)
    # data_to_database(paytype)
