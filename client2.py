#!/usr/bin/python3
#client.py
import socket

def main():
    host = "192.168.60.68"  # Change this to the appropriate host
    port = 2001        # Change this to the appropriate port

    successful_connections = 0
    max_successful_connections = 10

    while successful_connections < max_successful_connections:
        try:
            # Create a socket
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Connect to the server
            client_socket.connect((host, port))

            # Receive data from the server
            received_data = client_socket.recv(1024).decode()
            while received_data:
                if received_data:
                    #Send back the received data
                    client_socket.send(received_data.encode())
                
                    successful_connections += 1
                    print(f"Successful connections: {successful_connections}/{max_successful_connections}")
                    print(f"Received data: {received_data}")
                else:
                    print("No data received. Retrying...")

            # Close the socket
            client_socket.close()
        
        except socket.error as e:
            print(f"Socket error: {e}. Retrying...")

if __name__ == "__main__":
    main()
