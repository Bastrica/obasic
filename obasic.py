# Imports
import os
import time
import sys
import signal
 
# Def
print("\033[1;34;34m \n")
def basicbanner():
 
    print(" ____  _               _      ")
    print("/  __\| |             (_)     ")
    print("| |  || |__   __ _ ___ _  ___ ")
    print("| |  || '_ \ / _` / __| |/ __|")
    print("| |__|| |_) | (_| \__ \ | (__by @bastrica ~ version 2.0 ")
    print("\____/|_.__/ \__,_|___/_|\___|")
    print("")
    print("- !Make Linux easier - For New Users! -")
    print("")
                               
                               
 
def clear_chat():
    print("\n" * 100)                                        
 
# Komande #
clear_chat()
print("Checking for updates.. Please wait!")
time.sleep(0.6)
print("No new updates..")
clear_chat()
def menu():
    print("\033[1;34;34m \n")
    basicbanner()
    print("     [LINUX]                        ")
    print('')
    print(" [1] Check For Updates")
    print(" [2] GitHub Programs")
    print(" [3] Softwares")
    print(" [4] LinuxMint Commands")
    print(" [5] About LinuxMint")
    print(" [6] Credits")
    print(" [7] Update & Upgrade")
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
   
 
 
    if choice == "2": 
        clear_chat()
        basicbanner()
        print("Loading...")
        time.sleep(2)   
        basicbanner()
        print("GitHub Programs \n [1] FACEBOOK-FBI \n [2] BLACKEYE \n [3] INSTA-BRUTE \n [0] MENU ")
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
 
 
   
    if choice == "3":     # SOFTWARES
        clear_chat()
        print("Loading..")
        time.sleep(2)
        clear_chat()
        basicbanner()
        print("Choose software to install \n [1] WINE \n [2] WINE TRICKS \n [3] PHP \n [4] MYSQL-SERVER \n [5] APACHE2 \n [6] PYTHON 3 \n [7] MENU")
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
            os.system('sudo apt-get update')
            os.system('sudo apt-get install python3.6')
            clear_chat()
            basicbanner()
            print("Installed")
            time.sleep(1)
            clear_chat()
            menu()
 
        if choice == "7":
            clear_chat()
            print("Loading Menu...")
            time.sleep(2)
            clear_chat()
            print("Loaded")
            time.sleep(0.3)
            clear_chat()
            menu()
 
 
    if choice == "1":
        clear_chat()
        time.sleep(0.5)
        basicbanner()
        print("Checking for Updates")
        time.sleep(0.5)
        clear_chat()
        basicbanner()
        print("No new updates..")
        time.sleep(1)
        clear_chat()
        print("Loading Menu")
        time.sleep(0.5)
        clear_chat()
        menu()
 
    if choice == "6":
        time.sleep(0.6)
        clear_chat()
        basicbanner()
        print(" Made by Bastrica \n Version 2.0 \n \n Credits: \n xHak9x - for program (fbi) \n \n thelinuxchoice - for program (blackeye & instainsane) \n \n \n [0] Menu")
        choice = input("Enter number: ")
        if choice == 0:
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