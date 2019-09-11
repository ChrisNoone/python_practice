# coding: utf-8

import pymysql


db = pymysql.connect('127.0.0.1', 'root', 'root', 'spider')

cur = db.cursor()
cur.execute('select version()')
data = cur.fetchone()
print('database version: %s' % data)
db.close()
