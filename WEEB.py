
import os
import platform
import time
import socket
import sys
import datetime

time.sleep(2)
print('''⣇⣿⠘⣿⣿⣿⡿⡿⣟⣟⢟⢟⢝⠵⡝⣿⡿⢂⣼⣿⣷⣌⠩⡫⡻⣝⠹⢿⣿⣷
⡆⣿⣆⠱⣝⡵⣝⢅⠙⣿⢕⢕⢕⢕⢝⣥⢒⠅⣿⣿⣿⡿⣳⣌⠪⡪⣡⢑⢝⣇             
⡆⣿⣿⣦⠹⣳⣳⣕⢅⠈⢗⢕⢕⢕⢕⢕⢈⢆⠟⠋⠉⠁⠉⠉⠁⠈⠼⢐⢕:
⡗⢰⣶⣶⣦⣝⢝⢕⢕⠅⡆⢕⢕⢕⢕⢕⣴⠏⣠⡶⠛⡉⡉⡛⢶⣦⡀⠐⣕⢕
⡝⡄⢻⢟⣿⣿⣷⣕⣕⣅⣿⣔⣕⣵⣵⣿⣿⢠⣿⢠⣮⡈⣌⠨⠅⠹⣷⡀⢱⢕
⡝⡵⠟⠈⢀⣀⣀⡀⠉⢿⣿⣿⣿⣿⣿⣿⣿⣼⣿⢈⡋⠴⢿⡟⣡⡇⣿⡇⡀⢕
⡝⠁⣠⣾⠟⡉⡉⡉⠻⣦⣻⣿⣿⣿⣿⣿⣿⣿⣿⣧⠸⣿⣦⣥⣿⡇⡿⣰⢗⢄
⠁⢰⣿⡏⣴⣌⠈⣌⠡⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣬⣉⣉⣁⣄⢖⢕⢕⢕
⡀⢻⣿⡇⢙⠁⠴⢿⡟⣡⡆⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣵⣵⣿
⡻⣄⣻⣿⣌⠘⢿⣷⣥⣿⠇⣿⣿⣿⣿⣿⣿⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣷⢄⠻⣿⣟⠿⠦⠍⠉⣡⣾⣿⣿⣿⣿⣿⣿⢸⣿⣦⠙⣿⣿⣿⣿⣿⣿⣿⣿⠟
⡕⡑⣑⣈⣻⢗⢟⢞⢝⣻⣿⣿⣿⣿⣿⣿⣿⠸⣿⠿⠃⣿⣿⣿⣿⣿⣿⡿⠁⣠
⡝⡵⡈⢟⢕⢕⢕⢕⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⠿⠋⣀⣈⠙
⡝⡵⡕⡀⠑⠳⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⢉⡠⡲⡫⡪⡪⡣
db   d8b   db d88888b d88888b d8888b
88   I8I   88 88'     88'     88  `8D 
88   I8I   88 88ooooo 88ooooo 88oooY' 
Y8   I8I   88 88~~~~~ 88~~~~~ 88~~~b. 
`8b d8'8b d8' 88.     88.     88   8D 
 `8b8' `8d8'  Y88888P Y88888P Y8888P'

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

    elif a=="create":  
        createinp= input("name your file>")
        open(createinp,"w+")

    #under construction
    
    elif a=="write":
        filename= input("name of file> ")
        f = open(filename,"w")
        filetext = input("> ") 
        f.write(filetext)

        f.close()

        g = open(filename,"r")

        s = g.read()
        print(s)
        g.close()

    elif a=="help":
        print("ls: list files or directories")
        print("\ncd: change your working directory")
        print("\ncd-b: go back one directory")
        print("\nclear: clear da screen")
        print("\ncreate: create a file and name it!")
        print("\nwrite: write in a file!")
        print("\nread: read da file!")
        print("\nerase: delete the file!")
        time.sleep(1)
        print("\nthis project is still under construction 0w0")
        
                

    

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

    if a=="off":
        print("Goodbye WEEB!")
        on = False



    
            
                
