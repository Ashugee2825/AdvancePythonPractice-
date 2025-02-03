''' 
1. In set we can store Homegeneous and Hetrogeneous values.
2. In set we cannot store Duplicate values.
3. Set is an Unordered Collection of Data: order of insertion is not preserved.
4. Set is mutable: we can change the elements of the set. or Once we create a set, we can modify it.
5. Set is represented by {}.
6. Set is mutable so we can add or remove elements from the set.
7.set does not support indexing of data.
8. set does not support slicing of data.
9. set does not support negative indexing of data.
10. set does not support negative slicing of data.  
11. In set we can not store duplicate values.
12. sets are mutable.

'''


# add(): used to add a single element to the set.
s1 = {10,True,'Kodnest',10,20,55.44}
print(s1,type(s1))
print(s1,type[s1]) #TypeError: 'set' object is not subscriptable
s1.remove(55.44)
print(s1) #{True, 10, 20, 'Kodnest'}
s1.add(100) 
print(s1) #{True, 100, 10, 20, 'Kodnest'}   
s1.pop(20) #TypeError: pop() takes no arguments
del s1[10] #TypeError: 'set' object doesn't support item deletion
s1.clear() #clear the set

# remove(): used to remove a single element from the set.
s1.pop() #KeyError: 'pop from an empty set'
print(s1) #NameError: name 'Print' is not defined


# del s1[2] #Error: TypeError: 'set' object doesn't support item deletion
del s1 #NameError: name 's1' is not defined





# update(): used to add multiple elements to the set.
s1 = {10,20,30,40,50}
s2 = {60,70,80,90,100}
s1.update(s2)
print(s1) #{100, 70, 40, 10, 80, 50, 20, 90, 60, 30}
s1.update([110,120,130,140,150])
print(s1) #{100, 70, 40, 10, 110, 80, 50, 20, 90, 120, 130, 140, 60, 30, 150}
s1.update((160,170,180,190,200))
print(s1) #{100, 70, 40, 10, 110, 80, 50, 160, 170, 180, 20, 90, 120, 130, 140, 60, 30, 150, 190, 200}


