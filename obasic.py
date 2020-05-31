# Imports
import os
import time
import sys
import signal

def clear_chat():
    print("\n" * 100)  
 
clear_chat()
print("\033[1;37;41m")
print("    -! Warning - This is First Version If you delete this tool !- ")
print("-! All Installed programs with this Tool will be deleted due to bug !-")
print("      -! This bug will be fixed in 1.0 Version of this Tool !-")
print("                   -! Thanks for Support !-")
print("")
print("Loading..")
print("10")
time.sleep(5)
print("5")
time.sleep(2)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(0.5)
# Def
print("\033[1;34;40m \n")
def basicbanner():
 
    print(" ____  _               _      ")
    print("/  __\| |             (_)     ")
    print("| |  || |__   __ _ ___ _  ___ ")
    print("| |  || '_ \ / _` / __| |/ __|")
    print("| |__|| |_) | (_| \__ \ | (__by @bastrica ~ version 0.5 ")
    print("\____/|_.__/ \__,_|___/_|\___|")
    print("")
    print("- !Make Linux easier - For New Users! -")

                               
                               
 
def clear_chat():
    print("\n" * 100)                                        
 
# Komande #
clear_chat()
print("Checking for updates.. Please wait!")
time.sleep(2)
print("No new updates..")
time.sleep(1)
clear_chat()
def menu():
    print("\033[1;34;40m \n")
    basicbanner()
    print("     [LINUX]                        ")
    print('')
    print(" [1] GitHub Programs")
    print(" [2] Softwares")
    print(" [3] Credits")
    print(" [4] Update & Upgrade")
    print(" [8] Exit")
    while 5:
        try:
            choicer = int(input("\n Enter number: "))
            break
        except ValueError:
            time.sleep(0.9)
            clear_chat()
            basicbanner()
            print("Please enter number!")
            time.sleep(1)
            clear_chat()
            menu()
 
    choice = str(choicer)
   
 
    if choice == "1": 
        clear_chat()
        basicbanner()
        clear_chat()
        print("Loading...")
        time.sleep(2)   
        clear_chat()
        basicbanner()
        print("GitHub Programs \n [1] FBI Facebook \n [2] Blackeye \n [3] Insta-Brute \n [0] Menu ")
        choice = input("Choose option: ")
 
 
        if choice == "1":
            os.getenv("HOME")
            os.system('git clone https://github.com/xHak9x/fbi.git')
            clear_chat()
            print("Installed & saved in /OBasic/fbi")
            time.sleep(1)
            clear_chat()
            menu()
 
        if choice == "2":
            os.system('git clone https://github.com/thelinuxchoice/blackeye')
            print("Installed & saved in /OBASIC/blackeye & Make [blackeye] executable")
            clear_chat()
            time.sleep(1)
            clear_chat()
            menu()
       
        if choice == "3":
            os.system('git clone https://github.com/thelinuxchoice/instainsane')
            print("Installed & saved in /OBasic/instainsane & Make [instainsane] executable")
            clear_chat()
            time.sleep(1)
            clear_chat()
            menu()
 
        if choice == "0":
            clear_chat()
            print("Loading")
            time.sleep(2)
            clear_chat()
            print("Loaded")
            time.sleep(0.1)
            clear_chat()
            menu()
 
        else:
            clear_chat()
            print("Enter another number!")
            time.sleep(1)
            clear_chat()
            menu()
 
 
   
    if choice == "2":     # SOFTWARES
        clear_chat()
        print("Loading..")
        time.sleep(2)
        clear_chat()
        basicbanner()
        print("Choose software to install \n [1] Wine \n [2] Wine Tricks \n [3] Php \n [4] MySql - Servr \n [5] Apache2 \n [6] Python 3 \n [0] Menu")
        choice = input("Choose option: ")
 
        if choice == "1":
            os.getenv("HOME")
            os.system('sudo dpkg --add-architecture i386')
            os.system('wget -nc https://dl.winehq.org/wine-builds/winehq.key')
            os.system('sudo apt-key add winehq.key')
            clear_chat()
            basicbanner()
            print("Installed")
            time.sleep(1)
            clear_chat()
            menu()
       
        if choice == "2":
            os.getenv("HOME")
            os.system('wget  https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks')
            os.system('chmod +x winetricks')
            clear_chat()
            basicbanner()
            print("Installed")
            time.sleep(1)
            clear_chat()
            menu()
       
        if choice == "3":
            os.getenv("HOME")
            os.system('sudo apt-get install apache2')
            os.system('sudo apt-get install mysql-server')
            os.system('sudo apt-get install php libapache2-mod-php')
            clear_chat()
            basicbanner()
            print("Installed")
            time.sleep(1)
            clear_chat()
            menu()
 
        if choice == "4":
            os.system('sudo apt-get install mysql-server')
            os.system('sudo mysql_secure_installation')
            clear_chat()
            basicbanner()
            print("Installed")
            time.sleep(1)
            clear_chat()
            menu()
 
        if choice == "5":
            os.getenv("HOME")
            os.system('sudo apt-get install apache2')
            clear_chat()
            basicbanner()
            print("Installed")
            time.sleep(1)
            clear_chat()
            menu()
 
 
        if choice == "6":
            os.getenv("HOME")
            os.system('sudo apt-get install software-properties-common')
            os.system('sudo add-apt-repository ppa:deadsnakes/ppa')
            os.system('sudo apt-get install python3.6')
            clear_chat()
            basicbanner()
            print("Installed")
            time.sleep(1)
            clear_chat()
            menu()
 
        if choice == "0":
            clear_chat()
            print("Loading Menu...")
            time.sleep(2)
            clear_chat()
            print("Loaded")
            time.sleep(0.3)
            clear_chat()
            menu()
 
    if choice == "3":
        time.sleep(0.6)
        clear_chat()
        basicbanner()
        print(" Made by Bastrica \n Version 0.5 \n \n Credits: \n aqamarine228 \n \n [0] Menu")
        choice = input("Enter number: ")
        if choice == "0":
            clear_chat()
            print("Loading..")
            time.sleep(1)
            clear_chat()
            menu()
 
 
    if choice == "7":
        print("Installing")
        time.sleep(2)
        os.system('apt update && apt upgrade')
        clear_chat()
        time.sleep(2)
        print("Installed")
        time.sleep(0.3)
        menu()
 
    if choice == "8":
        clear_chat()
        time.sleep(0.5)
        basicbanner()
        print("Exiting.. please wait & don't turn of your pc!")
        time.sleep(2)
        clear_chat()
        basicbanner()
        os.kill(os.getppid(), signal.SIGHUP)
 
    else:
        print("This option doesn't exist, please enter another one!")
        time.sleep(1)
        clear_chat()
        menu()
 
menu()
