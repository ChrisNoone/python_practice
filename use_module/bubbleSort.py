# coding:utf-8

init_list = []
for i in range(10):
    init_list.append(int(raw_input("input your number %s/10:" % i)))
                       
print "your list is:", init_list
raw_input("Enter to sort...")

a = init_list

for i in range(1, len(a)):
    for j in range(len(a)-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            
print "after sorted:", a
