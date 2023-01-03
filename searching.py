import login
from values import Proj_Meta
import json
from colorama import Fore
import constrains as chk
#-------------------------------------------------------------------------------
usermail = login.usr_valid_email
#--------------------------------------------------------------------------------
#---------------------------DEFINE FUNCTION-------------------------------------
def searchproj():
    searchstart = chk.date_validate("Project Start Date")
    searchend = chk.date_validate("Project End Date")
    proj_file = open("data.json",'r')
    read_data = json.load(proj_file)
    i = 0 
    while i < len(read_data["User_Projects"]):
        if read_data['User_Projects'][i]["User_Email"] == usermail :
            if searchstart == read_data['User_Projects'][i]["Project_Start_Date"] and searchend == read_data['User_Projects'][i]["Project_End_Date"]:
                print(f"{Fore.YELLOW}************************************{Fore.RESET}")
                for elem in Proj_Meta[1:] :
                    print(f"{elem} --------> {read_data['User_Projects'][i][elem]}")
                    print(f"{Fore.BLUE}----------------------{Fore.RESET}")
            else:
                if i == (len(read_data["User_Projects"])-1):
                    print(f"{Fore.RED}-----Project Not Found------{Fore.RESET}")
        i += 1
#--------------------------------------------------------------------------------
    #--------------------Rechoosing From Login Options----------------------
    from loginoptions import listing_options, userchoose, choose_from
    listing_options()
    userchoose()
    choose_from() 