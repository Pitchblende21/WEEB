import os
import platform
import time
import socket
import sys
import datetime
from os import path

time.sleep(2)
print('''
⠀⠀  ⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀
⠀⠀⠀⣴⠿⠏⠀⠀⠀⠀⠀⠀⢳⡀⠀⡏⠀⠀⠀⠀⠀⢷
⠀⠀⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀⠀⠀ ⡇
⠀⠀⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿⠀⣸⠀⠀OK⠀ ⡇
⠀⠀⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀⣿⠀⢹⠀⠀⠀⠀⠀ ⡇
⠀⠀⠙⢿⣯⠄⠀⠀⠀⢀⡀⠀⠀⡿⠀⠀⡇⠀⠀⠀⠀⡼
⠀⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀⠀⠘⠤⣄⣠⠞⠀
⠀⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀
⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀
⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀⠀⣄⢸⠀⠀⠀⠀⠀⠀
⣿⣿⣧⣀⣿………⣀⣰⣏⣘⣆⣀

db   d8b   db d88888b d88888b d8888b
88   I8I   88 88'     88'     88  `8D 
88   I8I   88 88ooooo 88ooooo 88oooY' 
Y8   I8I   88 88~~~~~ 88~~~~~ 88~~~b. 
`8b d8'8b d8' 88.     88.     88   8D 
 `8b8' `8d8'  Y88888P Y88888P Y8888P  v.1.2

''')


def cd():
    cdcmd = input(">")
    if not os.path.isdir(cdcmd): 
        print('The path specified does not exist, QUITTING!')
        sys.exit()
        


    os.chdir(cdcmd) 

Current_Date = datetime.datetime.today().strftime ('%d-%b-%Y') 

print("login at:",Current_Date,"input help for a list of commands")
on = True
     
while on == True:
    a = input(">> ") 

    
    if a == "ls":
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

    elif a =="Aaronsoftword":
        
        file_path = input("\nChoose file: ")

        if path.exists(file_path):
            print("\n\tFile already exists!")
            ans = input("\nDo you want to use this file? (y/n)\n-> ")

            if ans == 'y' or ans == 'Y':
                file = open(file_path, "a")
                ans = input("\nDo you want to erase all content? (y/n)\n-> ")

                if ans == 'y' or ans == 'Y':
                    print("\n\tErasing...\n")
                    file.seek(0)
                    file.truncate()

                else:
                    pass

            else:
                exit()

        else:
            print("\n\tCreating new file...\n")
            file = open(file_path, "a")

        print("\nPress RETURN to start a new line.\nPress Ctrl + C to save and close.\nPress command z for backspace.\n\n")
    
        line_count = 1

        while line_count > 0:
            try:
                line = input("\t" + str(line_count) + " ")
                file.write(line)
                file.write('\n')
                line_count += 1
            except KeyboardInterrupt:
                print("\n\n\tClosing...")
                break

        file.close()

        

    elif a=="help":
        print("ls: list files or directories")
        print("\ncd: change your working directory")
        print("\ncd-b: go back one directory")
        print("\nclear: clear da screen")
        print("\nAaronsoftword:text editor ")
        
        print("\nread: read da file!")
        print("\nerase: delete the file!")
        print("\nbye: say bye to WEEB")
        print("\nANS: network scan")
        time.sleep(1)
        print("\nthis project is still under construction 0w0")
        
                

    

    elif a =="erase":
        try:
            filedel = input("file for deletion> ") 
            os.remove(filedel)
            print("file successfully deleted")
        except FileNotFoundError:
            print("sry man, that file doesn't exist XD")

    elif a=="read": 
        try:
            fileread = input("file> ")
            filereade =open(fileread, "r")
            print(filereade.read())
        except FileNotFoundError:
            print("sorry, that isn't a file UwU")
        


    


    elif a =="bye":
        print("bye weeb UwU")
        time.sleep(1)
        sys.exit()

    elif a =="ANS":
        print("still under construction")
        
    else:
        print("no command found.")

    
            
                

