from socket import *
import sys

server_host = sys.argv[1]
server_port = sys.argv[2]
filename = sys.argv[3]

try:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    server_port = int(server_port)
    clientSocket.connect(server_host, int(server_port))

    header = "GET " + filename + "HTTP/1.1\r\n\r\n"
    headerBytes = bytes(header, "UTF-8")
    clientSocket.send(headerBytes)
    print (clientSocket.recv(4096))
    clientSocket.close()

except IOError:
    exit(1)


