#------------------------- RUN ---> MainScript.py --> to run Project---------------------------

import login
from values import Proj_Meta
import json
from colorama import Fore
import constrains as chk
#-------------------------------------------------------------------------------
usermail = login.usr_valid_email
user_input = ""
#--------------------------------------------------------------------------------
#-------------------------------Edit Options FUNCTION--------------------------------------
def search_options():
    print(f"{Fore.LIGHTBLACK_EX}*CHOOSE FIELD NUMBER FOR DELETING ----- :{Fore.RESET}")
    options = ("Project Start Date","Project End Date", "Cancel")
    for count, i in enumerate(options, 1):
        print(f"{Fore.CYAN}{count} ----> {i}{Fore.RESET}")
    print(f"{Fore.LIGHTBLACK_EX}--------------------------------------{Fore.RESET}")
#-------------------------------USER CHOOSE OPTION------------------------------------
def search_list():
    search_options()
    global user_input
    user_input = input(f"{Fore.BLUE}Your Choice: {Fore.RESET}")
    while True:
        if user_input.isdigit() and int(user_input) in [1, 2, 3]:
            user_input = int(user_input)
            break
        else:
            print (f"{Fore.RED}*WRONG ENTERY ..... PLEASE ADD ONE NUMBER FROM THE FOLLOWING LIST*{Fore.RESET}")
            search_options()
            user_input = input(f"{Fore.BLUE}Your Choice: {Fore.RESET}")
            
    return user_input
#--------------------------------------------------------------------------------------------------------

#---------------------------------Core Function OF SEARCHING---------------------------------------------------
def searching(searchvalue, searchfield):
    proj_file = open("data.json",'r')
    read_data = json.load(proj_file)
    i = 0 
    proj_counter = 0
    while i < len(read_data["User_Projects"]):
        if read_data['User_Projects'][i]["User_Email"] == usermail :
            proj_counter += 1
            if searchvalue == read_data['User_Projects'][i][searchfield] :
                print(f"{Fore.YELLOW}************************************{Fore.RESET}")
                print(f"{Fore.YELLOW}             Project({proj_counter}){Fore.RESET}")
                print(f"{Fore.YELLOW}************************************{Fore.RESET}")
                for elem in Proj_Meta[1:] :
                    print(f"{elem} --------> {read_data['User_Projects'][i][elem]}")
                    print(f"{Fore.BLUE}----------------------{Fore.RESET}")
            else:
                if i == (len(read_data["User_Projects"])-1):
                    print(f"{Fore.RED}\n-----Project Not Found------\n{Fore.RESET}")
        i += 1



#---------------------------DEFINE FUNCTION-------------------------------------
def searchproj():
    search_list()
    if user_input == 1: 
        searchstart = chk.date_validate("Project Start Date")
        searching(searchstart,"Project_Start_Date")
    elif user_input == 2: 
        searchend = chk.date_validate("Project End Date")
        searching(searchend,"Project_End_Date")
#--------------------Rechoosing From Login Options----------------------
    elif user_input == 3:
        from loginoptions import listing_options, userchoose, choose_from
        listing_options()
        userchoose()
        choose_from() 
#--------------------Rechoosing From Login Options----------------------
    from loginoptions import listing_options, userchoose, choose_from
    listing_options()
    userchoose()
    choose_from() 
    
#------------FINAL VERSION V2.0.1