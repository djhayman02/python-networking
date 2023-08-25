#!/usr/bin/python3
#client.py

import socket

host = "192.168.51.68"  # Change this to the appropriate host
port = 2002        # Change this to the appropriate port
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect():
    client_socket.connect((host, port))

def rxtx():
    received_data = client_socket.recv(1024)
    # Receive data from the server               
    data = b''
    data += received_data
    for num in range(1,500): #received_data:
        #Send back the received data
        #client_socket.send(received_data)
        try:
        
            received_data = client_socket.recv(1024)
            data += received_data
        except:
            received_data = client_socket.recv(1024)
            data += received_data          
        #successful_connections += 1
        #print(f"Successful connections: {successful_connections}/{max_successful_connections}")
        #print(f"Received data: {data.encode('ascii')}")       
    
    with open("my_file.txt", "wb") as binary_file:
   
        # Write bytes to file
        binary_file.write(data)
try:
    connect()
    rxtx()
except:
    connect()
    rxtx()


