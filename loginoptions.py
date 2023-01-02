from colorama import Fore
import login
import values
import Viewdetails as viewds
import EditList as edls
#DEFINE FUNCTION OF MENU AFTER LOGINING IN :
login_choose = ""
#------------------------------LISTING OPTIONS---------------------------------------
def listing_options():
    
    print(f"{Fore.LIGHTBLACK_EX} Please Choose Number from list {Fore.RESET}")
    
    options = ("View Projects","Create Project","Edit Project","Delete Project", "Cancel")
    for count, i in enumerate(options, 1):
        print(f"{count} ----> {i}")
#-------------------------------CALLING FUNCTION--------------------------------------
listing_options()
#-------------------------------USER CHOOSE OPTION------------------------------------

login_choose = input("Your Choice: ")
while True:
    if login_choose.isdigit():
        login_choose = int(login_choose)
        break
    else:
        print (f"{Fore.RED}*WRONG ENTERY ..... PLEASE ADD ONLY NUMBER*{Fore.RESET}")
        listing_options()
        login_choose = input("Your Choice :")
    
while True:
    if int(login_choose) in [1, 2, 3, 4, 5]:
        break
    else:
        print (f"{Fore.RED}*WRONG ENTERY ..... PLEASE ADD ONE NUMBER FROM THE FOLLOWING LIST*{Fore.RESET}")
        listing_options()
        login_choose = input("Your Choice :")  

#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
def choose_from():
    login.usr_valid_email
    if login_choose == 1 :
        print("View Projects")
        viewds.viewproj()
    #---------------------------------------------- 
    elif login_choose == 2:
        print("Create Your Own Project")
        values.values(login.usr_valid_email)
    #----------------------------------------------
    elif login_choose == 3 :
        print("Edit Projects")
        edls.edit_actions()
    #----------------------------------------------
    elif login_choose == 4 :
        print("Delete Projects")
    #----------------------------------------------
    elif login_choose == 5 :
        exit
#-------------------------------------------------------------------
choose_from()