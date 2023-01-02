#------------------------------------------------------------#
            #To: Eng./ Abdullah Ashraf Elsayed
            #From: Hussein Amr Ghorabah
            #Track : DevOps - Mansoura Branch
#------------------------------------------------------------#
                    #lab3 - answer- Python
#------------------------------------------------------------#

#-------------------------------------------------------------------------------------
#Question NO.2 
#-------------------------------------------------------------------------------------
"""First Step of Project -CROWD FUNDING console app-"""
#-------------------------------------------------------------------------------------

#Importing pre-defined libraries

from colorama import Fore

#Definations of Functions which will be used in -CROWD FUNDING console app-


def fileinsert(info):
    try:
        fileobj = open("userdata.txt", "a")
    except Exception as ex:
        print(ex)
    else:
        fileobj.write(info)
        fileobj.close()

