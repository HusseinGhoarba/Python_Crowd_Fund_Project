
#------------------------- RUN ---> MainScript.py --> to run Project---------------------------

#Importing Required Libraries
import constrains as chk
from colorama import Fore
import maskpass
# import loginoptions as lnoptions
#-----------------------------------LOGIN FUNCTION--------------------------------------------
usr_valid_email = ""
def loginaction():
    #get information from user ---------------------------------------------------------------
    global usr_valid_email
    usremail = chk.email_add()
    userpassword = maskpass.askpass(prompt= f"{Fore.LIGHTYELLOW_EX}Enter Password: {Fore.RESET}", mask="*")
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
        import MainScript
    userdataf.close()
#------------FINAL VERSION V2.0.2