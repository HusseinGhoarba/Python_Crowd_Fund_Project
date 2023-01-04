#------------------------- RUN ---> MainScript.py --> to run Project---------------------------

from colorama import Fore
import constrains as chk
import time
import login
from values import Proj_Meta
import json
#-------------------------------Edit Options FUNCTION--------------------------------------
def edit_options():
    print(f"{Fore.LIGHTBLACK_EX}*CHOOSE FIELD NUMBER FOR EDITING ----- :{Fore.RESET}")
    options = ("Project Title","Project Details","Project Total Fund", "Project Dates", "Cancel")
    for count, i in enumerate(options, 1):
        print(f"{Fore.CYAN}{count} ----> {i}{Fore.RESET}")
    print(f"{Fore.LIGHTBLACK_EX}--------------------------------------{Fore.RESET}")
#-------------------------------USER CHOOSE OPTION------------------------------------
def edit_list():
    edit_options()
    user_input = input(f"{Fore.BLUE}Your Choice: {Fore.RESET}")
    while True:
        if user_input.isdigit() and int(user_input) in [1, 2, 3, 4, 5]:
            user_input = int(user_input)
            break
        else:
            print (f"{Fore.RED}*WRONG ENTERY ..... PLEASE ADD ONE NUMBER FROM THE FOLLOWING LIST*{Fore.RESET}")
            edit_options()
            user_input = input(f"{Fore.BLUE}Your Choice: {Fore.RESET}")

    return user_input
#--------------------------------------------------------------------------------------------------------
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
#---------------------------------GOOING TO DESTINATION------------------------------------------------
usermail = login.usr_valid_email
#---------------------------DEFINE FUNCTION-------------------------------------
def editproj(idfield , newvalue, thirdarg="None", newvaluetwo="None"):
    proj_title = chk.name_add("Project Title To Modify")
    proj_file = open("data.json")
    read_data = json.load(proj_file)

    length_projects = int(len(read_data['User_Projects']))

    for item in range(length_projects) :
        if read_data['User_Projects'][item]["User_Email"] == usermail and read_data['User_Projects'][item]["Project_Title"] == proj_title :
            read_data['User_Projects'][item][idfield] = newvalue
            if thirdarg == "None" :
                print("--------------------------")
            else:
                read_data['User_Projects'][item][thirdarg] = newvaluetwo
            rewrite = open('data.json', 'w')
            json.dump(read_data, rewrite, indent=6 )
            rewrite.close()
            print(f"{Fore.GREEN}------Edited Successfully------{Fore.RESET}")
    
        
    proj_file.close()
    #--------------------Rechoosing From Login Options----------------------
    from loginoptions import listing_options, userchoose, choose_from
    listing_options()
    userchoose()
    choose_from() 
    
#--------------------------------------------------------------------------------

#---------------------------------DEFINE ACTIONS FUNCTIONS-----------------------------------------------

def edit_actions():
    choosed = edit_list()
    if choosed == 1 :
        field = "Project_Title"
        editval = chk.name_add("new project_title ")
        editproj(field , editval)
    elif choosed == 2 :
        field = "Project_Details"
        editval = input("Add New Project Details: ")
        editproj(field , editval)
    elif choosed == 3:
        field = "Project_Target"
        editval = chk.confirm_number("New Total Fund")
        editproj(field , editval)
    elif choosed == 4:
        field = ["New Project_Start_Date", "New Project_End_Date"]
        editval = get_date()
        editproj(field[0] , editval[0], field[1], editval[1])
    elif choosed == 5 :
        #--------------------Rechoosing From Login Options----------------------
        from loginoptions import listing_options, userchoose, choose_from
        listing_options()
        userchoose()
        choose_from() 
        
#------------FINAL VERSION V2.0.1