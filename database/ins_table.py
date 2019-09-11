# coding: utf-8

import pymysql


db = pymysql.connect('127.0.0.7', 'root', 'root', 'spider')
cur = db.cursor()
sql = '''insert into employee(first_name,
        last_name, age, sex, income)
        values ('Chris', 'Mohan', 20, 'M', 2000)'''
try:
    cur.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()
