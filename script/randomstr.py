# coding: utf-8


import string
import random


def func(slen):
        str = ''
        slist = [random.choice(string.digits + string.ascii_letters + '/') for i in range(slen)]
        str = ''.join(slist)
        return str + '=='
	

print(func(1918))
