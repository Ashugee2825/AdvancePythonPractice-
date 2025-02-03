''' 
for control variable in range(5):

for control variable in range(5,10):

range(5) --->   5 is end
range (1, 5)

Array is a collection of similar type of elements that have a contiguous memory location.

iteralbe: An object that can be iterated over. An object which implements the __iter__ method. 

iteable means that the object can be iterated over. example of iterable objects are list, tuple, string, dictionary etc.




'''

for i in range(5):
    print(i)

for j in [5,10]:
    print(j)

for k in 'Kodnest':
    print(k)

for l in (5,10):
    print(l)           

for j1 in 'Kodnest' :
    print(j1, end="")

for j2 in [10,20,30]:
    print(j2 +  50)

for num in range(1, 11):
    print(num, end=",")
'''
for (int i = 0; i < 10; i++)    # Java
{
    System.out.println(i);
}   
'''

for num2 in range(1, 10):
    print(num2)

for num3 in range(1, 21,2):
    print(num3, end="  ")

for i3 in range(5):
    print(i3, end=" ")


# WAP to print all even numbers between 1 to 20
for i in range(1, 21):
    if(i % 2 == 0):
        print(i, end=",")


# WAP to print all odd numbers between 1 to 20
for i in range(1, 21):
    if(i % 2 != 0):
        print(i, end=",")


# WAP to print all numbers between 1 to 20 which are divisible by 3
for i in range(1, 21):
    if(i % 3 == 0):
        print(i, end=",")


# WAP to print all numbers between 1 to 20 which are not divisible by 3
for i in range(1, 21):
    if(i % 3 != 0):
        print(i, end=",")


# WAP to print all numbers between 1 to 20 which are divisible by 3 and 5
for i in range(1, 21):
    if(i % 3 == 0 and i % 5 == 0):
        print(i, end=",")

# WAP to print all numbers between 1 to 20 which are divisible by 3 or 5
for i in range(1, 21):
    if(i % 3 == 0 or i % 5 == 0):
        print(i, end=",")

# WAP to print all numbers between 1 to 20 which are divisible by 3 and not by 5
for i in range(1, 21):
    if(i % 3 == 0 and i % 5 != 0):
        print(i, end=",")

# WAP to print all numbers between 1 to 20 which are divisible by 5 and not by 3
for i in range(1, 21):
    if(i % 3 != 0 and i % 5 == 0):
        print(i, end=",")

# WAP to print all numbers between 1 to 20 which are not divisible by 5 and 3
for i in range(1, 21):
    if(i % 3 != 0 and i % 5 !=0 ):
        print(i, end=",")


# WAP to print all numbers between 1 to 20 which are not divisible by 5 or 3



# WAP to print all numbers between 1 to 20 which are not divisible by 5 and not by 3



#whie loop  print (1 , 10)


# WAP to print numbers from 1 to 10 using while loop    
i = 1
while(i<10):
    print(i+100)
    i = i+1

    
# WAP to print number from 1-10 but if number is 6  then skip printing.
for i in range(1, 11):
    if i == 6:
        continue
    print(i)
    



# WAP to print number from 1-10 but if number is 5  then stop printing.         
for i in range(1, 11):
    if i == 6:
       break
    print(i)

#WAP     


def disp():
    pass

class Demo:
    pass

for number in range(1, 4):
    pass


