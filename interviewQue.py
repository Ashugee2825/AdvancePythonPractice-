for y in range(1, 11):         # print 1 to 10
    z = 200              # global variable

def disp(a):     # a is a parameter
    print(a)    # 50
    y = 100       # local variable
    print(y)    #100


disp(50)     #50
print(y)     #10 
print(z)     #200
//print(a)   print #Error     





# Loop to print numbers from 1 to 10
for y in range(1, 11):         
    print(y)  # This will print numbers from 1 to 10

# Function definition
def disp(a):     # 'a' is a parameter
    print(a)    # This will print the value of 'a', which is 50 when the function is called
    y = 100     # 'y' is a local variable within the function
    print(y)    # This will print the local variable 'y', which is 100

# Function call
disp(50)     # This calls the function 'disp' with the argument 50, so it prints 50 and then 100

# The following lines will cause errors:
print(y)     # This will cause an error because 'y' is not defined in this scope. 
             # 'y' inside the function 'disp' is local to that function and the 'y' in the loop is also local to the loop.
print(z)     # This will cause an error because 'z' is not defined anywhere in the code.
//print(a)   # This will cause an error because 'a' is a parameter of the function 'disp' and is not accessible outside of it.






# Explain  Login Required Decorator
# Explain  Login Required Decorator with arguments 

# Explain diff ttypes of request
#Deleting nth Node
#Reverse a linked list
#Find the middle of a linked list
#Find the intersection point of two linked lists
#Detect a loop in a linked list
#Remove a loop in a linked list
#Merge two sorted linked lists
#Reverse a linked list in groups of k
#Rotate a linked list
#Clone a linked list with next and random pointer
#Flatten a linked list
#Check if a linked list is a palindrome
#Add two numbers represented by linked lists
#Check if a linked list is a palindrome
#Add two numbers represented by linked lists
#Find the length of a linked 




