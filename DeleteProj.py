from colorama import Fore
import constrains as chk
import time
import login
from values import Proj_Meta
import json
#-------------------------------Edit Options FUNCTION--------------------------------------
def delete_options():
    print(f"{Fore.LIGHTBLACK_EX}*CHOOSE FIELD NUMBER FOR EDITING ----- :{Fore.RESET}")
    options = ("Delete Project", "Cancel")
    for count, i in enumerate(options, 1):
        print(f"{count} ----> {i}")

#-------------------------------USER CHOOSE OPTION------------------------------------
def delete_list():
    delete_options()
    user_input = input("Your Choice :")
    while True:
        if user_input.isdigit():
            user_input = int(user_input)
            break
        else:
            print (f"{Fore.RED}*WRONG ENTERY ..... PLEASE ADD ONLY NUMBER*{Fore.RESET}")
            delete_options()
            user_input = input("Your Choice :")
    
    while True:
        if int(user_input) in [1, 2]:
            break
        else:
            print (f"{Fore.RED}*WRONG ENTERY ..... PLEASE ADD ONE NUMBER FROM THE FOLLOWING LIST*{Fore.RESET}")
            delete_options()
            user_input = input("Your Choice: ")
              
    return user_input
#--------------------------------------------------------------------------------------------------------

#---------------------------------GOOING TO DESTINATION------------------------------------------------
usermail = login.usr_valid_email
#---------------------------DEFINE FUNCTION-------------------------------------
def editproj():
    proj_title = chk.name_add("Project Title")
    proj_file = open("data.json")
    read_data = json.load(proj_file)

    length_projects = int(len(read_data['User_Projects']))

    for item in range(length_projects) :
        if read_data['User_Projects'][item]["User_Email"] == usermail and read_data['User_Projects'][item]["Project_Title"] == proj_title :
            del read_data['User_Projects'][item]
            rewrite = open('data.json', 'w')
            json.dump(read_data, rewrite, indent=6 )
            rewrite.close()
            print(f"{Fore.GREEN}------Project Deleted------{Fore.RESET}")
            break
    else: 
        print(f"{Fore.RED}------Entery Not Found------{Fore.RESET}")
    proj_file.close()

    #--------------------Rechoosing From Login Options----------------------
    from loginoptions import listing_options, userchoose, choose_from
    listing_options()
    userchoose()
    choose_from() 
    
#--------------------------------------------------------------------------------

#---------------------------------DEFINE ACTIONS FUNCTIONS-----------------------------------------------

def delete_actions():
    choosed = delete_list()
    if choosed == 1 :
        editproj()
    elif choosed == 2 :
        #--------------------Rechoosing From Login Options----------------------
        from loginoptions import listing_options, userchoose, choose_from
        listing_options()
        userchoose()
        choose_from() 