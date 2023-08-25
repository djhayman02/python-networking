#!/usr/bin/python3
#scanner.py

import socket
import time

startTime = time.time()

target = input('Please specify the host that you want to scan: ')
target_IP = socket.gethostbyname(target)
startPort = input('Please specify the start port that you want to scan: ')
endPort = input('Please specify the end port that you want to scan: ')
startPort = int(startPort)
endPort = int(endPort)
#print ('Initiating Scan for host: ', target_IP)
     
for i in range(startPort, endPort):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn = scanner.connect_ex((target_IP, i))
    if(conn == 0):
        print ('Port %d: OPEN' %(i))
    scanner.close()

endTime = time.time()
totalTime = endTime - startTime
print('Total Time: %s' %(totalTime))