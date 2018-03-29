"""
Author: Nicholas Baron (830278807)
Description: This is a TCP server that receives a file from a client and saves it.
It replies to the client with the number of bytes that is received
"""
import sys
import socket

print("Welcome to the FTP server!\n")

if len(sys.argv) != 1:
    print("[ERROR] " + str(sys.argv[0]) + " Incorrect command line arguments")
    exit(1)

server_ip = '0.0.0.0'
server_port = 5005
buffer_size = 1024
time_out = 1

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((server_ip, server_port))
sock.listen(1)

while True:
    connection, address = sock.accept()
    connection.settimeout(time_out)
    print("[LOG] " + sys.argv[0] + " Connection from: " + str(address))
    file_name = str(connection.recv(buffer_size)).split(':')[1][:-1]
    file = open(file_name, 'wb')
    total_bytes = 0
    while True:
        try:
            received = connection.recv(buffer_size)
            received_bytes = len(received)
            print("[LOG] Received " + str(received_bytes) + " bytes.")
            total_bytes += received_bytes
            file.write(received)
        except:
            break

    print("[LOG] Client sent " + str(total_bytes) + " bytes.")
    print("[LOG] Bytes written to file: " + file_name)
    connection.send(str(total_bytes).encode())
    connection.close()
    file.close()

