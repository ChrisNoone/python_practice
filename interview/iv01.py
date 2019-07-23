# coding: utf-8
"""
计算上n层楼梯所有的结果
"""


def countsteps(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return countsteps(n-1) + countsteps(n-2) + countsteps(n-3)


# n = int(input('请输入一个数字：'))
# print('结果：%s' % countsteps(n))

def get_stepresult(n):
    result = []
    def detailsteps(n, temp=''):
        num = sum_str(temp)
        if num == n:
            result.append(temp)
            return
        if num > n:
            return
        for i in range(1, 4):
            detailsteps(n, temp+str(i))
    detailsteps(n)
    return result


def sum_str(st):
    n = 0
    for i in st:
        n = n + int(i)
    return n


print(get_stepresult(5))
