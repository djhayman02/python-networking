#!/usr/bin/python3
#client.py

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#host = socket.gethostname()
host = "192.168.60.68"
port = 2001

try:
    client.connect((host, port)) 
    for num in range(1,20):
        msg = client.recv(1024)
        print(num)
        print (msg.decode('ascii'))
        client.send(msg)
except:
    
    client.connect((host, port)) 
    for num in range(1,20):
        msg = client.recv(1024)
        print(num)
        print (msg.decode('ascii'))
        client.send(msg)


print (msg.decode('ascii'))