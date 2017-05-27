import socket
from time import sleep

###

# DIRECT COPY OF THE ORIGINAL MULTICASTSERVER FILE

###

#researched IP ranges for multicasting: using 224.1.1.1
MCAST_GRP = '224.1.1.1'
#researched port numbers to use, chose a generic one found in example
MCAST_PORT = 5007


#create socket and set socket options
serSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
serSock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255)

#start sending packets every 3 seconds
#while the program is running...
while True:

    #notify of a new packet sent (from server 2)
    print("Server 2: multicast packet sent now")
    #Make the message that which is required in the assignment documentation
    message = "Multicasting Assignment ECE 4436 from Server 2"
    #send the packet
    serSock.sendto(message.encode(), (MCAST_GRP, MCAST_PORT))
    #hold for 3 seconds until sending another one
    sleep(3)