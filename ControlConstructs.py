#print("one")
#print("two")

#print("three")  

'''
1. Conditional: if-else, if-elif
2. Looping: for, while
3.Jumping: break, continue, pass

'''

def checkAgeSimple(age):
    if(age>18):
        print("Age is greater than 18")
    else:
        print("Age is less than 18")
        checkAgeSimple(18)
        return age
    
    # WAP to display 'Child' if age is below 18, display 'Adult' if age is above 18, display 'Senior Citizen' if age is above 65.

def checkAge(age):  
    if(age<18):
        print("Child")
    elif(age>18 and age<65):
        print("Adult")
    else:
        print("Senior Citizen")




def displayAgeCategory(age):
    if(age<18):
        print("Child")
    elif(age>18 and age<65):
        print("Adult")
    else:
        print("Senior Citizen")
displayAgeCategory(int(input("Enter Age: ")))        

