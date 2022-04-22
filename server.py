# server.py
# Kieron Yin
# https://pythontic.com/modules/socket/udp-client-server-example

import socket
import random

localIP     = "127.0.0.1"
localPort   = 65000
bufferSize  = 1024

msgFromServer = "PONG"
bytesToSend = str.encode(msgFromServer)

msgDropped = "PacketDrop"
bytesToSend2 = str.encode(msgDropped)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")

# Listen for incoming datagrams
while(True):
    print("Server is Listening...")
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Recieved PING:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    print(clientMsg)
    print(clientIP)
    # Sending a reply to client
    if(random.randint(0, 9) > 2):
        UDPServerSocket.sendto(bytesToSend, address)
    else:
        UDPServerSocket.timeout
        print("Faking packet drop")
    