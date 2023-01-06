#------------------------- RUN ---> MainScript.py --> to run Project---------------------------

import json
import constrains as chk
import time
from colorama import Fore
import login
#------------------------------------------------------
login.usr_valid_email

Proj_Meta = [ "User_Email" ,"Project_Title"  , "Project_Details" , "Project_Target", "Project_Start_Date" , "Project_End_Date"]
def values(usr_valid_email):
    global Proj_Meta
    #---------------------------------------------
    title_name = chk.TitleCheckExistance("Project Title")
    #---------------------------------------------
    Details = input(f"{Fore.LIGHTYELLOW_EX}Add Your Project Details: {Fore.RESET}")
    #----------------------------------------------
    target_fund = chk.confirm_number("Funding Total Target in $ currency: ")
    #----------------------------------------------
    def get_date():
        proj_st_date = chk.date_validate("Project_Start_Date")
        proj_end_date = chk.date_validate("Project_End_Date")
        while True :
            d1 = time.strptime(proj_st_date, "%d/%m/%Y")
            d2 = time.strptime(proj_end_date, "%d/%m/%Y")
            if d1 < d2:
                break
            else:
                print(f"{Fore.RED}*Wrong Entey .. End Date can't be earler than Start Date{Fore.RESET}")
                print(f"{Fore.RED}*Please re-enter the data of the date: {Fore.RESET}")
                proj_st_date = chk.date_validate("Project_Start_Date")
                proj_end_date = chk.date_validate("Project_End_Date")
        return proj_st_date , proj_end_date 

    date_list = get_date()
    Proj_Starts = date_list[0]
    Proj_Ends = date_list[1]
    #---------------------------------------------------------------------------
    user_mail = login.usr_valid_email
    #---------------------------------------------------------------------------
    Proj_values = [user_mail, title_name, Details, target_fund, Proj_Starts,  Proj_Ends ]
    #----------------------------------------------------------------------------
    Project = {}
    for i in range(6):
        Project[Proj_Meta[i]] = Proj_values[i]
    #-----------------------------------------------------------------------------------
    proj_file = open("data.json",'r+')
    data = json.load(proj_file)
    data["User_Projects"].append(Project)
    proj_file.seek(0)
    json.dump(data, proj_file, indent = 6)
    proj_file.close()
    #-----------------------------------------------------------------------------------
    print(f"{Fore.GREEN}-----------------Project DATA----------------{Fore.RESET}\n")
    for elem in Proj_Meta[1:] :
        print(f"{Fore.LIGHTBLACK_EX}{elem} -------> {Project[elem]}{Fore.RESET}\n")
    print(f"{Fore.GREEN}---------Project Created Succesfully---------{Fore.RESET}\n")
    #------------------------------------------------------------------------------------
    #--------------------Rechoosing From Login Options----------------------
    from loginoptions import listing_options, userchoose, choose_from
    listing_options()
    userchoose()
    choose_from() 
    
#Finall Version v2.0.2
