class Student:
    college = 'Kodnest'
    def get_info(self):
        print(f'College Name is: ', Student.college)
        

    @classmethod
    def change_college(cls, new_college):
        cls.college = new_college  # cls.college is same as Student.college

s1 = Student()  # creating object of Student class
s1.get_info()   # College Name is: Kodnest
Student.change_college('code')  # changing college name
s1.get_info()    # College Name is: code


