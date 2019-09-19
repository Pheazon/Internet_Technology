import socket
import time

s = socket.socket()
host = "localhost"
port = 58543

s.bind((host, port))
s.listen(5)
i = 0
print ('Sender ready and is listening')
c, address = s.accept()
Ack = 0
#dropPacket = random.randint(0,10)
while i<2:
	if(i==0):
		r=input("Send data -->")
		for j in range (5):
			print("SENDING " + (r+" : "+str(j) + " | "))
			if j != 0:
				c.send(((" | " + r+" : "+str(j)).encode('utf-8')))
			else:
				c.send(((r+" : "+str(j)).encode('utf-8')))
		Ack = c.recv(1024).decode('utf-8')
		print("Ack is " + Ack)
		print("Receiver " + str(address) + " connected")
		i+=1
	elif(i==1):
		r=input("Send data -->")
		for j in range (int(Ack),(int(Ack))+5):
			print("SENDING " + (r+" : "+str(j) + " | "))
			if j != int(Ack):
				c.send(((" | " + r+" : "+str(j)).encode('utf-8')))
			else:
				c.send(((r+" : "+str(j)).encode('utf-8')))
		Ack = c.recv(1024).decode('utf-8')
		print("Ack is " + Ack)
		print("Receiver " + str(address) + " connected")
		i+=1
c.close()