import socket
from socket import *
serverSocket = socket (AF_INET, SOCK_STREAM)
#prepare a server socket
serverSocket.bind(('localhost', 90))
serverSocket.listen(5)

while True:
    #Establish the connection
    print ("Ready to serve..")
    connectionSocket, address = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:], "rb")
        outputdata = f.read()
        #send one http header line into socket
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n')
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i:i+1])
        connectionSocket.send(b'\r\n\r\n')
        connectionSocket.close()
    except IOError:
        #file not found
        connectionSocket.close()




#fill in end
