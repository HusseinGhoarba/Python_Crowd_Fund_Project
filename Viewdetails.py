#------------------------- RUN ---> MainScript.py --> to run Project---------------------------

import login
from values import Proj_Meta
import json
from colorama import Fore
#-------------------------------------------------------------------------------
usermail = login.usr_valid_email
#--------------------------------------------------------------------------------
#---------------------------DEFINE FUNCTION-------------------------------------
def viewproj():
    proj_file = open("data.json",'r')
    read_data = json.load(proj_file)
    i = 0 
    proj_counter = 0
    noproj_flag = 0 
    while i < len(read_data["User_Projects"]):
        if read_data['User_Projects'][i]["User_Email"] == usermail :
            noproj_flag = 1
            proj_counter += 1 
            print(f"{Fore.YELLOW}************************************{Fore.RESET}")
            print(f"{Fore.YELLOW}             Project({proj_counter}){Fore.RESET}")
            print(f"{Fore.YELLOW}************************************{Fore.RESET}")
            for elem in Proj_Meta[1:] :
                print(f"{elem} --------> {read_data['User_Projects'][i][elem]}")
                print(f"{Fore.BLUE}----------------------{Fore.RESET}")
        i += 1
        
    if noproj_flag == 0 :
        print(f"{Fore.RED}\n----- There is No Project -----\n{Fore.RESET}")

    #--------------------Rechoosing From Login Options----------------------
    from loginoptions import listing_options, userchoose, choose_from
    listing_options()
    userchoose()
    choose_from() 
#--------------------------------------------------------------------------------

#------------FINAL VERSION V2.0.2