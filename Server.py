from socket import *
serverSocket = socket (AF_INET, SOCK_STREAM)
#prepare a server socket
serverSocket.bind(('localhost', 1026))
serverSocket.listen(5)

while True:
    #Establish the connection
    print ("Ready to serve..")
    connectionSocket, address = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024)
        print("Message: " + str(message))
        if len(message) < 1: continue
        filename = message.split()[1]
        print("Opening file: " + str(filename))
        f = open(filename[1:], "rb")
        outputdata = f.read()
        print ("After reading: " + str(outputdata))
        #send one http header line into socket

        header = "HTTP/1.1 200 OK\r\n\r\n"
        headerBytes = bytes(header, "UTF-8")
        connectionSocket.send(headerBytes)

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i:i+1])
        connectionSocket.send(b'\r\n\r\n')
        connectionSocket.close()
        print("Success")
    except IOError:
        #file not found
        header = "HTTP/1.1 404 Not Found\r\n"
        headerBytes = bytes(header, "UTF-8")
        connectionSocket.send(headerBytes)
        print("file not found")
        connectionSocket.close()

serverSocket.close()




#fill in end
