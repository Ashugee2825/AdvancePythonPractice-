''' 
Method Chaining is the process of calling one method from another method with respect to the current object.
Method Chaining: Method chaining is a technique used to call multiple methods of the same object in a single line.
Method chaining is done using the super() function.
The super() function is used to call the methods of the superclass.
The super() function returns a temporary object of the superclass, which allows us to call the methods of the superclass.
The super() function can also be used to call the constructor of the superclass.
The super() function is useful in multiple inheritance.
The super() function is used to call the methods of the superclass in the subclass.
The super() function is used to call the constructor of the superclass in the constructor of the subclass.
The super() function is used to call the methods of the superclass in the subclass.




'''

class GrandParent: # Define a class GrandParent
    def cook(self): # Define a method cook()
        print("GrandParent can cook Biryani") # Print a message

class Parent(GrandParent): # Define a class Parent
    def cook(self): # Define a method cook()
        print("Parent can cook kheer") # Print a message
 
class Child(Parent): # Define a class Child
    def cook(self): # Define a method cook()
        print("Child wont cook") # Print a message
        super().cook()  # Call the cook() method of the Parent class using super() function 
        super(Parent, self).cook() # Call the cook() method of the Parent class using super() function with arguments Parent and self 

c = Child() # Create an object of class Child
c.cook()  # Child wont cook 
p = Parent() # Create an object of class Parent
p.cook()  # Parent can cook kheer
g = GrandParent() # Create an object of class GrandParent
g.cook()  # GrandParent can cook Biryani
