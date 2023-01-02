#Importing Required Libraries:
import constrains as chk
import usedfun as uf
#------------------REGISTER FUNCTION-----------------------------------------------
def registeraction():
    fname = chk.name_add("first")
    lname = chk.name_add("last")
    email = chk.email_add()
    password = chk.add_pass()
    confirmpass = str(chk.confirm_pass(password))
    numberph = input("Enter Phone Number: ")
    finalphonum = f"{numberph}\n"
    uf.fileinsert(f"{fname}:{lname}:{email}:{password}:{confirmpass}:{finalphonum}")
    return "1"