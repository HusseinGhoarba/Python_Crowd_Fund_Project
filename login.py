#Importing Required Libraries
import constrains as chk
from colorama import Fore
# import loginoptions as lnoptions
#-----------------------------------LOGIN FUNCTION--------------------------------------------
usr_valid_email = ""
def loginaction():
    #get information from user ---------------------------------------------------------------
    global usr_valid_email
    usremail = chk.email_add()
    userpassword = input("Enter Password: ")
    #check user existance --------------------------------------------------------------------
    userdataf = open("userdata.txt", "r")
    for i in userdataf:
        userinfos = i.strip('\n')
        userinfos = userinfos.split(":")
        if len(userinfos) < 4:
            continue
        elif userinfos[2] == usremail and userinfos[3] == userpassword:
            print(f"{Fore.GREEN}----------------Logged In Successfully-----------------------{Fore.RESET}")
            usr_valid_email = usremail
            import loginoptions
            break
    else:
        print(f"{Fore.RED}----------------Unsuccesfuly: User Not Found---------------------------{Fore.RESET}")
        import mainfund
    userdataf.close()
#----------------------------