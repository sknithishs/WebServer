from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', 4040))
serverSocket.listen()

while True:
    connectionSocket, addr = serverSocket.accept()
    connectionSocket.send(bytes('Hello Client','utf-8'))
    connectionSocket.close()
serverSocket.close()
