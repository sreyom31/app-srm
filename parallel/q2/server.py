import socket, _thread

server = socket.socket()

host = socket.gethostname()
port = 12345

server.bind((host, port))

current_turn = 1
totalPlayer = 0
clientList = []

server.listen(5)

def checkValidity(message):
    if message == 'Move' or message == 'Attack' or message == 'Kill' or message == 'capture':
        return True
    return False


colors = ['black', 'white']


def clientThread(conn, addr, num):
    global current_turn
    conn.sendto(f"Welocme Player: {num}\n Your Color is {colors[num-1]}\n".encode(), addr)
    while True:
        message = conn.recv(2048).decode()
        print(message.split()[0])
        if checkValidity(message.split()[0]) and current_turn==num:
            broadcast(message, conn, current_turn)
            if current_turn == 1:
                current_turn = 2
            else:
                current_turn = 1
        elif(current_turn!=num):
            conn.sendto(f"Not Your Turn".encode(), addr)
            print("Wrong Player Trid to Move\n")
        elif not checkValidity(message.split()[0]):
            conn.sendto(f"Invalid Move\n".encode(), addr)
            print("Invalid Move")


def broadcast(message, conn, num):
    for client in clientList:
        if client[0] != conn:
            client[0].sendto(f'Move By Player: {num}\n{message}'.encode(), client[1])

    
while True:
    conn, addr = server.accept()
    print("Connected to :", addr)
    totalPlayer += 1
    if totalPlayer <= 2:
        clientList.append([conn, addr])
        _thread.start_new_thread(clientThread, (conn, addr, totalPlayer))
    else:
        print("Player number exceeded")
        totalPlayer -= 1
        conn.close()
