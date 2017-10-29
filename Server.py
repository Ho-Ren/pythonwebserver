import socket
from socket import *
serverSocket = socket (AF_INET, SOCK_STREAM)
#prepare a server socket
serverSocket.bind(('localhost', 90))
serverSocket.listen(5)

while true:
    #Establish the connection
    print ("Ready to serve..")
    connectionSocket, address = serverSocket.accept()





#fill in end
