import socket

def server():
    s = socket.socket()
    print('Socket Created')

    s.bind(('localhost',9999))

    s.listen(3)
    print('Waiting For Connection')

    while True:
        c, addr = s.accept()
        print('Connected with ', addr)
        c.send(bytes('Welcome' , 'utf-8'))
server()

def client():
    c = socket.socket()

    c.connect(('localhost',9999))

    print(c.recv(1024).decode())
client()