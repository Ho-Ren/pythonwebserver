from socket import *
import threading

class myThread(threading.Thread):

    def __init__(self, connection, address):
        threading.Thread.__init__(self)
        self.connectionSocket = connection
        self.address = address
    def run(self):
        while True:
            try:
                message = connectionSocket.recv(1024)
                if len(message) < 1: continue
                filename = message.split()[1]
                f = open(filename[1:], "rb")
                outputdata = f.read()
                # send one http header line into socket
                header = "HTTP/1.1 200 OK\r\n\r\n"
                headerBytes = bytes(header, "UTF-8")
                connectionSocket.send(headerBytes)
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i:i + 1])
                connectionSocket.send(b'\r\n\r\n')
                connectionSocket.close()
                print("Success")
            except IOError:
                # file not found
                header = "HTTP/1.1 404 Not Found\r\n\r\n"
                headerBytes = bytes(header, "UTF-8")
                connectionSocket.send(headerBytes)
                print("file not found")
                connectionSocket.close()


serverSocket = socket (AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost', 80))
serverSocket.listen(5)
threads = []

while True:
    #Establish the connection
    print ("Ready to serve..")
    connectionSocket, address = serverSocket.accept()
    newThread = myThread(connectionSocket, address)
    newThread.start()

    threads.append(newThread)


