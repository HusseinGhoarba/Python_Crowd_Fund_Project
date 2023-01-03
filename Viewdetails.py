import login
from values import Proj_Meta
import json
#-------------------------------------------------------------------------------
usermail = login.usr_valid_email
#--------------------------------------------------------------------------------
#---------------------------DEFINE FUNCTION-------------------------------------
def viewproj():
    proj_file = open("data.json",'r')
    read_data = json.load(proj_file)
    i = 0 
    while i < len(read_data["User_Projects"]):
        if read_data['User_Projects'][i]["User_Email"] == usermail :
            for elem in Proj_Meta[1:] :
                print(f"{elem} --------> {read_data['User_Projects'][i][elem]}")
        i += 1
#--------------------------------------------------------------------------------
