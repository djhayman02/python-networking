#!/usr/bin/python3
#http-sockets.py

import socket

remote_host = "192.168.51.68"
remote_port = 8080
data = b''
for i in range(1,50):
    request = "GET /"+ str(i) + ".html HTTP/1.1\r\nHost: 192.168.51.68\r\n\r\n"

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((remote_host,remote_port))
    client.send(request.encode())
    response = client.recv(4096)
    data += response.decode()
    print(data.decode())