import socket
from _thread import *


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

IP_address = socket.gethostname()

Port = 12345

server.bind((IP_address, Port))

server.listen(100)

list_of_clients = []

def clientthread(conn, addr):
    conn.sendto("Welcome".encode(), addr)
    while True:
        message = conn.recv(2048).decode()
        print(message)
        broadcast(message, conn, addr)



def broadcast(message, conn, addr):
	for client in list_of_clients:
		if client[0]!=conn:
			client[0].sendto(f'Message From: {addr}\n{message}'.encode(), client[1])


def remove(connection):
	if connection in list_of_clients:
		list_of_clients.remove(connection)

while True:
    conn, addr = server.accept()
    print("Connected to :", addr)
    list_of_clients.append([conn, addr])
    start_new_thread(clientthread, (conn, addr))

