from re import S
import socket
import sys

msg = sys.argv[1]
s = socket.socket()
host = socket.gethostname()
port = 12346
s.connect((host, port))
s.send(msg.encode())
rec = s.recv(1024).decode("utf-8")
print(rec)
s.close()
