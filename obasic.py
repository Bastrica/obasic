# Imports
import os

# Def
def basicbanner():
    print("   ____  ____           _____ _____ _____ ")
    print("  / __ \|  _ \   /\    / ____|_   _/ ____|")
    print(" | |  | | |_) | /  \  | (___   | || |     ")
    print(" | |  | |  _ < / /\ \  \___ \  | || |     ")
    print(" | |__| | |_) / ____ \ ____) |_| || |____ ")
    print("  \____/|____/_/    \_\_____/|_____\_____|")
    print("")
    print("")

def clear_chat():
    print("\n" * 100)                                         

# Komande #
def menu():
    basicbanner()
    print(" [1] Info \n [2] GitHub Programs  \n [3] Softwares \n [4] SystemCommands")
    choice = input("Enter number: ")

    if choice == 1:
        basicbanner()
        clear_chat()
        print("Program by Bastrica \n Version 0.1 \n Updates Soon \n Enter 00 To go in Menu")
        choice = input("OB: Enter number: ")
        if choice == 00:
            clear_chat()
            menu()
   
        


    if choice == 2:     # GITHUB PROGRAMS
        clear_chat()
        basicbanner()
        print("GitHub Programs \n [1] FBI(facebookBot) \n [2] BLACKEYE \n [3] INSTAINSTANE \n [4] updateSoon ")
        choice = input("Choose option: ")

        if choice == 1:
            os.getenv("HOME")
            os.system('apt update && apt upgrade')
            os.system('apt install git python2')
            os.system('git clone https://github.com/xHak9x/fbi.git')
            os.system('pip2 install -r requirements.txt')
            print("Installed & saved in /Desktop/OBasic/fbi")

        if choice == 2:
            os.system('git clone https://github.com/thelinuxchoice/blackeye')
            print("Installed & saved in /Desktop/OBASIC/blackeye")
        
        if choice == 3:
            os.system('git clone https://github.com/thelinuxchoice/instainsane')
            os.system('chmod +x instainsane.sh')

        else:
            print("Enter another number!")
        
   
    if choice == 3:     # SOFTWARES
        clear_chat()
        basicbanner()
        print("Choose software to install \n [1] WINE \n [2] WINE TRICKS \n [3] PHP \n [4] MYSQL-SERVER \n [5] APACHE2 \n [6] PYTHON 3 \n [7] None")
        choice = input("Choose option: ")

        if choice == 1:
            os.getenv("HOME")
            os.system('sudo dpkg --add-architecture i386')
            os.system('wget -nc https://dl.winehq.org/wine-builds/winehq.key')
            os.system('sudo apt-key add winehq.key')
            print("Installed")
        
        if choice == 2:
            os.getenv("HOME")
            os.system('wget  https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks')
            os.system('chmod +x winetricks')
            print("Installed")
        
        if choice == 3:
            os.getenv("HOME")
            os.system('sudo apt-get install apache2')
            os.system('sudo apt-get install mysql-server')
            os.system('sudo apt-get install php libapache2-mod-php')
            print("Installed")

        if choice == 4:
            os.system('sudo apt-get install mysql-server')
            os.system('sudo mysql_secure_installation')

        if choice == 5:
            os.getenv("HOME")
            os.system('sudo apt-get install apache2')

        if choice == 6:
            os.getenv("HOME")
            os.system('sudo apt-get install software-properties-common')
            os.system('sudo add-apt-repository ppa:deadsnakes/ppa')
            os.system('sudo apt-get update')
            os.system('sudo apt-get install python3.6')

    if choice == 4:     # SYSTEM COMMANDS
        clear_chat()
        basicbanner()
        print("SystemComands \n [1] Update \n [2] Upgrade \n [3] Disks \n [4] TurnOff PC \n [5] Reboot \n  [6] Ping")

        if choice == 1:
            os.system('sudo apt-get update')

        if choice == 2:
             os.system('sudo apt-get upgrade')

        if choice == 3:
            os.system('sudo fdisk -l')

        if choice == 4:
            os.system('sudo poweroff')

        if choice == 5:
            os.system('sudo reboot')

        if choice == 6:
            os.system('ping www.pornhub.com')

        os.system('exit')
menu()


