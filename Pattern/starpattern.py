
# n = 5
# 
# print('*'* n)
# print('*'* n)
# print('*'* n)
# print('*'* n)
# print('*'* n)

'''      
rows  = 4
col = 5
for i in range(rows):
    for j in range(col):
        print('*', end=' ')
    print()
  '''

# 
# *  1 Star
# **  2 Star
# *** 3 Star
# **** 4 Star
# ***** 5 Star

rows = 4
col = 5
for i in range(rows):
    for j in range(col):
        print('*', end=' ')
    print()

print("---------------------------------------------------------------")

rows = 5
print()
for i in range(rows):
    for j in range(i+1):
        print('*', end=' ')
    print()

print("---------------------------------------------------------------")


print()
for i in range(rows):
    for j in range(i, rows):
        print('*', end=' ')
    print()

print("---------------------------------------------------------------")


rows = 5
print()
for i in range(rows):
    for j in range(i+1):
        print('*', end=' ')
    print()
for i in range(rows):
    for j in range(i, rows-1):
        print('*', end=' ')
    print()

print("---------------------------------------------------------------")


rows = 5
print()
for i in range(rows):
    for j in range(i+1):
        print('*', end=' ')
    print()
print()    
for i in range(rows):
    for j in range(i, rows):
        print('*', end=' ')
    print()

print("---------------------------------------------------------------")



print()
for i in range(rows):
    for j in range(i + 1):
        print('*', end=' ')
    for j in range(i, rows):
        print('-', end=' ')   
    print()



print("---------------------------------------------------------------")


print()
for i in range(rows):
    for j in range(i + 1):
        print('*', end=' ')
    for j in range(i, rows):
        print('-', end=' ')   
    for j in range(i, rows):
        print('-', end=' ')
    for j in range(i + 1):
        print('*', end=' ')        
    print()



print("---------------------------------------------------------------")



    
print()
for i in range(rows):
    for j in range(i + 1):
        print('*', end="")
    for j in range(i, rows-1):
        print('', end="")   
    for j in range(i, rows-1):
        print('', end="")
    for j in range(i + 1):
        print('*', end="")        
    print()
for i in range(rows):
    for j in range(i,rows-1):
        print('*', end="")
    for j in range(i +1):
        print('-', end="")   
    for j in range(i +1):
        print('-', end="")
    for j in range(i + 1):
        print('*', end="")        
    print()



print("---------------------------------------------------------------")



for i in range(rows):
        for j in range(i, rows):
            print("", end='')
        for j in range(i):
            print('*', end='')
        for j in range(i+1):
            print('*', end='')
        print()
for i in range(1,rows):
    for i in range(i):
        print(' ', end='')            
