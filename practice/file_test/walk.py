# coding:utf-8
''' 文件遍历 '''

import os

li = []

def walkthrough(s):
    for i in os.listdir(s):
        if os.path.isfile(os.path.join(s,i)):
            if i[-3:] == ".py":
                li.append(os.path.join(s,i))
        else:
            walkthrough(os.path.join(s,i))

ss = r"D:\workspace"
walkthrough(ss)
df = open("testresult.log","a+")
for i in li:
    df.write(i+'\n')
