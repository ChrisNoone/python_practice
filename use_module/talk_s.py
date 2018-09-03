# coding:utf-8

from socket import *

HOST = ''
PORT = 21567
ADDR = (HOST,PORT)

server = socket(AF_INET,SOCK_STREAM)
server.bind(ADDR)
server.listen(1)

while True:
    print 'waiting...'
    client,addr = server.accept()
    print 'connected.',addr

    while True:
        
        data_r = client.recv(1024)
        print data_r
        data_s = raw_input('N:>')
        client.send(data_s)
        
    client.close()
