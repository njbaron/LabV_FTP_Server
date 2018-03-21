import sys
import socket

print("Welcome to the FTP server!")

if len(sys.argv) != 1:
    print("[ERROR] " + str(sys.argv[0]) + " Incorrect command line arguments")
    exit(1)

server_ip = '127.0.0.1'
server_port = 5005
buffer_size = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((server_ip, server_port))
sock.listen(1)

while True:
    connection, address = sock.accept()
    print("[LOG] " + sys.argv[0] + " Connection from: " + str(address))
    file_name = str(sock.recv(buffer_size)).split(':')[1]
    file = open(file_name, 'wb')
    received_bytes = 0
    while True:
        received = sock.recv(buffer_size)
        if not received:
            break
        received_bytes += len(received)
        file.write(received)
    connection.send(received_bytes)

