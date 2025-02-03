from abc import ABC, abstractmethod

'''
Abstraction in Python 
Abstraction is used to hide the internal functionality of the function from the users.
The users only interact with the basic implementation of the function, but inner working is hidden.
User is familiar with that "what function does" but they don't know "how it does."
In Python, an abstraction is used to hide the irrelevant data/class in order to reduce the complexity.
It also enhances the application efficiency.
In Python, we use abstract classes and methods to define the abstraction.

Abstract class: A class that is never intended to instantiate is known as an abstract class.

Abstract method: A method that is declared in the abstract class, but it does not have any implementation is known as an abstract method.

Example: of Abtraction in Python
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

# Driver code
dog = Dog()
cat = Cat()
print(dog.make_sound())  # Output: Bark
print(cat.make_sound())  # Output: Meow

'''

class Shape(ABC):  # Abstract class
    def __init__(self, name):  # Constructor
        self.name = name  # Instance variable

    @abstractmethod
    def area(self):  # Abstract method
        pass  # Abstract method should not have implementation

class Circle(Shape):  # Child class
    def __init__(self, name, radius):  # Constructor
        super().__init__(name)  # Calling parent class constructor
        self.radius = radius  # Instance variable

    def area(self):  # Concrete method
        return 3.14 * self.radius ** 2  # Implementing area method

c1 = Circle("Circle", 4)  # Creating object of Circle class
print(c1.area())  # Output: Area of the circle


class Demo1(ABC):  # Abstract class
    @abstractmethod
    def disp1(self):  # Abstract method
        print("Inside disp1")   # Inside disp1

class Demo1Impl(Demo1):  # Child class
    def disp1(self):    # Concrete method 
        print("Inside disp1 implementation")  # Inside disp1 implementation

d1 = Demo1Impl()  # Creating object of Demo1Impl class
d1.disp1()  # Inside disp1 implementation


print("-----------------------------------")

class Demo11(ABC):  # Abstract class 
    pass  # Empty class

# d1 = Demo11()  # This will raise TypeError because we cannot instantiate an abstract class without concrete methods


class Demo2(ABC):   # Abstract class
    def disp2(self):  # Concrete method 
        print("Inside disp2")   # Inside disp2

d2 = Demo2()  # Creating object of Demo2 class 
d2.disp2() # Inside disp2        

'''
If abstract class does not have method any then object for that abstract class can be created.

If abstract class have only concrete methods then object for that abstract class can be created and concrete methods can be invoked. 



'''

print("-----------------------------------")

class Demo3(ABC):   # Abstract class
    def info(self):  # Concrete method
        print("Inside info")  # Inside info
    @abstractmethod  # Abstract method
    def disp3(self):  # Abstract method 
        print("Inside disp3") # Inside disp3

class Demo4(Demo3):  # Child class
    def disp3(self):  # Implementing abstract method
        print("Inside disp3 implementation")  # Inside disp3 implementation

d4 = Demo4()  # Creating object of Demo4 class
d4.info()  # Inside info
d4.disp3()  # Inside disp3 implementation


import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2, 2)

    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)

# Taking user input for dimensions
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
radius = float(input("Enter the radius of the circle: "))

# Creating instances
rectangle = Rectangle(length, width)
circle = Circle(radius)
# Displaying area and perimeter
print(f"Rectangle Area: {rectangle.area()}")
print(f"Rectangle Perimeter: {rectangle.perimeter()}")
print(f"Circle Area: {circle.area()}")
print(f"Circle Perimeter: {circle.perimeter()}")