# client should send 10 pings to the server
# client cannot wait forever, should only wait up to 1 second for a reply
    # if there is no reply, assume packet was lost

# Send ping message using UDP (connectionless - do not need to set up connection)

# print response message from the server
# calculate and print RTT in seconds of each packet (in seconds)
# otherwise print Request Timed Out
import socket
from socket import AF_INET, SOCK_DGRAM
from time import sleep
import time

print("         UDP Heartbeat Client")

serverName = '127.0.0.1'

#create the socket (same as server)
clientSocket = socket.socket(AF_INET, SOCK_DGRAM)
#now we have to set the timeout of the socket ** REQUIRED-1sec timeout
clientSocket.settimeout(3)
#create sequence number to send to server
seqNum=0
#run the loop to send pings
print(".....Sending messages every 3 seconds.....")
while True:

    #adjust the message and sequence number
    message = "Sequence No.: " + str(seqNum)

    seqNum+=1

    #send a message to the port (port from server: 12000)
    clientSocket.sendto(message.encode(),(serverName,12000))

    #hold for 3 seconds and send another (every 3 seconds until shut down)
    sleep(3)