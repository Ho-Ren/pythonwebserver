from socket import *
import sys

server_host = sys.argv[1]
server_port = sys.argv[2]
filename = sys.argv[3]

try:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    server_port = int(server_port)
    clientSocket.connect(("localhost", server_port))
    header = "GET /" + filename + " HTTP/1.1\r\n\r\n"
    headerBytes = bytes(header, "UTF-8")
    clientSocket.send(headerBytes)

    response = clientSocket.recv(1024)
    print(type(response))
    print (response)


    message = ""
    while response:
        response = clientSocket.recv(1024)
        message += str(response)

    print(message)
    clientSocket.close()
except IOError:
    print("ERROR")


