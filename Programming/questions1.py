class Product:
    def __init__(self,p_name,price,stock):
        self.p_name = p_name
        self.price = price
        self.stock = stock

    def display_info(self):
        print(f'Product Name: {self.p_name}, Price: {self.price}, Stock: {self.stock}')
    
    def update_price(self,newPrice):
        self.price = newPrice
        print(f'Updating price to {newPrice}...')
        print(f'New Price: {newPrice}')
    
    def update_stock(self, newstock):
        self.stock = newstock
        print(f'Updating stock to {newstock}...')
        print(f'New Stock: {newstock}')

p_name = input()
price = float(input())
stock = int(input())
newprice = float(input())
newstock = int(input())

p1 = Product(p_name,price,stock)
p1.display_info()
p1.update_price(newprice)
p1.update_stock(newstock)



class Vechile:
    def __init__(self,make,model,year,weight,is_avilable=True):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.is_avilable = is_avilable
    
    def display_info(self):
        status = "Available" if self.is_avilable else ""
        print(f'Vechile: {self.make} {self.model} {self.year} {self.weight}')

    def update_weight(self,newWeight):
        self.weight = newWeight
        print(f'Updating weight to {newWeight}...')
        print(f'New Weight: {newWeight}')

# mam code
class Product:
    def __init__(self,p_name,price,stock):
        self.p_name = p_name
        self.price = price
        self.stock = stock

    def display_info(self):
        print(f'Product Name: {self.p_name}, Price: {self.price}, Stock: {self.stock}')
    
    def update_price(self,newPrice):
        self.price = newPrice
        print(f'Updating price to {newPrice}...')
        print(f'New Price: {newPrice}')
    
    def update_stock(self, newstock):
        self.stock = newstock
        print(f'Updating stock to {newstock}...')
        print(f'New Stock: {newstock}')

p_name = input()
price = float(input())
stock = int(input())
newprice = float(input())
newstock = int(input())

p1 = Product(p_name,price,stock)
p1.display_info()
p1.update_price(newprice)
p1.update_stock(newstock)



class Student:
            def __init__(self,rollno,name,grade):
                self.rollno = rollno
                self.name = name
                self.grade = grade

            def dispaly_info(self):
                 print(f'Roll No: {self.rollno}, Name: {self.name}, Grade: {self.grade}')  

            def update_grade(self,newgrade):
                self.grade = newgrade
                print(f'Updating grade to {newgrade}...')
                print(f'New Grade: {newgrade}')