
# coding:utf-8
''' % 格式化输出'''
'''
in_put = raw_input("please input your name:")
if in_put != '':
    print "%s is 25" % in_put
print "***hello world***"
'''

'''文件操作'''
'''
import os
# print os.getcwd()

body_file = open(r"C:\Users\imade\Desktop\body.json","r")
s = ''.join(body_file.readlines())
print type(s),s
'''

'''时间操作'''
'''
import time
print time.localtime()
print time.localtime(time.time())
print time.strftime('%Y/%m/%d %H:%M:%S %Z',time.localtime()).decode('gbk').encode('utf-8')
'''

'''lambda python内置函数'''
'''
f = lambda x:x+1
print f(1)
print type(lambda x:x+1(2))
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print filter(lambda x: x % 3 == 0, foo)
print map(lambda x: x * 2 + 10, foo)
print reduce(lambda x, y: x + y, foo)

print range(1,10)
print reduce(lambda x,y:x+y, range(1,101))
'''

'''随机数'''
import random
print random.random()
print random.randint(1,10)