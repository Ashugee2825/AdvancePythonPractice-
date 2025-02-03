''' 
1. Constructor chaining is the process of calling one constructor from another constructor with respect to the current object.
2. In Python, constructor chaining is done using the super() function.
3. The super() function is used to call the constructor of the parent class.
4. The super() function returns a temporary object of the superclass, which allows us to call the constructor of the superclass.
5. The super() function can also be used to call the methods of the superclass.
6. The super() function is useful in multiple inheritance.
7. The super() function is used to call the constructor of the superclass in the constructor of the subclass.
8. The super() function is used to call the methods of the superclass in the subclass.
9. The super() function is used to call the constructor of the superclass in the constructor of the subclass.
10. constructor is not inherited in the subclass. So, we need to call the constructor of the superclass explicitly.
11.
'''

class GrandParent:
    def __init__(self): # Define a constructor
        def __init__(self): # in this line we are creating constructor in GrandParent class
            self.x = 100 # Initialize an instance variable
class Parent(GrandParent): # Define a class Parent
    def __init__(self): # Define a constructor
        self.y = 200 # Initialize an instance variable
class Child(Parent):  # Define a class child
    def __inti__(self): # Define a constructor
        self.z = 300 # Initialize an instance variable
        super().__init__() # Call the constructor of the Parent class

c = Child() # Create an object of class Child
print(c.z) # 300
print(c.y) # 200
print(c.x) # 100

