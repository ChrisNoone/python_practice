# coding:utf-8

'''冒泡排序'''
def func_sort(s):
    if type(s).__name__ != "list":
        print "please give list!"
    else:
        for j in range(1,len(s)):
            for i in range(len(s)-j):
                if s[i]>s[i+1]:
                    s[i],s[i+1]=s[i+1],s[i]
    return s

'''快速排序'''
def func_fsort(s):
    if len(s) <= 1:
        return s
    key = s[0]
    lt_l = []
    lt_r = []
    lt_m = []
    for i in s:
        if i<key:
            lt_l.append(i)
        elif i>key:
            lt_r.append(i)
        else:
            lt_m.append(i)
    lt_l = func_fsort(lt_l)
    lt_r = func_fsort(lt_r)
    return lt_l+lt_m+lt_r

li = [3,7,2,9,11,4,8]
print func_sort(li)
print func_fsort(li)