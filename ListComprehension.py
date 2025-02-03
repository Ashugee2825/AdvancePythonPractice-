'''
list Comprehension: 
[expression ]



li1 = []



: if and else both in list Comprehension :
li = [1,2,3] 
exprected_output = ['']

'''

# 
# 
# li1 = [1,2,3,4,5]
# print(li1)
# sq_li = []
# for i in li1:
    # sq_li.append(i**2)
# print(sq_li)    
# 
# 


li1 = [1,2,3,4,5]
duplicate_li1 = [i for i in li1]

# when we have only if part then write it after for loop.
even = [i for i in li1 if i%2 == 0] 
sq_list = [i ** 2 for i in li1] 
new_li1 = [ele+2 for ele in li1]

#when we have if-else both write it before fro loop
even_odd = ['even' if i%2 == 0 else 'odd' for i in li1]


# mutiple for loop Nested for loops inside list comprehsion 
li = [[10,20],[30,40],[50,60]]
new_li = [ele for sublist in li for ele in sublist]






