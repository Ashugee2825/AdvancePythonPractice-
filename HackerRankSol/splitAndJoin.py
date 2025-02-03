s = input().split()
print('-'.join(s)) # 'this-is-a-string'

# print('---------------------------')  
def split_and_join(line):
     return '-'.join(line.split())
res = split_and_join('this is a string')
print(res) # 'this-is-a-string' 

# print('---------------------------')  
print('this is a string'.split('-')) # ['this is a string']
print('this-is-a-string'.split('-')) # ['this', 'is', 'a', 'string']
print('this-is-a-string'.split()) # ['this-is-a-string']
print('this-is-a-string'.split('-')) # ['this', 'is', 'a', 'string']
print('this-is-a-string'.split(' ')) # ['this-is-a-string']
print('this-is-a-string'.split('-')) # ['this', 'is', 'a', 'string']
print('this-is-a-string'.split(' ')) # ['this-is-a-string']


# print('---------------------------')
def split_and_join(line):   # 'this is a
     line = line.split()  # ['this', 'is', 'a']  
     return '-' .join(line)  # 'this-is-a'



# print('---------------------------')  
def print_full_name(a, b):
    print("Hello {} {}! You just delved into python.".format(a, b))
print_full_name('Ross', 'Taylor') # Hello Ross Taylor! You just delved into python.

#split  is created to split the string into a list of strings.
#join is created to join the list of strings into a single string.
#split is used to split a string into a list of strings. 
#join is used to join a list of strings into a single string.
# split is example of string to list is  'this is a string'.split() # ['this', 'is', 'a', 'string']
# join is example of list to string is '-'.join(s) # 'this-is-a-string'


