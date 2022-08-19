from json.encoder import INFINITY
from re import X
from xml.dom import UserDataHandler
import itertools 

def user_details():
    """
    Prompt user input
    """
    #Checking if users first name has a digit or not
    
    for x in itertools.repeat([]):
        nameFirst=input("Insert your first name\n").lower()
        if (any(x.isdigit() for x in nameFirst)) or len(nameFirst)==0:
            print("invalid first name\n")
            continue
        else:
            break
        
    for x in itertools.repeat([]):
        nameLast=input("Insert your last name\n").lower()
        if (any(x.isdigit() for x in nameLast)):
            print("invalid last name\n")
            continue
        else:
            break
           
    for x in itertools.repeat([]):
        campYear=int(input("Insert your cohort ( year of attendance 2022+ )\n"))
        if(campYear < 2022):
            print("Invalid cohort\n")
            continue
        else:
            break
    

    for x in itertools.repeat([]):
        campuses=input("Insert the campus you will be attending in(Durban, Jhohannesburg, Cape Town, Phokeng)  \n")
        if user_campus(campuses)==-1:
            continue
        else:
            break

    #printing final username on the screen
    
    print(create_user_name(nameFirst,nameLast,campYear,campuses))




def create_user_name(first_name, last_name, cohort, final_campus):
    """
    Create and return a valid username
    """
    name=""
    if(len(first_name)==1):
        name=name+first_name[:]+'oo'
    if(len(first_name)<3):
        name=name+first_name[:]+'o'
    elif(len(first_name))>3:
        name=name+first_name[-3:]
        
    if(len(last_name)==1):
        name=name+last_name[:]+'oo'
    if(len(last_name)<3):
        name=name+last_name[:]+'o'
    elif(len(last_name))>=3:
        name=name+last_name[0:3]    
        
    name=name+str(cohort)
    name=name.lower()+user_campus(final_campus)
    
    
    
    return name

    

def user_campus(campus):
    """
    Return valid campus abbreviations
    """
    campName=''
    if campus == 'Johannesburg':
        campName= 'JHB'
    elif campus == 'Durban':
        campName= 'DBN'
    elif campus == 'Cape Town':
        campName='CPT'
    elif campus == 'Phokeng':
         campName='Pho'
    elif campus == 'johannesburg':
        campName= 'JHB'
    elif campus == 'durban':
        campName= 'DBN'
    elif campus == 'cape town':
        campName='CPT'
    elif campus == 'phokeng':
         campName='Pho'
    else:
        return "not found"                               

    return campName    


if __name__ == '__main__':
    user_details()