from re import S
import socket
import sys

command = sys.argv[1]
s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host, port))
s.send(command.encode())
rec = s.recv(1024).decode("utf-8")
print(rec)
s.close()