
#Scripting way for Writing the code:
print('Scripting way of Printing: hello World')


#Procedural way of writing the code
# Define a function called 'message' that encapsulates the print logic.
# Functions help organize code into reusable blocks.
def message_procedural():
    # This is the function body that executes when 'message_procedural()' is called.
    print('Inside method message: Hello world')

# Call the function to execute the print statement inside it.
message_procedural()

#Object Oriented way of Writing the code:
class Demo1:
    def instance_method(self):
        print('Object oriented way of printing: Hello world')
d1 = Demo1() 

d1.instance_method()    


# Scripting way for Writing the code:
# Directly printing the output without using any functions or classes.
# This is the simplest form of coding, often used for quick scripts or testing.
print('Scripting way of Printing: hello World')

# Procedural way of writing the code:
# Define a function called 'message' that encapsulates the print logic.
# Functions help organize code into reusable blocks.
def message():
    # This is the function body that executes when 'message()' is called.
    print('Inside method message: Hello world')

# Call the function to execute the print statement inside it.
message()

# Object Oriented way of Writing the code:
# Define a class called 'Demo'.
class Demo:
    # Define a method inside the class. 'self' refers to the instance of the class.
    def instance_method(self):
        # This method will print a message when called through an object.
        print('Object oriented way of printing: Hello world')

# Create an instance (object) of the Demo class.
d1 = Demo() 

# Call the method 'instance_method' using the object 'd1'.
d1.instance_method()
