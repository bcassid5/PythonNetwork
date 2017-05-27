import socket

#researched IP ranges for multicasting: using 224.1.1.1
MCAST_GRP = '224.1.1.1'
#researched port numbers to use, chose a generic one found in example
MCAST_PORT = 5007
#create the new UDP socket, as done before in the other programs such as ping
cliSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
#set the socket options
try:
    cliSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
except AttributeError:
    pass
    #set the socket to the required TTL=255
    cliSock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255)
    cliSock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 1)

#make sure to bind to the IP and port, and set other recommended options
cliSock.bind((MCAST_GRP, MCAST_PORT))
host = socket.gethostbyname(socket.gethostname())
cliSock.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_IF, socket.inet_aton(host))
cliSock.setsockopt(socket.SOL_IP, socket.IP_ADD_MEMBERSHIP,
                   socket.inet_aton(MCAST_GRP) + socket.inet_aton(host))

#now start receiving from the servers!
#run until cancelled
while 1:
    #try to get the socket message and address
    try:
        message, address = cliSock.recvfrom(1024)
    #if there is an error, just say there is an exception for debugging reference
    except socket.error:
        print ('Exception')
    #print the information as required
    print ("Client 1: Data received from: " + str(address) + "with the message: " + message.decode())