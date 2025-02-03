class Employee
    company_name = 'code' # class variable  

    def __init__(self, name, age, design):
        self.name = name # instance variable
        self.age = age  # instance variable
        self.design = design
        
     def login(self,time):
        print(f'{self.name} is logged in at {time}')

    def logout(self,time):
        print(f'{self.name} is logged out at {time}')

    def work(self):
        print(f'{self.name} is working...{hours}')  # hours is not defined      
    
    def getDetails(self):
        print(f'Name: {self.name}
        print() Age: {self.age}, Designation: {self.design}')