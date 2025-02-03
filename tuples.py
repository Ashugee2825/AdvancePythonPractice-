''' 
In Tuple We can stor Homogeneous and Heterogeneous elements or Data type.
In Tuple we can store Duplicate values.
Tuple is an Ordered Collection of Data: order of insertion is preserved.
Tuple is immutable: we cannot change the elements of the tuple. or Once we create a tuple, we cannot modify it.
'''

tup1 = (10,22.55, 'Kodnest', True,10)
print(tup1)
print(tup1,type(tup1))
print(tup1[2]) #Kodnest
print(tup1[1:4]) #(22.55, 'Kodnest', True)
print(tup1[1:4:2]) #(22.55, True)
print(tup1[-1]) #10
print(tup1[-1:-4:-1]) #(10, True, 'Kodnest')
print(tup1[-1:-4]) #()


del tup1 #NameError: name 'tup1' is not defined
print(tup1) #NameError: name 'tup1' is not defined


tup1,append(100)  #AttributeError: 'tuple' object has no attribute 'append' #Tuple is immutable so we cannot add or remove elements from the tuple.
tup1.insert(1,15) #AttributeError: 'tuple' object has no attribute 'insert' #Tuple is immutable so we cannot add or remove elements from the tuple.
tup1.remove(10) #AttributeError: 'tuple' object has no attribute '__remove' #Tuple is immutable so we cannot add or remove elements from the tuple.
tup1.pop() #AttributeError: 'tuple' object has no attribute 'pop' #Tuple is immutable so we cannot add or remove elements from the tuple.
del tup1[1] #TypeError: 'tuple' object doesn't support item deletion #Tuple is immutable so we cannot add or remove elements from the tuple.
del tup1 #NameError: name 'tup1' is not defined
tup1.clear() #AttributeError: 'tuple' object has no attribute 'clear' #Tuple is immutable so we cannot add or remove elements from the tuple.


#create a singleton Tuple
tup1 = (10,) #tuple with single element
print(tup1) #(10,)
print(tup,type(tup1)) #(10,) <class 'tuple'>    
print(len(tup1)) #1

# Tuple is immutable so we cannot change the elements of the tuple.
new_tup = (10,20,30,40,50) 
new_tup_list = list(new_tup)


# new_tup_list[2] = 100
new_tup = tuple(new_tup_list)
print(new_tup)  # (10, 20, 100, 40, 50)
ele1 = new_tup[2]   
print(ele1) #100

# Unpacking of Tuple
ele1, ele2, ele3, ele4, ele5 = new_tup
print('Value of ele1:', ele1) #Value of ele1: 10






t1 = (10, 20, 30, 40, 50)
t2 = (60, 70, 80, 90, 100)
t3 = t1 + t2
print(t3)  #(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

# Tuple is immutable so we cannot change the elements of the tuple.
# We can concatenate two or more tuples using the + operator.
# We can repeat a tuple multiple times using the * operator.
# We can check if an element is present in the tuple using the in and not in operators.
# We can find the length of a tuple using the len() function.
# We can access elements of a tuple using indexing and slicing.
# We can unpack a tuple into multiple variables.




    