import socket
import time

s = socket.socket()
host = "localhost"
port = 58540

s.bind((host, port))
s.listen(5)
i = 0
print ('Sender ready and is listening')
c, address = s.accept()
while i < 10:
    r = input("Send data -->")
    c.send(((r + ":" + str(i)).encode('utf-8')))
    print(c.recv(1024).decode('utf-8'))
    print("Receiver " + str(address) + " connected")
    i += 1

c.close()