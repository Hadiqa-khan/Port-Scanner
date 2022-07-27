#!/usr/bin/python3
from socket import *
def port_scanner(PORT):
    
    print(f"[+] SCANNING FOR IP {HOST}")
    for i in PORT:
        if s.connect_ex((HOST,i)):
            print(f"[-] PORT {i} CLOSED")
        else:
            print(f"[+] PORT {i} OPEN")
            print(str(s.recv(1024)).strip('b'))
if __name__=='__main__':
    s = socket(AF_INET,SOCK_STREAM)
    s.settimeout(5)
    HOST = input("ENTER IP TO SCAN : ")
    PORTS = input("ENTER NO OF PORTS TO SCAN SEPARATED BY SPACE: ")
    print('\n')
    PORT = PORTS.split()
    for i in range(len(PORT)):
        PORT[i]=int(PORT[i])
    port_scanner(PORT)
	