#!/usr/bin/python3
#scanner.py

import socket
import time
import math

startTime = time.time()

target = input('Please specify the IP that you want to scan: ')
#target_IP = socket.gethostbyname(target)
startPort = input('Please specify the start port that you want to scan: ')
endPort = input('Please specify the end port that you want to scan: ')
scanPronic = input('Please specify the if you want to scan pronic only: (y/N) ')
startPort = int(startPort)
endPort = int(endPort)
print ('Initiating Scan for host: ', target)
openPorts = set()
#pronicPorts = set()
 
# function to check Pronic Number
def pronic_check(n):
    x = (int)(math.sqrt(n))
 
    # Checking Pronic Number by multiplying
    # consecutive numbers
    if (x*(x + 1)== n):
        return True
        #print("true")
    else:
        return False
        #print("False")

def scan():     
    for i in range(startPort, endPort):
        if scanPronic != "y":
            scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            conn = scanner.connect_ex((target, i))
            if(conn == 0):
                #print ('Port %d: OPEN' %(i))
                openPorts.add(i)
            scanner.close()
        else:
            if pronic_check(i):
                scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                conn = scanner.connect_ex((target, i))
                print(f"Pronic ports found {i}")
                if(conn == 0):
                    print ('Port %d: OPEN' %(i))
                    openPorts.add(i)
                scanner.close()

for i in range(1,10):
    scan()

#for i in range(1,71):
#    pronic = i*(i+1)
#    #print(pronic)
#    if pronic > 4000 < 4999:
#        pronicPorts.add(i)


if scanPronic != "y":
    print("Scanned all ports within the range")
else:
    print("Scanned only pronic numbered ports.")
print(openPorts)
endTime = time.time()
totalTime = endTime - startTime
print('Start Time: %s' %(startTime))
print('End Time: %s' %(endTime))
print('Total Time: %s' %(totalTime))