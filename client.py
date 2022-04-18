# client.py
# Kieron Yin
# https://pythontic.com/modules/socket/udp-client-server-example

import socket

msgFromClient       = "Hello, this is the client"
bytesToSend         = str.encode(msgFromClient)
# Matches to the IP and port of the running server
serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = "Message from Server {}".format(msgFromServer[0])
print(msg)