print('Hello World'.islower()) # False

#PYTHON -----python
print('Hello World'.swapcase()) # hELLO wORLD
print('a'.islower()) # True
print('KODNEST'.isupper()) # True

S = input() # 'PythoN' --- 'pYTHOn'
print(S.swapcase()) # 'pYTHOn'


print('---------------------------')
def swap_case(s):  # 'PythoN' --- 'pYTHOn'
    sample = ''
    for i in s:
        if i.islower():  # 
            sample += i.upper()
        else:
            sample += i.lower()
    return s.swapcase()

res = swap_case('PythoN')
print(res)



print('---------------------------')


        