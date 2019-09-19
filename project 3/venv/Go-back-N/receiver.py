import socket
import re
import random

s = socket.socket()
host = "localhost"
port = 58543

s.connect((host, port))
i = 0
Ack = 0;

while i < 2:
    if (i == 0):
        dropPacket = random.randint(0, 4)
        Ack = dropPacket
        a = 0
        totalData = ""
        sentData = ""
        while totalData.count('|') < 4:
            data = s.recv(1024).decode('utf-8')
            totalData += data
        dataOne, dataTwo, dataThree, dataFour, dataFive = totalData.split('|')
        dataReceived, ackNum = dataOne.split(':')
        print("DATA RECEIVED IS " + dataReceived + " DATA ACKNUM IS " + str(ackNum))
        if (dropPacket == 0):
            a -= 1
        elif (dropPacket == 1):
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataTwo.split(':')
            sentData += (dataReceived + ":0 , ")
        elif (dropPacket == 2):
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataTwo.split(':')
            sentData += (dataReceived + ":0 , ")
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataThree.split(':')
            sentData += (dataReceived + ":1 , ")
        elif (dropPacket == 3):
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataTwo.split(':')
            sentData += (dataReceived + ":0 , ")
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataThree.split(':')
            sentData += (dataReceived + ":1 , ")
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataFour.split(':')
            sentData += (dataReceived + ":2 , ")
        elif (dropPacket == 4):
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataTwo.split(':')
            sentData += (dataReceived + ":0 , ")
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataThree.split(':')
            sentData += (dataReceived + ":1 , ")
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataFour.split(':')
            sentData += (dataReceived + ":2 , ")
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataFive.split(':')
            sentData += (dataReceived + ":3 , ")

        print('Received --> ' + sentData)
        print("ACK IS " + str(a))
        temp = str(a)
        s.send(temp.encode('utf-8'))
        i += 1
    elif (i == 1):
        dropPacket = random.randint(int(Ack), int(Ack) + 5)
        a = Ack
        totalData = ""
        sentData = ""
        while totalData.count('|') < 4:
            data = s.recv(1024).decode('utf-8')
            totalData += data

        dataOne, dataTwo, dataThree, dataFour, dataFive = totalData.split('|')
        dataReceived, ackNum = dataOne.split(':')
        print("DATA RECEIVED IS " + dataReceived + " DATA ACKNUM IS " + str(ackNum))
        if (dropPacket == int(Ack)):
            a -= 1
        elif (dropPacket == int(Ack) + 1):
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataTwo.split(':')
            sentData += str(dataReceived + str(Ack) + ",")
        elif (dropPacket == int(Ack) + 2):
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataTwo.split(':')
            sentData += str(dataReceived + str(Ack) + ",")
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataThree.split(':')
            sentData += str(dataReceived + str(int(Ack + 1)) + ",")
        elif (dropPacket == int(Ack) + 3):
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataTwo.split(':')
            sentData += str(dataReceived + str(Ack) + ",")
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataThree.split(':')
            sentData += str(dataReceived + str(int(Ack + 1)) + ",")
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataFour.split(':')
            sentData += str(dataReceived + str(int(Ack + 2)) + ",")
        elif (dropPacket == int(Ack) + 4):
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataTwo.split(':')
            sentData += str(dataReceived + str(Ack) + ",")
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataThree.split(':')
            sentData += str(dataReceived + str(int((Ack + 1))) + ",")
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataFour.split(':')
            sentData += str(dataReceived + str(int((Ack + 2))) + ",")
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataFive.split(':')
            sentData += str(dataReceived + str(int((Ack + 3))) + ",")

        print('Received --> ' + sentData)
        print("ACK IS " + str(a))
        temp = str(a)
        s.send(temp.encode('utf-8'))
        i += 1
s.close()