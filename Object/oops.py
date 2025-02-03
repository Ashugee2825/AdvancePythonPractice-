'''
OOPs in Python: Object Oriented Programming 

It is a programming paradigm that provides a means of structuring programs so that properties and behaviors are bundled into individual objects. 

For example, a car is an object which has certain properties such as color, model, and certain behaviors such as accelerating, stopping, and so on.

In Python, an object is created using the class keyword.

A class is a blueprint for the object.

We can think of class as a sketch of a parrot with labels. It contains all the details about the name, colors, size etc. Based on these descriptions, we can study about the parrot. Here, a parrot is an object.

The example for class of parrot can be :


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

    def get_age(self):
        return self.age

# Example usage:
my_dog = Dog("Buddy", 3)
print(my_dog.bark())  # Output: Buddy says woof!
print(my_dog.get_age())  # Output: 3





'''