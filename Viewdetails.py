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
    while i < len(read_data["User_Projects"]):
        if read_data['User_Projects'][i]["User_Email"] == usermail :
            print(f"{Fore.YELLOW}************************************{Fore.RESET}")
            for elem in Proj_Meta[1:] :
                print(f"{elem} --------> {read_data['User_Projects'][i][elem]}")
                print(f"{Fore.BLUE}----------------------{Fore.RESET}")
        i += 1
    #--------------------Rechoosing From Login Options----------------------
    from loginoptions import listing_options, userchoose, choose_from
    listing_options()
    userchoose()
    choose_from() 
#--------------------------------------------------------------------------------