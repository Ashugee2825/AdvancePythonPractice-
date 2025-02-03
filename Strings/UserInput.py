# input() wil always as a string: input() function always returns a string value
# If you want to perform any arithmetic operation, you need to convert the string to int or float
# num1 = int(input("Enter the num1: "))
# num2 = int(input("Enter the num2: "))
# print('Value of num1 is:', num1, 'Data Type of num1 is:', type(num1))
# print(num1 + num2)
#


num1 = input("Enter the num1: ")
num2 = input("Enter the num2: ")
print('Value of num1 is:', num1, 'Data Type of num1 is:', type(num1))
print(num1 + num2)



num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: ")) 
print(f'Addtition of {num1}  and {num2} is {num1 + num2}')
print(f'Subtraction of {num1}  and {num2} is {num1 - num2}')
print(f'Multiplication of {num1}  and {num2} is {num1 * num2}')
print(f'Division of {num1}  and {num2} is {num1 / num2}')
print(f'Floor Division of {num1}  and {num2} is {num1 // num2}')
print(f'Modulus of {num1}  and {num2} is {num1 % num2}')
print(f'Exponent of {num1}  and {num2} is {num1 ** num2}')
print(f'Exponent of {num1}  and {num2} is {pow(num1, num2)}')
print(f'Exponent of {num1}  and {num2} is {pow(num1, num2, 3)}')
print(f'Exponent of {num1}  and {num2} is {pow(num1, num2, 5)}')


