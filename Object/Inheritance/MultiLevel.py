'''   

class Demo1:
    def disp1(self):
        print("Inside disp1")
class Demo2:
    def disp2(self):
        print("Inside disp2")
class Demo3(Demo1, Demo2):
    pass
d3 = Demo3()
d3.disp1()  # Inside disp1
d3.disp2()  # Inside disp2    
        

'''
print("------------------------------------------------------------")

'''  
class Demo1New:  # Renamed class to avoid conflict
    def disp(self):  # Same method name as in Demo1
        print("Inside disp1 of Demo1New")  # Updated method body to reflect new class name
class Demo2:  # Same class name as in Demo2
    def disp2(self):  # Same method name as in Demo2
        print("Inside disp2")  # Same method body as in Demo2
class Demo3(Demo1New, Demo2): # Inherit from Demo1New and Demo2
    pass  # No new method
d3 = Demo3()  # Create an instance of Demo3
d3.disp()  # Inside disp1 of Demo1New

  #MRO means Method Resolution Order. It is the order in which methods are inherited in the case of multiple inheritance.
    #In the above example, the method disp() of Demo1 is inherited because it is the first class in the inheritance list.
    #If we change the order of inheritance, the output will be different.
    # Example of Method Resolution Order (MRO)
    class A:
        def method(self):
            print("A method")

    class B(A):
        def method(self):
            print("B method")

    class C(A):
        def method(self):
            print("C method")

    class D(B, C):
        pass

    d = D()
    d.method()  # B method

    # To see the MRO
    print(D.__mro__)  # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

    # The MRO is D -> B -> C -> A -> object
    # It means that the method resolution order is D -> B -> C -> A -> object.
    # It is the order in which the methods are inherited in the case of multiple inheritance.
    # In the above example, the method method() of class B is inherited because it is the first class in the inheritance list.
    # If we change the order of inheritance, the output will be different.
    # Example of Method Resolution Order (MRO)
    

'''


class Demo11:  # Define a class Demo1
    def __init__(self): # Define a constructor
        self.x = 100 # Initialize an instance variable
class Demo22: # Define a class Demo2
    def __init__(self):
        self.x = 200
class Demo33(Demo22, Demo11):
    def __init__(self):
        self.x = 300

d33 = Demo33()
print(d33.x)  # 300

print("------------------------------------------------------------")

class Demo111:
    def __init__(self):
        self.x = 100
class Demo222:
    pass
class Demo333(Demo222, Demo111):
    pass

d333 = Demo333()
print(d333.x)  # 100