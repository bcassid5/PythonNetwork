
from socket import *
import socket
import sys

# Create a server socket, bind it to a port and start listening
# fill in start

#create an INET, STREAMing socket
tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind the socket to a public host,
# and a well-known port
tcpSerSock.bind((socket.gethostname(), 12000))
#become a server socket
tcpSerSock.listen(5)
#fill in ends

while 1:
    # Start receiving data from the client
    print( 'Ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print ('Received a connection from:', addr)
    message = tcpCliSock.recv(2048)
    if str(message) != '':
            #, encoding='utf8' ) != '':             NOTE: this line doesnt seem to work on mac terminal? removed and it ran fine
        print (message)

    # Extract the filename from the given message
        print (message.split()[1])
        file1 = str(message)
                     #, encoding='utf8' )           NOTE: this line doesnt seem to work on mac terminal? removed and it ran fine
        filename = file1.split()[1].split("/")[1]
        print (filename)
        fileExist = "false"
        filetouse = "/" + filename
        print (filetouse)
        try:
        # Check whether the file exist in the cache
            f = open(filetouse[1:], "rb")
            outputdata = f.readlines()
            fileExist = "true"

        # ProxyServer finds a cache hit and generates a response message
        
            tcpCliSock.send(bytes("HTTP/1.0 200 OK\r\n",'utf-8'))
            tcpCliSock.send(bytes("Content-Type:text/html\r\n",'utf-8'))
        # Fill in start.

            for i in range(0, len(outputdata)):
                tcpCliSock.send(outputdata[i])
        # Fill in end.
            f.close()
            print ('Read from cache')

    # Error handling for file not found in cache
        except IOError:
            if fileExist == "false":
            # Create a socket on the proxy server
                c = socket.socket(AF_INET, SOCK_STREAM)         #NOTE: had to add socket. to the start of this to make it work
                hostn = filename.replace("www.", "", 1)
                print (hostn)
                try:
                # Connect to the socket to port 80
                
                # fill in start
                    c.connect((hostn, 80))
                #fill in ends
            
                # Create a temporary file on this socket and ask port 80 for the file requested by the client
                    fileobj = c.makefile('rwb')
                    string1 = "GET " + "http://" + filename + " HTTP/1.0\n\n"
                    naming = bytes(string1,'utf-8')
                    c.send(naming)
                    fileobj.write(naming)
               
                # Read the response into buffer
                
                # fill in start
                    buff = fileobj.readlines()
                #fill in ends

                # Create a new file in the cache for the requested file.
                # Also send the response in the buffer to client socket and the corresponding file in the cache
                    tmpFile = open("./" + filename,"wb")
                    
                # Fill in start.
                    for i in range(0, len(buff)):
                        tmpFile.write(buff[i])
                        tcpCliSock.send(buff[i])
                # Fill in end.
                
                    tmpFile.close()
                except:
                    print ("Illegal request")
            else:
            # HTTP response message for file not found
                
                # Fill in start.
                tcpCliSock.send(bytes("HTTP/1.0 404 NOT FOUND\r\n", 'utf-8'))
                print("File Not Found")
                # Fill in end.

    # Close the client and the server sockets
    tcpCliSock.close()
    
# Fill in start.
tcpSerSock.close()
# Fill in end.
    
