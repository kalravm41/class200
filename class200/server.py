from os import remove
import socket
from threading import Thread
from typing import Collection

clients = []
nickNames = []
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipAddress = '127.0.0.1'
port = 8000;

# socket.AF_INET represents IPv4
# socket.SOCK_STREAM to create TCP Socket
# socket.SOCK_DGRAM to create UDP Socket
# TCP is slower than UDP


#  ---x---x---x---x---x---x---x---x---x---x---x---x---x---x---  #
def remove(conn):
    if conn in clients:
        clients.remove(Collection) 
#  ---x---x---x---x---x---x---x---x---x---x---x---x---x---x---  #



#  ---x---x---x---x---x---x---x---x---x---x---x---x---x---x---  #
def broadcast(message, conn) :
    for client in clients:
        if(client != conn) :
            try:
                client.send(message.encode('UTF-8'))

            except:
                remove(client)     
#  ---x---x---x---x---x---x---x---x---x---x---x---x---x---x---  #



#  ---x---x---x---x---x---x---x---x---x---x---x---x---x---x---  #
def removeNickname(nm) :
    if nickName in nm:
        nm.remove(nickName)

#  ---x---x---x---x---x---x---x---x---x---x---x---x---x---x---  #




#  ---x---x---x---x---x---x---x---x---x---x---x---x---x---x---  #
def clientThread(conn, addr):
    conn.send('Welcome To This Chat Room'.encode('UTF-8'))  

    while True:
        try:
            message = conn.recv(2048).decode('UTF-8')

            if message :
                print('<' + addr[0] + '>' + message)

                messageToSend = '<' + addr[0] + '>' + message;
                broadcast(messageToSend, conn)

            else :
                remove(conn)   
                removeNickname(nickNames) 

        except:
            continue  
#  ---x---x---x---x---x---x---x---x---x---x---x---x---x---x---  #



server.bind((ipAddress, port))
server.listen()

while True:
    conn, addr = server.accept()
    conn.send('Nickname'.encode('UTF-8'))

    nickName = conn.recv(2048).decode('UTF-8')
    nickNames.append(nickName)

    clients.append(conn);
    message = f"{nickName} Joined"

    print(f"{addr[0]} connected")
    print(message)
    broadcast(message, conn)

    newThread = Thread(target= clientThread, args= (conn, addr))
    newThread.start()     
