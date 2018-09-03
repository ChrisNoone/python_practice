import os

path2 = r"d:\workspace\python\Etekcity\file_test\os2"
# print type(path2),path2
# print type(os.getcwd()),os.getcwd()
# print type(os.listdir(path2)),os.listdir(path2)
for i in os.listdir(path2):
    print i
    print os.path.join(path2,i)
#     print os.path.join(path2,i)
    print os.path.abspath(i)