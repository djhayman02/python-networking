#!/usr/bin/python3
#server.py

import socket 

host = "192.168.51.68"
port = 8080
     
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen(4)
print('Server is listening for incoming connections')
     
while True:
    conn,addr = server.accept()
    print("Connection Received from %s" % str(addr))
    msg = 'Connection Established'+ "\r\n"
    conn.send(msg.encode('ascii'))
    recevied = conn.recv(1024)
    print(recevied.decode('ascii'))
    conn.close()