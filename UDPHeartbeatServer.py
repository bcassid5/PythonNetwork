# We will need the following module to generate randomized lost packets
import random
from socket import *
import time

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('127.0.0.1', 12000))
serverSocket.settimeout(5);

print("UDP Heartbeat Server")
print(".....Waiting for packet delivery from client (5sec timeout).....")

count = 0

while True:

    if count==0:
        # Receive the client packet along with the address it is coming from
        message, address = serverSocket.recvfrom(1024)
        message = message.decode()
        if message != "":
            print("Client at " + str(address) + " is online!")
            print(message)
            count=1
    else:
        # Otherwise, the server responds
        message, address = serverSocket.recvfrom(1024)
        print(message.decode())


serverSocket.close()
print(".....Client is offline!.....")