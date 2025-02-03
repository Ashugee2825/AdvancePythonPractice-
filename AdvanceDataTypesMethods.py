# iterable  object
# List, Set, Dictionary, Tuple, String , range() are the iterable objects in python.

# # List (iterable object)


#li1 = list(5)
#print(li1) #    TypeError: 'int' object is not iterable

li1 = list('Kodnest')
print(li1) #['K', 'o', 'd', 'n', 'e', 's', 't']

li1 = list((10,20,30,40,50))
print(li1) #[10, 20, 30, 40, 50]

li1 = list({10,20,30,40,50})
print(li1) #[40, 10, 50, 20, 30]

li1 = list({'name': 'Kodnest', 'age': 24, 'phone': 1234567890})
print(li1) #['name', 'age', 'phone']

li1 = list(range(1,10))
print(li1) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

li2 = list((10,20))
print(li2) #[10, 20]

li3 = list((100,200))
print(li3) #[100, 200]

li4 = list({'Name': 'Kodnest', 'Age': 24})
li5 = list({'Name': 'Kodnest', 'Age': 24}.items())

li6 = range(1,101)
print(li6) 

tup1 = tuple([10,20,30]) 
print(tup1) # (10, 20, 30)
tup2 = tuple({100,200})
print(tup2)

tup3 = tuple(range(1,11))
print(tup3)

tup4 = tuple('Kodnest')
print(tup4) 

tup5 = tuple({'name':'Ashutosh', 'age' : 24})
print(tup5) # ('name', 'age')


# set(iterable_object):
s1 = set([10,20,30])
print(s1) # {10,20,30}

# dict (iterable_object: key:value)
d1 = dict([['name', 'Ashutosh'], ['age', '24']])
print(d1)  # {'name': 'Ashutosh', }


