from _thread import *
import socket
from time import sleep

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(100)

is_writing = False
content = []
clientList = []
cur_writer = None

def reader(conn, addr):
    for i in content:
        conn.sendto(f'{i[1]}\n'.encode(), addr)

def writer(conn, addr):
    global cur_writer
    while True:
        message = conn.recv(2048).decode().strip()
        print(message)
        if message == 'exit':
            cur_writer = None
            conn.close()
            break
        content.append([f'Writer: {addr}', message])
        print(content)
        broadcast(message)

def broadcast(meassage):
    for i in clientList:
        if i[0] != cur_writer:
            i[0].sendto(f'{meassage}\n'.encode(), i[1])


while True:
    conn, addr = s.accept()
    print(f'Connected to: {addr}')
    conn.sendto('You a reader or writer: '.encode(), addr)
    message = conn.recv(2048).decode().strip()
    print(message == 'reader')
    if message == 'reader':
        start_new_thread(reader, (conn, addr))
        clientList.append([conn, addr])
    elif message == 'writer':
        print('Request for writer: ') 
        if not cur_writer:
            cur_writer = conn
            start_new_thread(writer, (conn, addr))
            clientList.append([conn, addr])
        else:
            conn.sendto('Writer is busy'.encode(), addr)
            sleep(2)
            conn.close()
    print(clientList)