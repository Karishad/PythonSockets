# client.py
# Kieron Yin
# https://pythontic.com/modules/socket/udp-client-server-example

import socket
import time

print("A python client.py by Kieron")
for pings in range(10):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # For the try catch, in the event the packet is dropped, connect
    client_socket.settimeout(1.0)
    message = b'PING'
    addr = ("127.0.0.1", 65000)

    start = time.time()
    client_socket.sendto(message, addr)
    try:
        data, server = client_socket.recvfrom(1024)
        end = time.time()
        elapsed = end - start
        print(pings, ": sent PING... recieved {}".format(data))
    except socket.timeout:
        print(pings, ": sent PING... Timed Out")