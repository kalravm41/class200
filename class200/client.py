import socket
from threading import Thread

nickname = input('Choose Your Nickname?: ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipAddress = '127.0.0.1'
port = 8000

client.connect((ipAddress,port))

print('CONNECTED TO THE SERVER !!!')

def Recieve():
    while True:
        try:
            message = client.recv(2048).decode('UTF-8')

            if message == nickname:
                client.send(nickname.encode('UTF-8'))
            else:
                print(message)    
        except:
            print('An Error Occured !!!')    
            client.close()

            break

def write1():
    while True:
        message = f"{nickname}:{input('')}"
        client.send(message.encode('UTF-8'))

        RecieveThread = Thread(target=Recieve)
        RecieveThread.start()
        
        WriteThread = Thread(target=write1)
        WriteThread.start()

if '__name__' ==  '__main__':
    Recieve()
            