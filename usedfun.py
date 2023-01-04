#------------------------- RUN ---> MainScript.py --> to run Project---------------------------

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

#------------FINAL VERSION V2.0.1