

# This is for the server side TCP 
import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # Creates a socket object for the server
print('Socket Created')

server.bind(("localhost",9999)) # Bind the loopback address to Server and port

server.listen(10) # The number if incoming connections the server will accept
print('Waiting For Connection')

while True: # The while true loop to accept the connection from the client
    client, addr = server.accept() # Accepts connection from any client 
    name = client.recv(1024).decode() # takes the name input from the client and decoded it
    print("Connected with ",addr,name) # prints the clients address and the connected name
    client.send(bytes("Welcome To The Server",'utf-8')) #have to send bytes then the decode format
    client.close() #closes the socket 
