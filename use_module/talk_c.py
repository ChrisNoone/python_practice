# coding:utf-8

from socket import *

HOST = '192.168.13.54'
PORT = 21567
ADDR = (HOST,PORT)

client = socket(AF_INET,SOCK_STREAM)
client.connect(ADDR)

while True:
    data_s = raw_input('A:>')
    client.send(data_s)
    data_r = client.recv(1024)
    print data_r

client.close()
