import os

os.chdir("D:\workspace")
name = os.path.basename("D:\workspace")
print os.getcwd()
print name,os.path.isdir(name)

print os.listdir(os.getcwd())
for i in os.listdir(os.getcwd()):
    print i,os.path.isdir(i)

# os.rmdir('os1')
# print os.listdir(os.getcwd())
# os.mkdir('os2')
# os.chdir(os.getcwd()+os.sep+'os2')
# print os.getcwd()