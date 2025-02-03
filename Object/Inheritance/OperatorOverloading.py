class Demo1:
    def display1(self):
        print("This is Inside display of Demo1 class")
    def __str__(self):
        return 'Hello'    
class Demo2:
    def display(self):
        print("This is Inside display of Demo2 class")
    def __str__(self):
        return 'hi'    
d1 = Demo1()
d2 = Demo2()


''' 
In Python if we print reference variable then it will dispalay string representation of an address of an object.


In the above example we have overridden the display method of Demo1 class in Demo2 class.

'''
print(d1)  # <__main__.Demo1 object at 0x0000021D3D3A3A00>
print(d2)  # <__main__.Demo2 object at 0x0000021D3D3A3A30>

# print(d1 + d2)  # TypeError: unsupported operand type(s) for +: 'Demo1' and 'Demo2'

print("--------------------------------------------------")


# mam Code 
class Demo11:
    def disp1(self):
        print('Inside disp1')
    def __str__(self):
        return 'Hello'
    def __add__(self,other):
        self.a = 20
        self.b = 30
        return self.a + other.b
    
class Demo22:
    def disp2(self):
        print("Inside disp2")
    def __str__(self):
        return 'Hi'
d1 = Demo11()
d2 = Demo22()
print(d1)
print(d2)
# print(d1 + d2) # 50

'''
In Python if we print reference variable then internally python
will invoke __str__() which always returns string representation of an 
address of an object. 

In the above examples we have overridden __str__ methods in their
respective classes.

Dunder Methods:  The method which has suffix as prefix __ and suffix __
These dunder methods are also called as magic methods or special methods.
These dunder methods can be called as Magic 

'''


class Demo111:
    def __str__(self):
        return 'Hello'
    def __sub__(self,other):
        self.a = 20
        self.b = 30
        return self.a - other.b
    
class Demo222:
    def disp2(self):
        print("Inside disp2")
    def __str__(self):
        return 'Hi'
d1 = Demo111()
d2 = Demo222()
print(d1)
print(d2)
#print(d1 - d2)  # -10


class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_sound(self):
        print(f"{self.name} says: Woof! Woof!")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_sound(self):
        print(f"{self.name} says: Meow! Meow!")

dog_name = input()
cat_name = input()

dog = Dog(dog_name)
cat = Cat(cat_name)

dog.make_sound()
cat.make_sound()