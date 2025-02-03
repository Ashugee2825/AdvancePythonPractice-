class Demo1: # Define a class Demo1
    def __init__(self, value=200): # Define a constructor
        self.x = value # Initialize an instance variable

d1 = Demo1() # Default value 200
print(d1.x)  # 200
''' git 
 when we create constructr in same class then only last declared constructor will be invoked at the time of object creation.

 Deifne Constructor in Inheritance 

# Constructor Overloading in Inheritance in Python  
class Demo1: # Define a class Demo1
    def __init__(self, value=200): # Define a constructor
        self.x = value # Initialize an instance variable

class Demo2(Demo1): # Define a class Demo2
    def __init__(self, value=400): # Define a constructor
        self.x = value # Initialize an instance variable

        
   git push  -u origin master
   
       

'''





