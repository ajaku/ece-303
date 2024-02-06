from socket import *

import sys

num_args = len(sys.argv)

if num_args != 4:
    print("Incorrect number of arguments")
    sys.exit()

serverName = sys.argv[1] 
serverPort = sys.argv[2]

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, int(serverPort)))

print(sys.argv[1])
message = 'GET /' + sys.argv[3] + '\r\n\r\n'
clientSocket.send(message.encode())
response = clientSocket.recv(1024)

while len(response) != 0:
    print(response.decode())
    response = clientSocket.recv(1024)

clientSocket.close()
