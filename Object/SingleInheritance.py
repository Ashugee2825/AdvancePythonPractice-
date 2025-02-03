class Demo1:   # Parent class 
    def fun1(self):   # instance method
        print("This is fun1 of Demo1 class")  # This is fun1 of Demo1 class

class Demo2(Demo1):  # Child class
    def disp1(self):  # instance method
        print("This is disp1 of Demo2 class") # This is disp1 of Demo2 class
 
d2 = Demo2()  # creating object of Demo2 class
d2.disp1()  # This is disp1 of Demo2 class
d2.fun1()  # This is fun1 of Demo1 class








