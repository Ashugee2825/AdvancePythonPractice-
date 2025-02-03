class Student: # Parent Class Student 
    def cook(self): # Define a method cook()  
        print("Student can cook cooking") # Print a message 
    def play(self): # Define a method play() 
        print("Student can play cricket") # Print a message

class Employee(Student): # Child Class Employee
    def work(self): # Define a method work()
        print("Employee can cook Working") # Print a message
    def cook(self): # Define a method cook()
        print("Employee can play cooking ") # Print a message

e= Employee() # Create an object of class Employee 
e.play() # Student can play cricket


# In the above example, the method cook() of the Employee class is called using the super() function.
# The super() function is used to call the methods of the superclass.
# The super() function returns a temporary object of the superclass, which allows us to call the methods of the superclass.
# The super() function can also be used to call the constructor of the superclass.

'''
work(): specialized method of Employee class : only implemented in Employee class
play(): inherited method of Student class 
cook(): Overridden method of Employee class 
'''
