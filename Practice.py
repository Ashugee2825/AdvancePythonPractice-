print(bool('Kodnest'))   # true
#  print(int('Kodnest'))    # Error 
#print(int('12.22'))    #12.22 ---important
# print(float('Kodnet'))  # Error
print(float('12.22'))   # 12.22---most important
print(bool('   '))     # false
print(bool(0))         # false 
print(bool(12))         # true
# print(int('12.56'))   # error
print(int(12.56))       # 12


# taking float value from user and converting it into float
value = float(input("Enter Price: " 'Enter the value: '))  # 12.22

value = int(float(input("Enter Price: " 'Enter the value: '))) # 12.22
print(value, type(value))