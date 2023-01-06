#------------------------- RUN ---> MainScript.py --> to run Project---------------------------
import login
from colorama import Fore
import maskpass
import json

#Check Constraints Files -------->
def name_add(hell):
  inputs = input(f"{Fore.LIGHTYELLOW_EX}Add {hell} name: {Fore.RESET}")
  while True:
      if inputs.isalpha(): 
          break
      else:
          print("Invalid Entery") 
          inputs = input(f"{Fore.LIGHTYELLOW_EX}Enter {hell} name: {Fore.RESET}")
  return inputs

def email_add():
    import re
    email = input(f"{Fore.LIGHTYELLOW_EX}Add Email : {Fore.RESET}")
    emailpat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    while True:   
        if re.fullmatch(emailpat, email):
            break
        else:
            print("*Invalid Sytnax of Email")
            email = input(f"{Fore.LIGHTYELLOW_EX}Add Email: {Fore.RESET}")
    return email

def add_pass():
    added = maskpass.askpass(prompt= f"{Fore.LIGHTYELLOW_EX}Enter Password: {Fore.RESET}", mask="*")
    while True:
        if len(added) > 0 :
            break
        else:
            print("*Password can't be empty")
            added = maskpass.askpass(prompt= f"{Fore.LIGHTYELLOW_EX}Enter Password: {Fore.RESET}", mask="*")
    return added

def confirm_pass(givenpass):
    confpass = maskpass.askpass(prompt= f"{Fore.LIGHTYELLOW_EX}Re_enter Password: {Fore.RESET}", mask="*")
    while True:
        if confpass == givenpass:
            break
        else:
            print("*Password Doesn't Match")
            confpass = maskpass.askpass(prompt= f"{Fore.LIGHTYELLOW_EX}Re_enter Password: {Fore.RESET}", mask="*")
    return confpass

def confirm_number(target):
    confnum = input(f"{Fore.LIGHTYELLOW_EX}Add {target}: {Fore.RESET}")
    while True:
        if confnum.isdigit():
            break
        else:
            print("*Your Entery isn't number")
            confnum = input(f"{Fore.LIGHTYELLOW_EX}Add {target}: {Fore.RESET}")
    return confnum

def date_validate(name):
    import re
    date_pattern = r'^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$'
    date = input(f"{Fore.LIGHTYELLOW_EX}Add {name}: {Fore.RESET}")
    while True:
        if re.fullmatch(date_pattern, date):
            break
        else:
            print(f"{Fore.RED}*Your for date should be in this form dd/mm/yyyy {Fore.RESET}")
            date = input(f"{Fore.LIGHTYELLOW_EX}Add {name}: {Fore.RESET}")
    return date

def phone_number():
    import re
    ph_pattern = r'^(\+201|01|00201)[0-2,5]{1}[0-9]{8}'
    phone = input(f"{Fore.LIGHTYELLOW_EX}Phone Number[Egypt]: {Fore.RESET}")
    while True:
        if re.fullmatch(ph_pattern, phone):
            break
        else:
            print(f"{Fore.RED}*Your for Phone should be compatible with Egypt phone numbers {Fore.RESET}")
            phone = input(f"{Fore.LIGHTYELLOW_EX}Phone Number[Egypt]: {Fore.RESET}")
    return phone

#check mail existance --------------------------------------------------------------------
def MailCheckExistance():
    mail = email_add()
    userdataf = open("userdata.txt", "r")
    for i in userdataf:
        userinfos = i.strip('\n')
        userinfos = userinfos.split(":")
        while True:
            if userinfos[2] != mail:
                break
            else:
                print(f"{Fore.RED}----------------Mail Exist before-----------------------{Fore.RESET}")
                mail = email_add()
    userdataf.close()
    return mail

def TitleCheckExistance(titlename):
    usermail = login.usr_valid_email
    title = name_add(titlename)
    proj_file = open("data.json",'r')
    read_data = json.load(proj_file)
    x = 0
    while x < len(read_data["User_Projects"]):
        i = 0
        if read_data['User_Projects'][x]["User_Email"] == usermail :
            while i < 6:
                if read_data['User_Projects'][i]["Project_Title"] == title:
                    print(f"{Fore.RED}----- There is a same title for other project -----{Fore.RESET}")
                    title = name_add(titlename)   
                i+=1
        x+=1
    return title
#------------FINAL VERSION V2.0.2