import socket
import re

s = socket.socket()
host = "localhost"
port = 58540

s.connect((host, port))
i = 0
a = -1
while i < 10:
    data = s.recv(1024).decode('utf-8')
    print('Received --> ' + data)
    if i == a + 1:
        a += 1
    temp = "Ack: " + str(a)

    s.send(temp.encode('utf-8'))
    i += 1

s.close()