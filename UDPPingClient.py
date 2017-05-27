# client should send 10 pings to the server
# client cannot wait forever, should only wait up to 1 second for a reply
    # if there is no reply, assume packet was lost

# Send ping message using UDP (connectionless - do not need to set up connection)

# print response message from the server
# calculate and print RTT in seconds of each packet (in seconds)
# otherwise print Request Timed Out
import socket
from socket import AF_INET, SOCK_DGRAM
import time
import datetime

serverName = '127.0.0.1'

#create the socket (same as server)
clientSocket = socket.socket(AF_INET, SOCK_DGRAM)

#now we have to set the timeout of the socket ** REQUIRED-1sec timeout
clientSocket.settimeout(1)

#create a loop tracker variable
cycleNo = 1

#create variables for min, max, and average RTT's
minTime = 1 #because it will never be less than 1
maxTime = 0 #because time will always be greater than 0
totalTime = 0 #will add all times to this then divide by:
successCount = 0 #number of successful returns

#create variables for packet loss
failCount = 0 #just add to this and divide by 10 to find failed packets

#run the loop to send pings
while cycleNo<=10:

    message = str(cycleNo)+ "  " + str(datetime.datetime.now())

    #start the time
    start = time.time()
    #send a message to the port (port from server: 12000)
    clientSocket.sendto(message.encode(),(serverName,12000))

    #now check for the return messages
    try:
        #recieve from server
        message, address = clientSocket.recvfrom(1024)

        #calc time since start
        timeElapsed = (time.time()-start)
        #print the sequence number and message and RTT
        print(str(cycleNo), "RTT: " + str(timeElapsed) + "s")

        if timeElapsed<minTime:
            minTime=timeElapsed

        if timeElapsed>maxTime:
            maxTime=timeElapsed

        successCount+=1
        totalTime+=timeElapsed

    #but if its longer than one second..
    except socket.timeout:
        #print the cycle number and a timeout notification
        print (str(cycleNo), "Request Timed Out")
        failCount+=1

    #now increment the cycleNo to start again
    cycleNo = cycleNo+1
    #finally close the socket when done
    if cycleNo>10:
        clientSocket.close()


average = totalTime / successCount
failPercent = failCount/10*100
# additionally calculate the min, max, and average RTTs as well as packet loss rate (%) at the end of all pings
print("maximum: " + str(maxTime), "minimum: " + str(minTime), "average: " + str(average))
print("packet loss: " + str(failPercent) + "%")
