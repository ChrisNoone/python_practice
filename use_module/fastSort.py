# coding:utf-8


def sort(a):
    if len(a) <= 1:
        return a
    key = a[0]
    a_l = []
    a_r = []
    a_m = []
    for i in a:
        if i < key:
            a_l.append(i)
        elif i > key:
            a_r.append(i)
        elif i == key:
            a_m.append(i)
    a_l = sort(a_l)
    a_r = sort(a_r)
    return a_l+a_m+a_r


init_list = []
for i in range(10):
    init_list.append(int(raw_input("input your number %s/10:"%str(i))))
                       
print "your list is:", init_list
raw_input("Enter to sort...")

a = sort(init_list)
print "after sorted:", a

