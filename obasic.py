# Imports
import os
import time
import sys
import signal
import shutil
def error1():
	print("This option doesn't exist, please enter another one!")


def loadingOption():
	clear_chat()
	print("Loading.. Please Wait!")
	time.sleep(0.7)
	clear_chat()
	basicbanner()

def gotoMenu():
	clear_chat()
	print("Loading Menu.. Please Wait!")
	time.sleep(0.7)
	clear_chat()
	menu()
	
def exit():
    clear_chat()
    print("Exiting..")
    time.sleep(0.5)
    os.system('exit')

def clear_chat():
    print("\n" * 999)  
    
def loading():
	print("5")
	time.sleep(2)
	for i in range(3, 0, -1):
		print(i)
		time.sleep(1)
 

clear_chat()
print("\033[1;37;41m")
print("                                                    -!      Warning - This is First Version        !- ")
print("                                                    -!       Maybe there will be some bugs         !-")
print("                                                    -!    Every bug will be fixed in 1.0 Version   !-")
print("                                                    -!       Report bugs on my github profile      !-")
print("")
print("Loading..")
loading()

# Def
def installedmsg():
	clear_chat()
	print("Saved in Tools Folder!")
	time.sleep(1)
	clear_chat()
	menu()

def validNumber():
    clear_chat()
    print("Please enter a valid number!")
    time.sleep(1)
    clear_chat()

print("\033[1;34;40m \n")
def basicbanner():
 
    print("                                                    ____  _               _      ")
    print("                                                   /  __\| |             (_)     ")
    print("                                                   | |  || |__   __ _ ___ _  ___ ")
    print("                                                   | |  || '_ \ / _` / __| |/ __|")
    print("                                                   | |__|| |_) | (_| \__ \ | (__by @bastrica ~ version 0.5 ")
    print("                                                   \____/|_.__/ \__,_|___/_|\___|")
    print("")          
    print("                                                  - !Make Linux easier - For New Users! -")

                               
                               
 
def clear_chat():
    print("\n" * 100)                                        
 
# Komande #
clear_chat()
print("Checking for updates.. Please wait!")
time.sleep(0.5)
print("No new updates..")
time.sleep(0.5)
clear_chat()
def menu():
    print("\033[1;34;40m \n")
    basicbanner()
    print('')
    print(" [1] GitHub Programs           [7] Learn SQL Injection           [13] Check Sites for Vulnerability          [19] What is MySql")
    print(" [2] Softwares                 [8] Learn Nmap                    [14] Find Admin Login Page                  [20] What is PHP")
    print(" [3] Credits                   [9] What is WireShark             [15] Google Dorks                           [21] How to Sniff Data")
    print(" [4] Do you need Linux?       [10] Learn MetaSploit              [16] What is HTTPS                          [22] How to Catch IP")
    print(" [5] Learn Linux Commands     [11] Learn Penetration Testing     [17] What is HTTP                           [23] Things to Learn for Ethical Hacking")
    print(" [6] Basics of Python         [12] Learn DDOS                    [18] What is WPA                            [24] Is Ethical hacking for You?")
    print("                                                                 [99] Exit")
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
        loadingOption()
        print(" GitHub Programs \n \n [1] FBI - Facebook \n [2] Blackeye \n [3] Insta-Brute \n [0] Menu")
        choice = input("Choose option: ")
 
 
        if choice == "1":
            os.chdir('Tools')
            os.system('git clone https://github.com/xHak9x/fbi.git')
            os.chdir('..')
            installedmsg()
 
        if choice == "2":
            os.chdir('Tools')
            os.system('git clone https://github.com/thelinuxchoice/blackeye')
            os.chdir('..')
            installedmsg()
       
        if choice == "3":
            os.chdir('Tools')
            os.system('git clone https://github.com/thelinuxchoice/instainsane')
            os.chdir('..')
            installedmsg()
 
        if choice == "0":
            clear_chat()
            menu()
 
 
 
   
    if choice == "2": # SOFTWARES
        loadingOption()
        print("Choose software to install \n [1] Wine \n [2] Wine Tricks \n [3] Php \n [4] MySql - Servr \n [5] Apache2 \n [6] Python 3 \n [0] Menu")
        choice = input("Choose option: ")
 
        if choice == "1":
            os.getenv("HOME")
            os.system('sudo dpkg --add-architecture i386')
            os.system('wget -nc https://dl.winehq.org/wine-builds/winehq.key')
            os.system('sudo apt-key add winehq.key')
            installedmsg()
       
        if choice == "2":
            os.getenv("HOME")
            os.system('wget  https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks')
            os.system('chmod +x winetricks')
            installedmsg()
       
        if choice == "3":
            os.getenv("HOME")
            os.system('sudo apt-get install apache2')
            os.system('sudo apt-get install mysql-server')
            os.system('sudo apt-get install php libapache2-mod-php')
            installedmsg()
 
        if choice == "4":
            os.system('sudo apt-get install mysql-server')
            os.system('sudo mysql_secure_installation')
            installedmsg()
 
        if choice == "5":
            os.getenv("HOME")
            os.system('sudo apt-get install apache2')
            installedmsg()
 
 
        if choice == "6":
            os.getenv("HOME")
            os.system('sudo apt-get install software-properties-common')
            os.system('sudo add-apt-repository ppa:deadsnakes/ppa')
            os.system('sudo apt-get install python3.6')
            installedmsg()
 
        if choice == "0":
            loadingOption()
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
 
 
    if choice == "4":
        loadingOption()
        print("\n                                                        Do you really need Linux?")
        print("")
        print("If you think you need Linux and you want to install Linux read this:")
        print("When it comes to stability, no operating system compares to Linux.")
        print("When you download a distro, you don't need to worry about crashes, fatal errors, major bugs, etc..")
        print("All you need to worry about is how much you want to customize your distro.")
        print("")
        print("                                                        Why should we use Linux?")
        print("")
        print("Linux makes very efficient use of the system's resources.")
        print("This allows them to install Linux even on old hardware, this helping in optimal use of all the hardware resources.")
        print("")
        print("                                                        Do Hackers use Linux?")
        print("")
        print("Linux is an extremely popular operating system for hackers.")
        print("First off, Linux's source code is freely available because it is an open source operating system")
        print("This means that Linux is very easy to modify or customize.")
        print("There are countless Linux security distros available that can double as Linux hacking software.")
        print("")
        print("                                                        Is Linux Safe?")
        print("")
        print("Linux is the most secure OS, as its source is open. Anyone can review it and make sure there are no bugs or back doors.")
        print("")
        print("\n[0] Back")
        choice = input("\nEnter Option:")
        if choice == "0":
            gotoMenu()
            
            
    if choice == "5":
        loadingOption()
        print("\n                                                        Learn Linux Commands")
        print("")
        print("sudo - Run command as superuser")
        print("")
        print("cd - Change current directory | example: cd Downloads | This will change your directory")
        print("")
        print("ls - List files in current directory | example: ls | output: Folder1, Folder2, Folder3, etc.")
        print("")
        print("rm - Remove command | example: rm list1 | This will remove list1 from the current directory")
        print("")
        print("mv - Command to move something from one directory to secound | example: mv file1 /home/user/Downloads/ | This will move file1 to Downloads")
        print("")
        print("rmdir - Delete folder from current directory | example: rmdir Folder1 | This will remove Folder1")
        print("")
        print("sudo apt-get update - Command is used to download package information from all current sources")
        print("")
        print("sudo apt-get upgrade - Command to install all avalible packages")
        print("")
        print("\n[0] Back")
        print("")
        choice = input("\nEnter Option: ")
        if choice == "0":
            gotoMenu()
            
            
    if choice == "6"
        loadingOption()
        print("\n                                                        Basics of Python")
        print("")
        print("")
    
 
 
    if choice == "99":
        exit()
 
    else:
        error1()
        time.sleep(1)
        clear_chat()
        menu()
        
menu()
