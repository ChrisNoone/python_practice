# coding:utf-8

print abs(-9)
print abs(5)

str1 = "my name is NooneLiu"
print str1.capitalize()
print str1.replace('NooneLiu','liuchaochao')
print str1.split(' ')

lis = [0,1,2,3,4,5,6,7,8,9]
print filter(lambda x:x%2==0,lis)
name = ["liu","huang","xiao","gong"]
age = ["24","25","26"]
city = ["guang","huang","xiang","yi"]
print zip(name,age,city)
print map(None,name,age,city)
print reduce(lambda x,y:x+y,range(1,101))

str_add = lambda x,y,z:x+y+z
print "callable(str_add):",callable(str_add)
print str_add("liu","chao","chao")
a = 1
a +=1
print a

tur = (1,2,3,4,5,6)
print list(tur)