# if String is holding integer then it can be converted to integer
a = '30'
print(a, type(a))
b = int(a)
print(b, type(b))


#string to integer conversion is not allowed if string is holding alphabets
# x = 'kod'
# print(x,type(x))
# y = int(x)
# print(y, type(y))



p = input('Enter Float type data:')  # 12.22
print(p, type(p))


#bool
q = 12
q = bool(q)
print(q, type(q))
q = bool(q)
print(q, type(q))

q = 0
q = bool(q)
print(q, type(q))
q = bool(q)
print(q, type(q))

'''
1.while converting int to bool for all non zero values it will return True

2. while Converting int to bool for 0 it will return False and empty string it will return False



'''