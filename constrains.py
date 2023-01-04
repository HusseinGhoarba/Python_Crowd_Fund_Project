#------------------------- RUN ---> MainScript.py --> to run Project---------------------------

from colorama import Fore
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
    added = input(f"{Fore.LIGHTYELLOW_EX}Enter Password: {Fore.RESET}")
    while True:
        if len(added) > 0 :
            break
        else:
            print("*Password Doesn't Match")
            added = input(f"{Fore.LIGHTYELLOW_EX}Enter Password: {Fore.RESET}")
    return added

def confirm_pass(givenpass):
    confpass = input(f"{Fore.LIGHTYELLOW_EX}Re-enter Password: {Fore.RESET}")
    while True:
        if confpass == givenpass:
            break
        else:
            print("*Password Doesn't Match")
            confpass = input(f"{Fore.LIGHTYELLOW_EX}Re-enter Password: {Fore.RESET}")
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

#------------FINAL VERSION V2.0.1