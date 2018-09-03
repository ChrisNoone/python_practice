# coding:utf-8

def sort(a):
    if len(a) <=1:
        return a
    l = []
    r = []
    m = []
    key = a[0]
    for i in a:
        if i < key:
            l.append(i)
        elif i > key:
            r.append(i)
        elif i == key:
            m.append(i)
    l = sort(l)
    r = sort(r)
    return l+m+r

lis = [23,34,45,78,21,44,9,25,48]
print sort(lis)
