# coding: utf-8

import pymysql


db = pymysql.connect('127.0.0.1', 'root', 'root', 'spider')
cur = db.cursor()
cur.execute('drop table if exists employee')
sql = """create table employee (
        first_name char(20) not null,
        last_name char(20),
        age int,
        sex char(1),
        income float)"""
cur.execute(sql)
db.close()
