class Employee:
    company_name = "Unknown"
    Employee_count = 0

    @classmethod
    def increment_employee_count(cls):
        cls.Employee_count += 1

    def __init__(self, name, age, designation, employee_id, salary):
        self.name = name
        self.age = age
        self.designation = designation
        Employee.Employee_count += 1

        self.employee_id = employee_id
        self.salary = salary

        #Increment employee count wheneever a new employee is created
        Employee.increment_employee_count()

name = input()  # John
employee_id = int(input())  # 101
salary = float(input())

employee = Employee(name, 25, "Software Developer", employee_id, salary)
print(f'Employee Name: {employee.name}') # Employee Name: John
print(f'Employee ID: {employee.employee_id}') # Employee ID: 101
print(f'Salary: {employee.salary}') # Salary: 50000.0
print(f'Total Employee: {Employee.Employee_count}') # Total Employee: 1
print("Employee Name: {employee.name}, ID: {employee.employee_id}, Salary: {employee.salary}, Total Employee: {Employee.Employee_count}")



# mam code
class Employee:
    company_name = "Unknown"
    employee_count = 0

    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        Employee.increment_employee_count()

    @staticmethod
    def company_policy():
        print("Company Policy: All employees must adhere to company ethics and integrity.")

    @classmethod
    def increment_employee_count(cls):
        cls.employee_count += 1

company_name = input()
Employee.company_name = company_name 

name = input()
employee_id = input()
salary = float(input())

employee = Employee(name, employee_id, salary)

print(f"Updated Employee Count: {Employee.employee_count}")
print(f"Company: {Employee.company_name}")
print(f"Employee Count: {Employee.employee_count}")
print(f"Employee Name: {employee.name}, ID: {employee.employee_id}, Salary: {int(employee.salary)}")
Employee.company_policy()
