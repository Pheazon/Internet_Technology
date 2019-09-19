import socket
import re
import random

s = socket.socket()
host = "localhost"
port = 58544

s.connect((host, port))
i = 0

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
        print(totalData)
        print("\n")
        dataOne, dataTwo, dataThree, dataFour, dataFive = totalData.split('|')
        print("DATAONE IS " + dataOne)
        dataReceived, ackNum = dataOne.split(':')
        print("DATA RECEIVED IS " + dataReceived + " DATA ACKNUM IS " + str(ackNum))
        if (dropPacket == 0):
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataTwo.split(':')
            sentData += (dataReceived + ":1 , ")
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataThree.split(':')
            sentData += (dataReceived + ":2 , ")
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataFour.split(':')
            sentData += (dataReceived + ":3 , ")
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataFive.split(':')
            sentData += (dataReceived + ":4 , ")

            sentData += (dataReceived + ":0 , ")
        elif (dropPacket == 1):
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataTwo.split(':')
            sentData += (dataReceived + ":0 , ")
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataThree.split(':')
            sentData += (dataReceived + ":2 , ")
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataFour.split(':')
            sentData += (dataReceived + ":3 , ")
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataFive.split(':')
            sentData += (dataReceived + ":4 , ")

            sentData += (dataReceived + ":1 , ")
        elif (dropPacket == 2):
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
            sentData += (dataReceived + ":3 , ")
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataFive.split(':')
            sentData += (dataReceived + ":4 , ")

            sentData += (dataReceived + ":2 , ")
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
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataFive.split(':')
            sentData += (dataReceived + ":4 , ")

            sentData += (dataReceived + ":3 , ")
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

            sentData += (dataReceived + ":4 , ")

        print('Received --> ' + sentData)
        print("ACK IS " + str(a))
        temp = str(a)
        s.send(temp.encode('utf-8'))
        i += 1
    elif (i == 1):
        dropPacket = random.randint(5, 9)
        a = Ack
        totalData = ""
        sentData = ""
        while totalData.count('|') < 4:
            data = s.recv(1024).decode('utf-8')
            totalData += data
        dataOne, dataTwo, dataThree, dataFour, dataFive = totalData.split('|')
        dataReceived, ackNum = dataOne.split(':')
        print("DATA RECEIVED IS " + dataReceived + " DATA ACKNUM IS " + str(ackNum))
        if (dropPacket == 5):
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataTwo.split(':')
            sentData += (dataReceived + ":6 , ")
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataThree.split(':')
            sentData += (dataReceived + ":7 , ")
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataFour.split(':')
            sentData += (dataReceived + ":8 , ")
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataFive.split(':')
            sentData += (dataReceived + ":9 , ")

            sentData += (dataReceived + ":5 , ")
        elif (dropPacket == 6):
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataTwo.split(':')
            sentData += (dataReceived + ":5 , ")
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataThree.split(':')
            sentData += (dataReceived + ":7 , ")
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataFour.split(':')
            sentData += (dataReceived + ":8 , ")
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataFive.split(':')
            sentData += (dataReceived + ":9 , ")

            sentData += (dataReceived + ":6 , ")
        elif (dropPacket == 7):
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataTwo.split(':')
            sentData += (dataReceived + ":5 , ")
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataThree.split(':')
            sentData += (dataReceived + ":6 , ")
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataFour.split(':')
            sentData += (dataReceived + ":8 , ")
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataFive.split(':')
            sentData += (dataReceived + ":9 , ")

            sentData += (dataReceived + ":7 , ")
        elif (dropPacket == 8):
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataTwo.split(':')
            sentData += (dataReceived + ":5 , ")
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataThree.split(':')
            sentData += (dataReceived + ":6 , ")
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataFour.split(':')
            sentData += (dataReceived + ":7 , ")
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataFive.split(':')
            sentData += (dataReceived + ":9 , ")

            sentData += (dataReceived + ":8 , ")
        elif (dropPacket == 9):
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataTwo.split(':')
            sentData += (dataReceived + ":5 , ")
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataThree.split(':')
            sentData += (dataReceived + ":6 , ")
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataFour.split(':')
            sentData += (dataReceived + ":7 , ")
            if (a + 1) == int(ackNum):
                a += 1
            dataReceived, ackNum = dataFive.split(':')
            sentData += (dataReceived + ":8 , ")

            sentData += (dataReceived + ":9 , ")

        print('Received --> ' + sentData)
        print("ACK IS " + str(a))
        temp = str(a)
        s.send(temp.encode('utf-8'))
        i += 1
s.close()