''' 
1.In List we can store Homogeneous as wll as Heterogeneous Data type
2. In List we can store Duplicate values.
3.List is an Ordered Collection of Data: order of insertion is preserved.
4. Lists are mutable: we can change the elements of the list  or Once we create a list, we can modify it.
5. List is mutable, so we can add, remove, or change elements in a list after it has been created.
6. List is a dynamic data structure, so it can grow or shrink in size as needed.
7. List is a collection of elements enclosed within square brackets [] and separated by commas.
8. List is a collection of elements enclosed within square brackets [] and separated by commas.
9. List is a collection of elements enclosed within square brackets [] and separated by commas.



'''

lil =  [10, 20, 30, 40, True, 'Kodnest']
print(lil,type(lil))

# append() method: It is used to add an element at the end of the list.
lil.append(300)
print(lil)   #[10, 20, 30, 40, True, 'Kodnst', 300]


# insert() method: It is used to add an element at a specific index in the list. insert(index, element)
lil.insert(1,15)
print(lil)   #[10, 15, 20, 30, 40, True, 'Kodnest', 300]


#remove(element): It is used to remove the first occurrence of the specified element from the list. reove(ele):Remove the first occurrence of the element.
lil.remove(20) #[10, 15, 30, 40, True, 'Kodnest', 300]
print(lil)

#pop(): It is used to remove and return the last element from the list. pop():Remove the last element.

lil.pop() #[10, 15, 30, 40, True, 'Kodnest']
print(lil)
removed_element = lil.pop()
print(removed_element)  #Kodnest
# dIIFERENCE BETWEEN POP AND REMOVE METHOD
# The pop() method removes and returns the last element from the list.
# The remove() method removes the first occurrence of the specified element from the list.
# The pop() method takes an optional index parameter to remove and return an element from a specific index.
# The remove() method does not return any value.


del lil[1]  #[10, 30, 40, True, 'Kodnest']  #del is a keyword used to delete an element from the list using the index. difference between pop and del is pop return the element and del does not return the element.
print(lil)

del lil 
print(lil)  #NameError: name 'lil' is not defined



#clear() method: It is used to remove all the elements from the list.
lil.clear()




#in and not in operator: It is used to check if an element is present in the list or not. It returns True if the element is present in the list, otherwise False.
print(10 in lil)  #True
print('Kodnest' in lil)  #True
print(200 in lil)  #False



#len() function: It is used to get the number of elements in the list.
print(len(lil))  #5