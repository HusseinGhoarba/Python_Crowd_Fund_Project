#------------------------------------------------------------#
            #From: Hussein Amr Ghorabah
            #Track : DevOps - Mansoura Branch
#------------------------------------------------------------#

#-------------------------------------------------------------------------------------
"""First Step of Project -CROWD FUNDING console app-"""
#-------------------------------------------------------------------------------------

#Importing Libraries------------------------------------------------------------------
from colorama import Fore
import login 
import register
#-------------------------------------------------------------------------------------
#Asking user to choose what he want to do --------------------------------------
usrinput = ""
def options():
    options = ("register","login","end")
    global usrinput
    input_message = "Choose an option: \n"
    for index, item in enumerate(options):
        input_message += f"{Fore.BLUE}{index + 1} {item}\n"

    input_message += f"{Fore.MAGENTA}Your Choice: {Fore.RESET}"

    while usrinput.lower() not in options:
        usrinput = input(f"{Fore.LIGHTWHITE_EX}{input_message}{Fore.RESET}")
        
    print(f"{Fore.CYAN}Your choice is : {Fore.GREEN}{usrinput}{Fore.RESET}")
    return usrinput
#--------------------------------------------------------------------------------------------------
#--------------------------Actions after user Decision---------------------------------------------
#CASE A - User choose to Register -----------------------------------------------------------------
def actions():
    if usrinput.lower() == "register":
        register.registeraction()
    #CASE B - User choose to Login check -----------------------------------------------------------------
    if usrinput.lower() == "login":
        login.loginaction()
    #CASE C - User choose to END -----------------------------------------------------------------
    elif usrinput.lower() == "end":
        exit
#--------------------CALLING------------------------------------------------
options()
actions()

