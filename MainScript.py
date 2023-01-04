#------------------------------------------------------------------------------------------#
                            #From: Hussein Amr Ghorabah
                            #Track : DevOps - Mansoura Branch
                            #CONSOLE APP PROJECT ---- Crowd Funding Project
                            #MAIN PROJECT SCRIPT TO RUN THE PROGRAM
#-------------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------
"""First Step of Project -CROWD FUNDING console app-"""
#-------------------------------------------------------------------------------------

#Importing Libraries------------------------------------------------------------------
from colorama import Fore
import login 
import register
#-------------------------------------------------------------------------------------
print(f"{Fore.LIGHTBLUE_EX}-------------------------------------------------------\n{Fore.RESET}")
print(f"{Fore.CYAN}                     Welcome to\n")
print(f"{Fore.CYAN}               ZX_Crwod_Funding Project\n")
print(f"{Fore.LIGHTBLUE_EX}-------------------------------------------------------{Fore.RESET}")
#Asking user to choose what he want to do --------------------------------------
usrinput = ""
#------------------------------------------------------------------------------------------------
def options():
    print(f"{Fore.LIGHTBLACK_EX}*CHOOSE FIELD NUMBER ----- :{Fore.RESET}")
    options = ("Register-New Account", "Login","End")
    for count, i in enumerate(options, 1):
        print(f"{Fore.CYAN}{count} ----> {i}{Fore.RESET}")
    print(f"{Fore.LIGHTBLACK_EX}--------------------------------------{Fore.RESET}")
#--------------------------------------------------------------------------------------------------

def choose_main_list():
    options()
    global usrinput
    usrinput = input(f"{Fore.BLUE}Your Choice: {Fore.RESET}")
    while True:
        if usrinput.isdigit() and int(usrinput) in [1, 2, 3]:
            usrinput = int(usrinput)
            break
        else:
            print (f"{Fore.RED}*WRONG ENTERY ..... PLEASE ADD ONE NUMBER FROM THE FOLLOWING LIST*{Fore.RESET}")
            options()
            usrinput = input(f"{Fore.BLUE}Your Choice: {Fore.RESET}")
#--------------------------Actions after user Decision---------------------------------------------
#CASE A - User choose to Register -----------------------------------------------------------------
def actions():
    if usrinput == 1 :
        register.registeraction()
    #CASE B - User choose to Login check -----------------------------------------------------------------
    if usrinput == 2:
        login.loginaction()
    #CASE C - User choose to END -----------------------------------------------------------------
    elif usrinput == 3 :
        quit
#--------------------CALLING------------------------------------------------
choose_main_list()
actions()
#------------FINAL VERSION V2.0.1
