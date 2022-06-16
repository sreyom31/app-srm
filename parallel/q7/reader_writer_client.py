from pickletools import read_string1
import socket, sys, select

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
s.connect((host, port))

while True:
    socket_list = [sys.stdin, s]
    read_socket, write_socket, error_socket = select.select(socket_list, [], [])

    for socks in read_socket:
        if socks == s:
            message = socks.recv(2048).decode()
            print(message)
        else:
            message = sys.stdin.readline()
            s.send(message.encode())
