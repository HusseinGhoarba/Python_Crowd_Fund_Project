#------------------------- RUN ---> MainScript.py --> to run Project---------------------------

#Importing Required Libraries:
import constrains as chk
import usedfun as uf
from colorama import Fore
#------------------REGISTER FUNCTION-----------------------------------------------
def registeraction():
    fname = chk.name_add("first")
    lname = chk.name_add("last")
    email = chk.email_add()
    password = chk.add_pass()
    confirmpass = str(chk.confirm_pass(password))
    numberph = chk.phone_number()
    finalphonum = f"{numberph}\n"
    uf.fileinsert(f"{fname}:{lname}:{email}:{password}:{confirmpass}:{finalphonum}")
    print(f"{Fore.GREEN}\n----User Created Successfully---\n{Fore.RESET}")
    return "1"
#------------FINAL VERSION V2.0.1