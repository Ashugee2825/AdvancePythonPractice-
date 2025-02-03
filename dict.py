# Dictionary is a collection of key-value pairs.
# Dictionary is mutable.
# Dictionary is represented by {}.
# Dictionary is an unordered collection of data.
# Dictionary does not support indexing of data.
# Dictionary does not support slicing of data.
# Dictionary does not support negative indexing of data.




d1 = {'a': 1, 'b': 2}
d2 = {'name' :"Ashutosh", 'age': 24,'phone': 1234567890}
print(d1, type(d1)) #{'a': 1, 'b': 2}

#In dictionary we cannot store Duplicate keys.
#In dictionary we can store Duplicate values.
d2['name']= 'pooja'
print(d1) #{'a': 1, 'b': 2} 
print(d2) #{'name': 'pooja', 'age': 24, 'phone': 23456}

#In dictionary we can store Duplicate values.
marks = {'Maths': 90, 'Physics': 80, 'Chemistry': 90, 'Maths': 95}  #Allowed


#In dictionary we cannot store Duplicate keys.
# marks = {'Maths': 90, 'Physics': 80, 'Chemistry': 90, 'Maths': 95}  #Not Allowed
# print(marks) #SyntaxError: duplicate key 'Maths' 



marks = {'Sci' : 85, 'Maths': 90, 'Physics': 80, 'Chemistry': 90} #allowed

for i in d1.keys():
    print(i) #a b

for i in d1.values():
    print(i) #1 2  

for i in d1.items():
    print(i) #('a', 1) ('b', 2)

  #  list(), tuple(), set(), bool(), dict(), str(), int(), float(), complex() are the built-in functions in python.  
  # more about built-in functions in python: https://docs.python.org/3/library/functions.html
  #            