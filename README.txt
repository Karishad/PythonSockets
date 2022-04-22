1. Open a new terminal -> cd to dir containing project files
2. Run server.py -> 'python3 server.py'
3. Open a new terminal -> cd to dir containing project files
4. Run client.py -> 'python3 client.py'

The client will send 10 packets to the server -> will send the message 'PING'
The server will have a 70% chance to respond with 'PONG'
    If the server does not respond, the client will time out and send another packet