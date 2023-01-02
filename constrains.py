import time
#Check Constraints Files -------->
def name_add(hell):
  inputs = input(f"Enter {hell} name: ")
  while True:
      if inputs.isalpha(): 
          break
      else:
          print("Invalid Entery") 
          inputs = input(f"Enter {hell} name: ")
  return inputs

def email_add():
    import re
    email = input("Add Email : ")
    emailpat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    while True:   
        if re.fullmatch(emailpat, email):
            break
        else:
            print("*Invalid Sytnax of Email")
            email = input("Add Email : ")
    return email

def add_pass():
    added = input("Enter Password: ")
    while True:
        if len(added) > 0 :
            break
        else:
            print("*Password Doesn't Match")
            added = input("Enter Password: ")
    return added

def confirm_pass(givenpass):
    confpass = input("Re-enter Password: ")
    while True:
        if confpass == givenpass:
            break
        else:
            print("*Password Doesn't Match")
            confpass = input("Re-enter Password: ")
    return confpass

def confirm_number(target):
    confnum = input(f"Add {target}: ")
    while True:
        if confnum.isdigit():
            break
        else:
            print("*Your Entery isn't number")
            confnum = input(f"Add {target}: ")
    return confnum

def date_validate(name):
    import re
    date_pattern = r'^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$'
    date = input(f"Add {name} : ")
    while True:
        if re.fullmatch(date_pattern, date):
            break
        else:
            print("*Your for date should be in this form dd/mm/yyyy ")
            date = input(f"Add {name} : ")
    return date

