"""
Author: Nicholas Baron (830278807)
Description: This is a TCP client that sends a file to a server.
The server replies to the client with the number of bytes it received as an error check and confirmation that
it received information.
"""
import sys
import socket
from time import sleep

print("Welcome to the FTP client!\n")

if len(sys.argv) != 3:
    print("[ERROR] " + str(sys.argv[0]) + " Incorrect command line arguments")
    exit(1)

server_ip = sys.argv[1]
server_port = 5005
file_name = sys.argv[2]
buffer_size = 1024
response_size = 20
time_out = 1

file = open(file_name, 'rb')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_ip, server_port))
sock.settimeout(time_out)
sock.send(("File:" + str(file_name)).encode())
sleep(.2)

total_bytes = 0

while True:
    data = file.read(buffer_size)
    if not data:
        break
    sent_bytes = sock.send(data)
    print("[LOG] Sending " + str(sent_bytes) + " bytes.")
    total_bytes += sent_bytes

file.close()

try:
    response = int(str(sock.recv(response_size))[2:-1])
except:
    response = -1
print("[LOG] Sent " + str(total_bytes) + " bytes.")
print("[LOG] Server received " + str(response) + " bytes.")

if total_bytes == response:
    print("[LOG] " + sys.argv[0] + " Transfer Successful!")
else:
    print("[WARNING] " + sys.argv[0] + " Transfer Unsuccessful!")
