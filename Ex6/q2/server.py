import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)
while True:
    c, addr = s.accept()
    print("connection from", addr)
    rec = c.recv(1024).decode("utf-8")
    print(rec)
    c.sendto(rec.upper().encode(), addr)
    c.close()