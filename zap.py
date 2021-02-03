import os
import platform
import time
import socket
import sys

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print(s.getsockname()[0])

def cd():
    cdcmd = input(">")
    if not os.path.isdir(cdcmd):
        print('The path specified does not exist, QUITTING!')
        sys.exit()
        


    os.chdir(cdcmd)
    

     
while True:
    a = input(">> ")
    if a == "ifconfig":
        get_ip_address()

    
        
    elif a == "ls":
        for i in os.listdir('.'):
            if os.path.isfile(i):
                print('f-',i)

            if os.path.isdir(i):
                print('d-',i)

            if os.path.islink(i):
                print('l-',i)

    elif a == "clear":
        for i in range(70):
            print("\n ")

    elif a=="cd":
        cd()

    elif a=="cd-b":
        os.chdir('..')



    else:
        print("no command found.")

    
            
                
