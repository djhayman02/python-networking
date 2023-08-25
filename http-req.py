#!/usr/bin/python3
#web-client.py
import socket
import requests

url = "http://192.168.51.68:8080/"

data = b''
for i in range(1,50):
    #url = url + str(i) + ".html"
    
    response = requests.get(url + str(i) + ".html")
    data += response.content
print(data)
