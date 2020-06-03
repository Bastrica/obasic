# Imports
import os
import time
import sys
import signal
import shutil
def error1():
	print("Please enter a valid number!")


def goBack():
	choice = input("[Click Enter to go Back]")
	if choice == "":
		gotoMenu()



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


print("\033[1;34;40m \n")
def basicbanner():

	print("                                                   $$\       $$\   $$\  $$$$$$\   $$$$$$\  $$\   $$\ ")
	print("                                                   $$ |      $$ |  $$ |$$  __$$\ $$  __$$\ $$ | $$  |")
	print("                                                   $$ |      $$ |  $$ |$$ /  $$ |$$ /  \__|$$ |$$  / ")
	print("                                                   $$ |      $$$$$$$$ |$$$$$$$$ |$$ |      $$$$$  /  ")
	print("                                                   $$ |      $$  __$$ |$$  __$$ |$$ |      $$  $$<   by @bastrica ~ version 0.5 ")
	print("                                                   $$ |      $$ |  $$ |$$ |  $$ |$$ |  $$\ $$ |\$$\  ")
	print("                                                   $$$$$$$$\ $$ |  $$ |$$ |  $$ |\$$$$$$  |$$ | \$$\ ")
	print("                                                   \________|\__|  \__|\__|  \__| \______/ \__|  \__|")
	print("")          
	print("                                                       - !Learn Ethical Hacking & More! -")

							
							

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
	print(" [6] Learn Python Course      [12] Learn DDOS                    [18] What is WPA                            [24] Is Ethical hacking for You?")
	print("                                                                 [99] Exit")
	while 5:
		try:
			choicer = int(input("\n Enter number: "))
			break
		except ValueError:
			time.sleep(0.5)
			clear_chat()
			basicbanner()
			print("Please enter a valid number!")
			time.sleep(1)
			clear_chat()
			menu()

	choice = str(choicer)


	if choice == "1": 
		loadingOption()
		print("")
		print("[1] GithubTool1           [6] GithubTool6           [11] GithubTool11")
		print("[2] GithubTool2           [7] GithubTool7           [12] GithubTool12")
		print("[3] GithubTool3           [8] GithubTool8           [13] GithubTool13")
		print("[4] GithubTool4           [9] GithubTool9           [14] GithubTool14")
		print("[5] GithubTOol5          [10] GithubTool10          [15] GithubTool15")
		print("")
		print("[0] Menu")
		print("")
		choice = input("Choose option: ")


		if choice == "1":
			os.chdir('Tools')
			os.system('')
			os.chdir('..')
			installedmsg()

		if choice == "2":
			os.chdir('Tools')
			os.system('')
			os.chdir('..')
			installedmsg()
	
		if choice == "3":
			os.chdir('Tools')
			os.system('')
			os.chdir('..')
			installedmsg()
			
		if choice == "4":
			os.chdir('Tools')
			os.system('')
			os.chdir('..')
			installedmsg()
			
		if choice == "5":
			os.chdir('Tools')
			os.system('')
			os.chdir('..')
			installedmsg()
			
		if choice == "6":
			os.chdir('Tools')
			os.system('')
			os.chdir('..')
			installedmsg()
			
		if choice == "7":
			os.chdir('Tools')
			os.system('')
			os.chdir('..')
			installedmsg()
			
		if choice == "8":
			os.chdir('Tools')
			os.system('')
			os.chdir('..')
			installedmsg()
			
		if choice == "9":
			os.chdir('Tools')
			os.system('')
			os.chdir('..')
			installedmsg()
			
		if choice == "10":
			os.chdir('Tools')
			os.system('')
			os.chdir('..')
			installedmsg()
			
		if choice == "11":
			os.chdir('Tools')
			os.system('')
			os.chdir('..')
			installedmsg()
			
		if choice == "12":
			os.chdir('Tools')
			os.system('')
			os.chdir('..')
			installedmsg()
			
			
		if choice == "13":
			os.chdir('Tools')
			os.system('')
			os.chdir('..')
			installedmsg()
			
		if choice == "14":
			os.chdir('Tools')
			os.system('')
			os.chdir('..')
			installedmsg()
			
		if choice == "15":
			os.chdir('Tools')
			os.system('')
			os.chdir('..')
			installedmsg()

		if choice == "0":
			gotoMenu()
			




	if choice == "2": # SOFTWARES
		loadingOption()

		if choice == "0":
			loadingOption()
			menu()


	if choice == "3":
		loadingOption()
		print("                                                              Made By @bastricaa")
		print("")
		print("                                                                   Credits:")
		print("                                                                 aqamarine228")
		print("                                                                   spaceman")
		print("                                                                    Crypt0")
		print("")
		print("")
		goBack()

	if choice == "4":
		loadingOption()
		print("\n                                                            Do you really need Linux?")
		print("")
		print("If you think you need Linux and you want to install Linux read this:")
		print("When it comes to stability, no operating system compares to Linux.")
		print("When you download a distro, you don't need to worry about crashes, fatal errors, major bugs, etc..")
		print("All you need to worry about is how much you want to customize your distro.")
		print("")
		print("                                                            Why should we use Linux?")
		print("")
		print("Linux makes very efficient use of the system's resources.")
		print("This allows them to install Linux even on old hardware, this helping in optimal use of all the hardware resources.")
		print("")
		print("                                                            Do Hackers use Linux?")
		print("")
		print("Linux is an extremely popular operating system for hackers.")
		print("First off, Linux's source code is freely available because it is an open source operating system")
		print("This means that Linux is very easy to modify or customize.")
		print("There are countless Linux security distros available that can double as Linux hacking software.")
		print("")
		print("                                                            Is Linux Safe?")
		print("")
		print("Linux is the most secure OS, as its source is open. Anyone can review it and make sure there are no bugs or back doors.")
		print("")
		goBack()
			
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
			
			
	if choice == "6":
		loadingOption()
		print("\n                                                        You Can find Courses Here")
		print("")
		print("https://www.youtube.com/watch?v=rfscVS0vtbw   | By freeCodeCamp.org | I watched this course to learn python")
		print("")
		print("\n[0] Back")
		choice = input("\nEnter Option: ")
		if choice == "0":
			gotoMenu()
			
			
	if choice == "7":
		loadingOption()
		print("\n                                                        Learn Sql Injection")
		print("")
		print("")
		print("\n                                                        What is Sql Injection")
		print("")
		print("A SQL injection attack is when a third party is able to use SQL commands to interfere with back-end databases in ways that they shouldn't be allowed to.")
		print("")
		print("")
		choice = input("\n[0] Back")
		if choice == "0":
			gotoMenu()
		
		
	if choice == "99":
		exit()

	else:
		error1()
		time.sleep(1)
		clear_chat()
		menu()
		
menu()
