# coding: utf-8


def func(n):
    if n >= 0:
        n = str(n)[::-1]
    else:
        n = '-' + str(n)[1::-1]
    return n


num = input('请输入一串数字：')
num = int(num)
print(func(num))
