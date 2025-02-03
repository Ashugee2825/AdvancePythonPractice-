# li = input('Enter space seperated Elements')
# print(li,type(li)) #10 20 30 40 <class 'str'>
# 
# print('k o d n '.split())  #['k', 'o', 'd', 'n']
# print(li)
# 
# li = list(map(int,li))
# print(li)  #[10,20]
# 
# 


# 
# # tup = tuple(map(int,input('Enter Space separated Element ').split()))
# print(tup)



li = list(map(int, input().split()))
print([i for i in li if i % 2 == 0])

