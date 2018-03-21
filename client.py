import sys
import socket

print("Welcome to the FTP client!")

if len(sys.argv) != 3:
    print("[ERROR] " + str(sys.argv[0]) + " Incorrect command line arguments")
    exit(1)

server_ip = sys.argv[1]
server_port = 5005
file_name = sys.argv[2]
buffer_size = 1024
response_size = 20

file = open(file_name, 'rb')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_ip,server_port))
sock.send(("File:" + str(file_name)).encode())

sent_bytes = 0

while file.:
    sent_bytes += sock.send(file.read(buffer_size))

file.close()

response = int(sock.recv(response_size))

if sent_bytes == response:
    print("[LOG] " + sys.argv[0] + " Transfer Successful!")
else:
    print("[WANRNING] " + sys.argv[0] + "Transfer Unsuccessful!")
