print(10 // 2)
print(True and False)   # False
print(True or False)  # True
print(not True)  # False

A = 1 # ON
B = 0 # OFF
result = A and B  # Both need to be ON for result to be 1
print("Are both switches ON? ", result)

result = A or B  # Any one switch need to be ON for result to be 1

print("Is any one switch ON? ", result)
result = not A  # If A is ON then result will be OFF
print("Is switch A OFF? ", result)
result = not B  # If B is OFF then result will be ON

print("Is switch B ON? ", result)   # True  
