#This is for the client side TCP 
import socket

client = socket.socket() # creats a client by binding to the socket 
client.connect(("localhost",9999))# connects to the ip and port binded to the server
name = input("Enter You name") # Extra feature added to show client/server side
client.send(bytes(name,'utf-8')) # client has to send to server in byte format
print(client.recv(1024).decode())# takes the packet to decode it