s = input()
postion,character = input().split()  # ['5', 'k']


postion = int(postion)

mutation = mutate_string(s, postion, character)



def mutation(s, postion, character):
    return mutate_string(s, postion, character)

s = input()
postion,character = input().split()  # ['5', 'k']
mutation(s,int(postion),character)



'''
list('Kodn') # ['K', 'o', 'd', 'n']
li = ['K', 'o', 'd', 'n']
li[1] = 'O'

list are mutable and strings are immutable in python
mutable means that the object can be changed after it is created, and immutable means that it can't be changed after it is created.

'''
 
def mutate_string(string, position, character):
    li = list(string)
    li[position] = character
    string = ''.join(li)
    return string

s = input()
postion,character = input().split()  # ['5', 'k']
res = mutate_string(s, int(postion), character) 
print(res) # 'kodnest'

