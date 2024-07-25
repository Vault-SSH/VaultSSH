from colorama import Fore, Back, Style
import os
import subprocess

vspath= os.path.join(os.path.expanduser( '~' ), '.config', 'VaultSSH')
tokenpath = os.path.join(vspath, 'tokens')

import os

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def listtokendir():
    for x in os.listdir(tokenpath):
     if x.endswith(".txt"):
         print(Fore.MAGENTA + x.strip(".txt"))

def printp(text):
    print(Fore.MAGENTA + text)

def logo():
    clear_screen()
    printp("██╗   ██╗ █████╗ ██╗   ██╗██╗  ████████╗    ███████╗███████╗██╗  ██╗")
    printp("██║   ██║██╔══██╗██║   ██║██║  ╚══██╔══╝    ██╔════╝██╔════╝██║  ██║")
    printp("██║   ██║███████║██║   ██║██║     ██║       ███████╗███████╗███████║")
    printp("╚██╗ ██╔╝██╔══██║██║   ██║██║     ██║       ╚════██║╚════██║██╔══██║")
    printp(" ╚████╔╝ ██║  ██║╚██████╔╝███████╗██║       ███████║███████║██║  ██║")
    printp("  ╚═══╝  ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝       ╚══════╝╚══════╝╚═╝  ╚═╝")
logo()
printp("[1] | Connect")
printp("[2] | Manage Connections")
printp("[3] | Create New Connection")
printp("[4] | About")
printp("[5] | Help")
print("             ")
print("             ")

ans = input(Fore.MAGENTA + "Selection >  ")
printp("Failed.")
if ans == "1":
    logo()
    printp("Which one do you want to connect to? (Type exact name)")
    listtokendir()
    print("             ")
    print("             ")
    ans = input(Fore.MAGENTA + "Selection >  ")
    ans = ans + ".txt"
    if os.path.isfile(os.path.join(tokenpath, ans)):
     printp("Token found!")
     print(Fore.WHITE + "")
     clear_screen()
     target = os.path.join(tokenpath, ans)
     with open(target) as f:
        command = f.readline().strip('\n')
        
        os.system(command)
        printp("Welcome back!")
    else: 
        printp("Whoops, that file doesn't exist, or couldn't be found. It might be moved or deleted. (Don't mess around with system files!)")
elif ans == "2":
     logo()
     printp("Which one do you want to manage?(Type exact name)")
     listtokendir()
     print("             ")
     print("             ")
     ans = input(Fore.MAGENTA + "Selection >  ")
     ans = ans + ".txt"
     if os.path.isfile(os.path.join(tokenpath, ans)):
         target = os.path.join(tokenpath, ans)
         printp("Token found!")
         logo()
         printp(ans.strip(".txt"))
         print("             ")
         printp("What do you want to do?")
         printp("[1] | Edit")
         printp("[2] | Delete")
         printp("[3] | Rename")
         printp("[4] | View")
         print("             ")
         print("             ")
         ans = input(Fore.MAGENTA + "Selection >  ")
         if ans == "1":
            ans = input(Fore.MAGENTA + "Enter the new command you'd usually use to SSH into the server. >  ")
            f = open(target, "w")
            f.write(ans)
            f.close()
            printp("Edited!")
         if ans == "2":
            os.remove(target)
            printp("Deleted!")
         if ans == "3":
            ans = input(Fore.MAGENTA + "Enter the new name you'd like to use. >  ")
            os.rename(target, os.path.join(tokenpath, ans + ".txt"))
            printp("Renamed!")
         if ans == "4":
            f = open(target)
            f.read()
            f.close()
elif ans == "3":
    logo()
    ans = input(Fore.MAGENTA + "Enter the command you'd usually use to SSH into the server. >  ")
    ans2 = input(Fore.MAGENTA + "What do you want to name the connection? (Short and simple is good!) >  ")
    f = open(os.path.join(tokenpath, ans2 + ".txt"), "a")
    f.write(ans)

# tXbtQjaxi4
# letters in list is glitched





