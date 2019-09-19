import socket
import re, uuid

s = socket.socket()
host = socket.gethostname()
host_ip = socket.gethostbyname(host)
des_ip = "8.8.4.4"
str = "Hello World"

for x in range(1,11):
    print("|", host_ip, ':'.join(re.findall('..', '%012x' % uuid.getnode())), x, des_ip, str, "|")