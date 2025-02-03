''' String are immutable:
1.Once we declare the String we cannot modify it,
if we try to modify the string it will new string

2. If new string does not have any refernce variable then it will be removed.
3. Python Internally uses String interning.
4.String Interning is the Process of checking string interns pool
before creaing any new object.

whenever we want to create new object, Python first will check string intern pool, weather that object exits or not.


'''
# s1  = 'Kodnest' 

# s1.upper()
# print(s1)


# s1 = 'K'
# print(s1, id(s1))

s1 = 'Hello'
s2 = 'world'
print(s1, id(s1))
print(s2, id(s2))

print(s1[0]) #H
print(s1[-1])

print('s1 ID of H',id(s1[0]))
print("s1 id of o", id(s1[-1 ]))

print('s2 ID of w:', id(s2[0]))
print('s2 ID of o: ', id(s2[1]))

