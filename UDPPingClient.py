# UDPPingerServer.py
# We will need the following module to generate randomized lost packets
import random
from socket import *
import time

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
noPings = 100;
destination = ("127.0.0.1",12000);
# Open Nebula Destination
dest_open_nebula = ("10.0.0.1",12000);
port = "1024";
mess = "Boo!"
for ping in range(noPings):
    #Getting the current time
    messageSendTime = time.time() * 1;
    # Printing ping message time is in ms.
    print("Ping " + str(ping) + " " + str(messageSendTime));
    # Creating client socket
    clientSocket = socket(AF_INET, SOCK_DGRAM);
    # Setting a timeout to stop waiting for the packet to be recieved if its lost.
    clientSocket.settimeout(1);
    # Binding the socket to localhost port 1024
    clientSocket.bind(('', 1024))
    # Sending the message to the esrver.
    clientSocket.sendto(mess.encode(),destination);
    # Try to recieve a message
    try:
        # Keep asking to recieve a message from teh server
        message, address = clientSocket.recvfrom(12000)
        # Get the recieve time
        recieveTime = time.time() * 1
        # Print RTT and other debugging information
        print("DEBUG: Init = " + str(messageSendTime) + " Final = " + str(recieveTime));
        print("Message Recieved: " + message.decode("utf-8") + " RTT = " + str(recieveTime - messageSendTime));
    # Packet is most likely lost if there is a timeout. Timeout has been set above of 1 second.
    except timeout:
        print("Request timed out.")