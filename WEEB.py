
import os
import platform
import time
import socket
import sys
import datetime



def cd():
    cdcmd = input(">")
    if not os.path.isdir(cdcmd): 
        print('The path specified does not exist, QUITTING!')
        sys.exit()
        


    os.chdir(cdcmd) 

Current_Date = datetime.datetime.today().strftime ('%d-%b-%Y') 

print("login at:",Current_Date)
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

    elif a=="create":  
        createinp= input("name your file>")
        open(createinp,"w+")

    elif a=="write": 
        fileed = input("enter file to write>> ")  
        my_file = open(fileed, "w")
        filetext = input('')
        my_file.write(filetext)
        my_file = open(fileed)

        content = my_file.read()

        my_file.close()

        print(content)

    elif a =="erase": 
        filedel = input("file for deletion> ") 
        os.remove(filedel)
        print("file successfully deleted")

    elif a=="read": 
        fileread = input("file> ")
        filereade =open(fileread, "r")
        print(filereade.read())



    else:
        print("no command found.")


    
            
                
