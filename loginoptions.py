#------------------------- RUN ---> MainScript.py --> to run Project---------------------------

from colorama import Fore
import login
import values
import Viewdetails as viewds
import EditList as edls
import DeleteProj as delproj
import searching
#DEFINE FUNCTION OF MENU AFTER LOGINING IN :
login_choose = ""
#------------------------------LISTING OPTIONS---------------------------------------
def listing_options():
    
    print(f"{Fore.LIGHTBLACK_EX}***Choose Number from list {Fore.RESET}")
    
    options = ("View Projects","Create Project","Edit Project","Delete Project","Project Search Using Project_Dates", "Cancel")
    for count, i in enumerate(options, 1):
        print(f"{Fore.LIGHTCYAN_EX}{count} ----> {i}{Fore.RESET}")
    print(f"{Fore.LIGHTBLACK_EX}--------------------------------------{Fore.RESET}")

#-------------------------------CALLING FUNCTION--------------------------------------
listing_options()
#-------------------------------USER CHOOSE OPTION------------------------------------
def userchoose():
    global login_choose
    login_choose = input(f"{Fore.BLUE}Your Choice: {Fore.RESET}") 
    while True:
        if login_choose.isdigit() and int(login_choose) in [1, 2, 3, 4, 5, 6]:
            login_choose = int(login_choose)
            break
        else:
            print (f"{Fore.RED}*WRONG ENTERY ..... ADD ONE NUMBER FROM THE FOLLOWING LIST*{Fore.RESET}")
            listing_options()
            login_choose = input(f"{Fore.BLUE}Your Choice: {Fore.RESET}") 
#--------------------------------------------------------------------------------------------------------
userchoose()
#--------------------------------------------------------------------------------------------------------
def choose_from():
    login.usr_valid_email
    if login_choose == 1 :
        print(f"{Fore.GREEN}-------View Projects-------{Fore.RESET}")
        viewds.viewproj()
    #---------------------------------------------- 
    elif login_choose == 2:
        print(f"{Fore.GREEN}-------Create Project------{Fore.RESET}")
        values.values(login.usr_valid_email)
    #----------------------------------------------
    elif login_choose == 3 :
        print(f"{Fore.GREEN}------Edit Projects------{Fore.RESET}")
        edls.edit_actions()
    #----------------------------------------------
    elif login_choose == 4 :
        print(f"{Fore.GREEN}------Delete Projects------{Fore.RESET}")
        delproj.delete_actions()
    #----------------------------------------------
    elif login_choose == 5 :
        print(f"{Fore.GREEN}------Searching for Project------{Fore.RESET}")
        searching.searchproj()
    #----------------------------------------------
    elif login_choose == 6 :
        quit
#-------------------------------------------------------------------
choose_from()

#------------FINAL VERSION V2.0.1