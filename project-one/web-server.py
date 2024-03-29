#import socket module

from socket import *

import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
serverPort = 8888
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to recieve")

while True:
    # Establish the connection
    print("Ready to serve...")
    connectionSocket, addr = serverSocket.accept()

    try:
            message = connectionSocket.recv(1024).decode()
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()

            # Send one HTTP header line into socket
            header = "HTTP/1.1 200 OK\r\n\r\n"
            connectionSocket.send(header.encode())

            connectionSocket.send(outputdata.encode())
            '''
            # Send the content of the required file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            '''
            connectionSocket.send("\r\n".encode())

            connectionSocket.close()
    except IOError:
        # Send response message for file not found
        message = "HTTP/1.1 404 Not Found\r\n\r\nCouldn't find file\r\n"
        connectionSocket.send(message.encode())

        # Close client socket
        connectionSocket.close()
        break;

serverSocket.close()
sys.exit()

